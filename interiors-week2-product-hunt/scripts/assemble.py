"""TEAM BLOCK 1 — Editorial assembly. Original observations stay separate from proposals.
Run from any directory. This module never edits earlier catalogues or downloads images.
Only offer-specific credible weights enter freight;missing values remain null.
"""
import json,math,csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
rows=load('data/evidence/selected.json');notes=load('data/evidence/detail-notes.json');guides=load('data/guides.json');markets=load('data/market-observations.json');images=load('data/image-manifest.json');cfg=load('data/settings.json')
for r in rows:
 i=r['id'];n=notes.get(str(i));r['brand']=n.get('brand','Other') if n else 'Other';r['description']=guides[r['group']].copy()
 if n:r['description'][0]=n['facts']+' '+guides[r['group']][0].split('. ',1)[-1]
 r['description'][0]='Selected style: '+r['name']+'. '+r['description'][0]
 r['description'][2]+=' Before choosing, compare the pictured finish with your room in natural light and confirm the exact size and quantity that will arrive.'
 r['detail_evidence']=n;r['image_record']=next(x for x in images if x['id']==i);r['market_context']=next((x for x in markets if x['group']==r['group']),None)
 r['jumia_search_url']=next(x['url'] for x in load('data/evidence/jumia-access.json') if x['id']==i)
 w=n.get('weight_g') if n else None;cm=n.get('packing_cm') if n else None
 # BLOCK 2 — Conditional item allocation,not a bookable parcel. Weight-only = lower bound.
 kg=max(w/1000,math.prod(cm)/cfg['divisor'] if cm else 0) if w else None
 r['chargeable_kg']=kg;r['freight_ngn']=math.ceil(kg*(cfg['air_usd_kg']*cfg['usd_ngn']+cfg['clearing_ngn_kg'])) if kg else None
 r['freight_status']='conditional supplier-piece allocation' if cm else ('weight-only lower bound;packing pending' if w else 'pending:credible selected-option packing missing')
 r['source_price_status']=n.get('source_price_cny') and 'Detail-page selected-option observation;reconfirm at checkout' or r['source_price_status'] if n else r['source_price_status']
 if n and n.get('source_price_cny') is not None:r['source_price_cny']=n['source_price_cny']
 # BLOCK 3 — Editable proposals,never a claim about historical retail prices.
 cost=max(r['source_price_cny'],cfg['source_floor_cny'])*cfg['usd_ngn']*cfg['cny_usd']+max(r['freight_ngn'] or 0,cfg['shipping_floor_ngn']);r['proposed_sale_ngn']=math.ceil(cost*cfg['markup']/100)*100
 discount=.12 if r['proposed_sale_ngn']<5000 else .10 if r['proposed_sale_ngn']<15000 else .08;r['proposed_compare_ngn']=math.ceil(r['proposed_sale_ngn']/(1-discount)/100)*100
(R/'data/products.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
keys=['id','day','daily_number','name','brand','category','url','source_price_cny','source_price_status','freight_ngn','freight_status','chargeable_kg','proposed_sale_ngn','proposed_compare_ngn','jumia_search_url']
with (R/'data/products.csv').open('w',newline='',encoding='utf-8-sig') as f:
 writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows({k:r.get(k) for k in keys} for r in rows)
print('Assembled',len(rows),'offers;',sum(bool(x['detail_evidence']) for x in rows),'detail reviews;',sum(x['freight_ngn'] is not None for x in rows),'conditional/lower-bound allocations')
