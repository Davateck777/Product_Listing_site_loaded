"""QA MODULE: validate selection,arithmetic,packing provenance,copy andpreservation.
PASS means file/logic checks,not procurement readiness orproduct safety certification.
"""
import json,math,re,hashlib,csv
from pathlib import Path
from collections import Counter
from PIL import Image
R=Path(__file__).resolve().parents[1];E=R/'data/evidence'
def load(p):return json.loads(p.read_text())
d=load(R/'data/products.json');ps=d['products'];cfg=d['metadata']['settings'];notes=load(E/'detail-notes.json');errors=[]
def ck(ok,name):
 if not ok:errors.append(name)
ck(len(ps)==200 and len({p['source_url'] for p in ps})==200,'200uniqueoffers');ck(Counter(p['day_number'] for p in ps)=={i:40 for i in range(1,6)},'5x40');ck(Counter(p['group'] for p in ps)=={g:10 for g in load(E/'guides.json')},'20families10each');ck(len(notes)==19,'19readabledetails')
prior=json.dumps(load(E/'excluded-earlier-kitchen.json'));browser=load(E/'browser-inspection.json')
for p,bi in zip(ps,browser):
 i=p['id'];s=p['shipping'];v=p['planning'];j=p['jumia'];im=p['images'];n=notes.get(str(i));sections=p['description_sections'];words=len(re.findall(r"\b[\w’'-]+\b",' '.join(x['text'] for x in sections)))
 ck(p['author']=='DAVE ADEX' and p['category']=='kitchen items',f'Identity{i}');ck(p['source_url'] not in prior,f'EarlierKitchenExcluded{i}');ck(150<=words<=200 and words==p['description_word_count'],f'BuyerLength{i}');ck([x['heading'] for x in sections]==['What the Product is?','What are the clear benefits of the Product','Features of the Product'],f'ExactHeadings{i}');ck(not re.search('[\u4e00-\u9fff]',p['name']+p['brand']),f'English{i}');ck(p['brand']=='Other' or(i==151 and p['brand']=='hx'),f'BrandEvidence{i}')
 ck(j['access']['query']==p['name'],f'ExactNameSearch{i}');ck(j['access']['result']=='access-blocked',f'BlockedAccessRecorded{i}');ck(j['price_ngn'] is None or ('identical SKU not verified' in j['match'] and j['price_ngn']>0),f'ContextLabel{i}');ck(j['search_url'].startswith('https://www.jumia.com.ng/catalog/?q='),f'JumiaURL{i}')
 ck(len(im)==1 and im[0]['role']=='main',f'MainOnly{i}');ck(bi['id']==i and bi['offer']==p['source_url'] and 'Chromium DOM' in bi['method'],f'BrowserAssociation{i}');ck(bi['image']==im[0]['catalogue_dom_url'],f'ExactMainAsset{i}');ip=R/im[0]['local_path'];ck(ip.is_file(),f'Image{i}')
 if ip.exists():
  with Image.open(ip) as img:img.verify()
 if s['estimated_ngn'] is not None:
  ck(n is not None and n['weight_g'] is not None and not n.get('freight_hold'),f'PackingProvenance{i}');kg=max(n['weight_g']/1000,math.prod(n['packing_cm'])/6000 if n['packing_cm'] else 0);fee=round(kg*(cfg['air_usd_kg']*cfg['usd_ngn']+cfg['clearing_ngn_kg']),2);ck(abs(kg-s['chargeable_kg_scenario'])<1e-9 and abs(fee-s['estimated_ngn'])<.001,f'Freight{i}')
 else:ck(s['chargeable_kg_scenario'] is None,f'NoInventedKg{i}')
 sale=math.ceil(1.25*(max(5.2,p['source_price_cny'])*cfg['cny_ngn']+max(2000,s['estimated_ngn'] or 0))/100)*100;ck(sale==v['sale_ngn'] and v['compare_at_ngn']>sale,f'ProposedPrice{i}');ck(v['source_floor_cny']>=5.2 and v['shipping_floor_ngn']>=2000,f'Floors{i}')
cf=sum(p['shipping']['estimated_ngn'] is not None for p in ps);dim=sum(p['shipping']['supplier_package_cm'] is not None for p in ps);jc=sum(p['jumia']['price_ngn'] is not None for p in ps)
ck(cf==13 and dim==5 and jc==173,'EvidenceTotals');ck(ps[60]['source_price_cny']==18 and ps[60]['catalogue_price_cny']==3.6,'Selected304BasinNotCheaperNonmagnetic');ck(ps[160]['source_price_cny']==.01 and ps[160]['shipping']['estimated_ngn'] is None,'ClipTeaserNotFreightQuote');ck(ps[198]['source_price_cny']==.8 and 'single component' in ps[198]['jumia']['note'],'24PieceHeadlineNotConfirmedFullSetQuote');ck(all(ps[i-1]['shipping']['estimated_ngn'] is None for i in [31,41,51,81,121,131,161]),'RejectMissingOrConflictingPacking')
with (R/'data/products.csv').open(encoding='utf-8-sig') as f:ck(len(list(csv.DictReader(f)))==200,'CSV200')
protected=load(E/'preserved-sha256.json');changed=[]
for path,h in protected.items():
 f=R.parent/path
 if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:changed.append(path)
ck(not changed,'PriorFilesUnchanged');html=(R.parent/'kitchen-week2-product-listings.html').read_text();ck(html.lower().startswith('<!doctype html>'),'HTML5Doctype');ck('data:image/jpeg;base64,' in html,'EmbeddedMainImages');ck(not re.search(r'<(?:img|script|link)[^>]+(?:src|href)=[\"\"]https?://',html),'NoExternalRuntimeAssets')
report=dict(result='FAIL' if errors else 'PASS',products=200,days=5,per_day=40,families=20,main_images=200,supplier_detail_pages_readable=19,detail_attempts=20,blocked_detail_pages=1,conditional_freight=cf,dimensional_scenarios=dim,weight_only_lower_bounds=cf-dim,pending_freight=200-cf,indexed_observations=len(load(R/'data/market-observations.json')),priced_context_assignments=jc,pending_jumia_prices=200-jc,verified_identical_jumia=0,description_words_min=min(p['description_word_count'] for p in ps),description_words_max=max(p['description_word_count'] for p in ps),earlier_files_checked=len(protected),earlier_files_changed=changed,errors=errors,scope='Structural/image/arithmetic checks only;not product safety,stock,dispatch,affordability orlive-price verification')
(R/'data/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not errors
