"""QA MODULE: structural/arithmetic/image checks,not safety or purchase certification.
Only new Week2 outputs are written. Previously protected files are read and hashed.
"""
import json,math,re,hashlib,csv
from pathlib import Path
from collections import Counter
from PIL import Image
R=Path(__file__).resolve().parents[1];E=R/'data/evidence'
def load(f):return json.loads(f.read_text())
d=load(R/'data/products.json');ps=d['products'];cfg=d['metadata']['settings'];ns=load(E/'detail-notes.json');errors=[]
def ck(ok,msg):
 if not ok:errors.append(msg)
ck(len(ps)==200 and len({p['source_url'] for p in ps})==200,'200uniqueoffers');ck(Counter(p['day_number'] for p in ps)=={i:40 for i in range(1,6)},'5x40');ck(len({p['group'] for p in ps})==20,'20families');ck(all(v==10 for v in Counter(p['group'] for p in ps).values()),'10perfamily');ck(len(ns)==20,'20detailpages')
prior=load(E/'excluded-earlier-electronics.json');prior_text=json.dumps(prior)
for p in ps:
 i=p['id'];s=p['shipping'];v=p['planning'];j=p['jumia'];im=p['images'];n=ns.get(str(i));texts=p['description_sections'];words=len(re.findall(r"\b[\w’'-]+\b",' '.join(x['text'] for x in texts)))
 ck(p['category']=='Electronics' and p['author']=='DAVE ADEX',f'Identity{i}');ck(p['source_url'] not in prior_text,f'NewOffer{i}');ck(150<=words<=200 and words==p['description_word_count'],f'Buyerlength{i}');ck([t['heading'] for t in texts]==['What the Product is?','What are the clear benefits of the Product','Features of the Product'],f'Headings{i}');ck(not re.search('[\u4e00-\u9fff]',p['name']+p['brand']),f'English{i}')
 ck(j['access']['query']==p['name'],f'ExactSearch{i}');ck(j['search_url'].startswith('https://www.jumia.com.ng/catalog/?q='),f'SearchURL{i}');ck(j['price_ngn'] is None or ('identical SKU not verified' in j['match'] and j['price_ngn']>0),f'JumiaCaveat{i}')
 ck(len(im)==1 and im[0]['role']=='main',f'MainOnly{i}');path=R/im[0]['local_path'];ck(path.is_file(),f'Image{i}')
 if path.exists():
  with Image.open(path) as img:img.verify()
 if s['estimated_ngn'] is not None:
  ck(n is not None and not n.get('freight_hold'),f'NoBatteryNormalFee{i}');kg=max(s['supplier_weight_g']/1000,math.prod(s['supplier_package_cm'])/6000 if s['supplier_package_cm'] else 0);ck(abs(kg-s['chargeable_kg_scenario'])<1e-9,f'WeightBasis{i}');fee=round(kg*(20.5*cfg['usd_ngn']+1500),2);ck(abs(fee-s['estimated_ngn'])<.001,f'Freight{i}')
 else:ck(s['chargeable_kg_scenario'] is None,f'PendingKg{i}')
 sale=math.ceil(1.25*(max(5.2,p['source_price_cny'])*cfg['cny_ngn']+max(2000,s['estimated_ngn'] or 0))/100)*100;ck(sale==v['sale_ngn'] and v['compare_at_ngn']>sale,f'Proposal{i}');ck(v['source_floor_cny']>=5.2 and v['shipping_floor_ngn']>=2000,f'Floors{i}')
ck(sum(p['shipping']['estimated_ngn'] is not None for p in ps)==12,'12conditional');ck(sum(p['jumia']['price_ngn'] is not None for p in ps)==130,'130contexts');ck(ps[160]['source_price_cny']==85 and ps[160]['catalogue_price_cny']==15,'UPSBodyNotCharger');ck(ps[50]['source_price_cny']==13,'USB3NotUSB2');ck(ps[60]['source_price_cny']==20 and '45W' in ps[60]['name'],'45WSelectedAdapter');ck(all(p['shipping']['estimated_ngn'] is None for p in ps[160:170]),'NoUPSNormalFreight')
with (R/'data/products.csv').open(encoding='utf-8-sig') as f:ck(len(list(csv.DictReader(f)))==200,'CSV200')
protected=load(E/'preserved-sha256.json');changed=[]
for name,digest in protected.items():
 path=R.parent/name
 if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:changed.append(name)
ck(not changed,'EarlierFilesUnchanged')
report=dict(result='PASS' if not errors else 'FAIL',products=200,days=5,per_day=40,families=20,main_images=200,supplier_detail_pages=20,conditional_freight=12,weight_only_lower_bounds=9,dimensional_scenarios=3,pending_freight=188,indexed_observations=28,priced_context_assignments=130,pending_jumia_prices=70,verified_identical_jumia=0,description_words_min=min(p['description_word_count'] for p in ps),description_words_max=max(p['description_word_count'] for p in ps),earlier_files_checked=len(protected),earlier_files_changed=changed,errors=errors,scope='Structural and arithmetic QA only; does not certify authenticity,safety,stock,dispatch or live-price completeness')
(R/'data/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not errors
