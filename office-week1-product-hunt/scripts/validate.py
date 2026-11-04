"""STRUCTURAL QA: checks arithmetic, provenance and earlier-file preservation.
A PASS does NOT certify procurement readiness, authenticity, safety or live prices.
Run after assemble.py and build.py. No network or third-party packages needed.
"""
import json,re,math,csv,hashlib
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1];E=R/'data/evidence'
d=json.loads((R/'data/products.json').read_text());ps=d['products'];cfg=d['metadata']['settings'];errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
check(len(ps)==250,'250records');check(len({p['source_url'] for p in ps})==250,'250uniqueoffers');check(Counter(p['day_number'] for p in ps)=={i:50 for i in range(1,6)},'5daysx50');check(Counter(p['group'] for p in ps)=={g:10 for g in {p['group'] for p in ps}},'10perfamily');check(len({p['group'] for p in ps})==25,'25families')
notes=json.loads((E/'detail-notes.json').read_text());check(len(notes)==25,'25representativepages')
for p in ps:
 i=p['id'];s=p['shipping'];v=p['planning'];j=p['jumia'];sections=p['description_sections'];n=len(re.findall(r"\b[\w’'-]+\b",' '.join(x['text'] for x in sections)))
 check(p['category']=='Office accessories' and p['author']=='DAVE ADEX',f'Identity{i}');check(150<=n<=200 and n==p['description_word_count'],f'Buyerlength{i}');check([x['heading'] for x in sections]==['What the Product is?','What are the clear benefits of the Product','Features of the Product'],f'Headings{i}')
 check(p['brand']=='Other' or re.fullmatch('[A-Za-z0-9 .,&-]+',p['brand']) is not None,f'Englishbrand{i}');check(re.fullmatch(r'https://detail\.1688\.com/offer/\d+\.html',p['source_url']) is not None,f'Canonicalurl{i}');check(len(p['images'])==1 and p['images'][0]['role']=='main',f'Mainonly{i}');check((R/p['images'][0]['local_path']).is_file(),f'Image{i}')
 check(v['source_floor_cny']>=5.2 and v['shipping_floor_ngn']>=2000,f'Floors{i}');check(v['compare_at_ngn']>v['sale_ngn'],f'Proposedcompare{i}');check(j['access']['query']==p['name'],f'Namesearch{i}');check(j['source_url'].startswith('https://www.jumia.com.ng/') and j['price_ngn']>0,f'Pricedcontext{i}');check(bool(j['pack_description']) and 'identical SKU not verified' in j['match'],f'Packandmatchcaveat{i}')
 if s['estimated_ngn'] is not None:
  check(str(i) in notes and s['supplier_weight_g']>0,f'Selectedfreightevidence{i}')
  if s['supplier_carton_cm']:
   kg=max(s['supplier_carton_weight_g']/1000,math.prod(s['supplier_carton_cm'])/cfg['volumetric_divisor'])/s['supplier_carton_quantity']
  else:kg=max(s['supplier_weight_g']/1000,math.prod(s['supplier_package_cm'])/cfg['volumetric_divisor'] if s['supplier_package_cm'] else 0)
  check(abs(kg-s['chargeable_kg_scenario'])<1e-9,f'Chargeablebasis{i}');check(abs(round(kg*(cfg['air_usd_kg']*cfg['usd_ngn']+cfg['clearing_ngn_kg']),2)-s['estimated_ngn'])<.011,f'Freightarithmetic{i}')
 else:check(s['chargeable_kg_scenario'] is None,f'Noinventedfreight{i}')
 cost=max(5.2,p['source_price_cny'])*cfg['cny_ngn']+max(2000,s['estimated_ngn'] or 0);check(math.ceil(cost*1.25/100)*100==v['sale_ngn'],f'Pricing{i}')
 check(abs(v['discount_percent']-round((1-v['sale_ngn']/v['compare_at_ngn'])*100,1))<.001,f'Discount{i}')
check(len(list((R/'assets/images').glob('*-main.jpg')))==250,'250mainfiles');check(len({p['images'][0]['catalogue_dom_url'] for p in ps})==250,'250distinctimageURLs');check(ps[90]['source_url'].endswith('/858408089598.html'),'Replacement91retained');check(all('553339987300' not in p['source_url'] for p in ps),'Nostock91excluded');check(ps[140]['source_price_cny']==1.2,'Scissorsselectedprice');check(ps[150]['shipping']['chargeable_kg_scenario']==.25,'Tape9050cartonallocation')
with (R/'data/products.csv').open(encoding='utf-8-sig') as f:
 rows=list(csv.DictReader(f));check(len(rows)==250,'CSV250rows');check(rows[150]['carton_units']=='80','CSVcartonbasis');check(rows[120]['jumia_pack_description']=='2 boxes×100 paper clips','CSVwholepackbasis')
check(abs(cfg['usd_ngn']*cfg['cny_usd']-cfg['cny_ngn'])<1e-8,'FXcrossrate')
conditional=sum(p['shipping']['estimated_ngn'] is not None for p in ps);weightonly=sum(p['shipping']['estimated_ngn'] is not None and not p['shipping']['supplier_package_cm'] and not p['shipping']['supplier_carton_cm'] for p in ps);cartons=sum(bool(p['shipping']['supplier_carton_cm']) for p in ps)
check(conditional==19 and weightonly==13 and cartons==1,'19conditional13lowerbounds1carton')
protected=json.loads((E/'preserved-catalogues-sha256.json').read_text());preservation={}
for name,digest in protected.items():
 path=R.parent/name;ok=path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==digest;preservation[name]=ok;check(ok,'Preserve:'+name)
report=dict(result='PASS' if not errors else 'FAIL',products=len(ps),days=dict(Counter(p['day_number'] for p in ps)),families=25,main_images=250,supplier_detail_pages=25,conditional_freight=conditional,unit_dimensional_scenarios=conditional-weightonly-cartons,carton_allocations=cartons,weight_only_lower_bounds=weightonly,pending_freight=250-conditional,priced_jumia_context_assignments=250,distinct_indexed_observations=len(json.loads((R/'data/market-observations.json').read_text())),verified_identical_jumia=0,description_words_min=min(p['description_word_count'] for p in ps),description_words_max=max(p['description_word_count'] for p in ps),earlier_files_preserved=preservation,errors=errors)
(R/'data/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not errors
