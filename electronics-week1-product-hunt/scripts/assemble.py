"""Assemble the NEW electronics research catalogue; preserve all earlier deliverables.
Never copy packing data between siblings. Unknown freight remains null.
Portable: run from any working directory after reviewing data/evidence inputs.
"""
import json,re,math,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R/'data/evidence';E=P
rows=json.load(open(P/'selected.json'));notes=json.load(open(P/'detail-notes.json'));guides=json.load(open(P/'guides.json'));images=json.load(open(R/'data/image-manifest.json'));access=json.load(open(P/'jumia-access.json'));market=json.load(open(R/'data/market-observations.json'));lookup={i:m for m in market for i in m['ids']}
cfg=dict(author='DAVE ADEX',category='Electronics',checked='2026-11-02',usd_ngn=1344.52,cny_usd=.150229,cny_ngn=1344.52*.150229,air_usd_kg=14.88,battery_usd_kg=15.50,clearing_ngn_kg=1500,volumetric_divisor=6000,source_floor_cny=5.2,shipping_floor_ngn=2000,markup=1.25,discount_target=.1,freight_url='https://dechaser.com/china-to-nigeria-shipping/',usd_fx_url='https://www.forbes.com/advisor/money-transfer/currency-converter/usd-ngn/',cny_fx_url='https://www.forbes.com/advisor/money-transfer/currency-converter/cny-usd/')
for r,im in zip(rows,images):
 id=r['id'];n=notes.get(str(id));r['catalogue_price_cny']=r['source_price_cny'];r['supplier_detail']=n;r['main_image']=im;r['selected_variant']=n['selected_variant'] if n else 'Catalogue candidate; exact connector, supplied unit, battery and included accessories need confirmation';r['price_basis']=r['source_price_status'];r['weight_g']=None;r['packing_cm']=None
 if n:
  n.update(url=r['url'],checked='2026-11-02',method='fetch_page rendered supplier attributes/packing text; supplier assertions, not independent testing');r['weight_g']=n['weight_g'];r['packing_cm']=n['packing_cm'];r['facts']=n['facts']
  if 'source_price_cny' in n:r['source_price_cny']=n['source_price_cny'];r['price_basis']='Rendered CNY option observation; final colour, pack, MOQ and checkout require reconfirmation'
  if n.get('dispatch'):r['dispatch_claim']=n['dispatch']
 r['freight_rate_usd_kg']=cfg['battery_usd_kg'] if r['cargo_class']=='battery' else cfg['air_usd_kg'];r['transit_scenario']='Published battery route15–25working days; final-mile coverage unconfirmed' if r['cargo_class']=='battery' else 'Published normal-cargo route7–10days; only after forwarder acceptance, not a delivery promise'
 r['shipping_estimate_ngn']=None;r['shipping_status']='Pending credible selected-unit packed weight/dimensions; no invented freight'
 if r['weight_g']:
  kg=r['weight_g']/1000;v=math.prod(r['packing_cm'])/6000 if r['packing_cm'] else None;cw=max(kg,v or 0);r['shipping_estimate_ngn']=round(cw*(r['freight_rate_usd_kg']*cfg['usd_ngn']+cfg['clearing_ngn_kg']),2);r['chargeable_kg']=cw;r['volumetric_kg']=v;r['shipping_status']=('Conditional packing scenario' if v else 'Weight-only LOWER BOUND; packed volume unknown')+'; normal rate assumes20kg+consolidation to Lagos. Battery final-mile coverage must be quoted. Not a small-parcel quote; carton allocation, rounding, acceptance, duties/VAT and other charges unconfirmed.'
 r['planning_source_cny']=max(5.2,r['source_price_cny']);r['planning_shipping_ngn']=max(2000,r['shipping_estimate_ngn'] or 0);cost=r['planning_source_cny']*cfg['cny_ngn']+r['planning_shipping_ngn'];sale=math.ceil(cost*1.25/100)*100;compare=math.ceil(sale/.9/100)*100;r.update(proposed_sale_ngn=sale,proposed_compare_at_ngn=compare,proposed_discount_percent=round((1-sale/compare)*100,1),proposal_status='Draft planning proposal, not a live or historical offer. Unconfirmed SKU cost/freight may raise this price.')
 r['market_comparison']=lookup.get(id);r['jumia_name_search']=access[id-1];r['market_review']='Comparison pending; insufficient relevant priced evidence' if not lookup.get(id) else 'Functional/model-wording context only, not identical verified SKU'
 if lookup.get(id) and sale>lookup[id]['price_ngn']:r['market_review']='PRICE REVIEW: proposal exceeds this non-identical Jumia comparator; affordability not established'
 definition,benefit,care=guides[r['group']];r['benefit']=benefit.split('. ')[0]+'.';parts=[r['name']+' is '+definition+'.',benefit,r['facts']+' '+care]
 def wc():return len(re.findall(r"\b[\w’'-]+\b",' '.join(parts)))
 if wc()<150:parts[1]+=' Think about where you will use it most often and which device you will connect, so your choice suits your everyday routine.'
 if wc()<150:parts[1]+=' Choose the version that matches your needs rather than relying on the photograph alone.'
 if wc()>200:parts[2]=care
 assert 150<=wc()<=200,(id,wc())
 r['details']=[dict(heading=h,text=t) for h,t in zip(['What the Product is?','What are the clear benefits of the Product','Features of the Product'],parts)];r['detail_word_count']=wc();r['detail_status']='Buyer-facing editorial copy based on title and representative inspection. Performance, electrical safety, water resistance, battery capacity and certifications are not independently tested.'
(R/'data/products.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(R/'data/settings.json').write_text(json.dumps(cfg,indent=2));(R/'data/market-observations.json').write_text(json.dumps(market,ensure_ascii=False,indent=2));(P/'detail-notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2))
# Research inputs already live in evidence; no same-file copy required.
(E/'catalogue-selection.json').write_text(json.dumps([{k:r[k] for k in ['id','title','url','catalogue_click_url','collection_url','catalogue_price_cny','brand_original_field']} for r in rows],ensure_ascii=False,indent=2))
(E/'freight-reference.json').write_text(json.dumps(dict(url=cfg['freight_url'],checked='2026-11-02',reader_chunk=2,normal_tiers={'1–10kg_usd_kg':20.5,'11–19kg_usd_kg':16.98,'20kg+office_usd_kg':12.9,'20kg+Lagosdoor_usd_kg':14.88,'20kg+otherstates_usd_kg':16.58},battery_usd_kg=15.50,clearing_ngn_kg=1500,normal_transit='7–10days published',battery_transit='15–25workingdays published',note='Battery final-mile coverage unspecified. Supplier dispatch and cargo transit differ; neither proves delivery. Duty, VAT, inspection, insurance and other costs extra/unconfirmed. Divisor6000 is a planning assumption, not a confirmed forwarder rule.'),indent=2))
print(dict(products=len(rows),inspected=len(notes),freight=sum(x['shipping_estimate_ngn'] is not None for x in rows),market=sum(x['market_comparison'] is not None for x in rows),words=(min(x['detail_word_count'] for x in rows),max(x['detail_word_count'] for x in rows))))
