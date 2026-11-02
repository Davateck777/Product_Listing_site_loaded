"""STRUCTURAL QA: passing validates files/arithmetic, NOT procurement or product safety."""
import json,re,math,csv
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1];d=json.loads((R/'data/products.json').read_text());p=d['products'];cfg=d['metadata']['settings'];errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
check(len(p)==200,'200records');check(len({x['source_url'] for x in p})==200,'200uniqueoffers');check(Counter(x['day_number'] for x in p)=={1:40,2:40,3:40,4:40,5:40},'5x40');check(Counter(x['kind'] for x in p)=={'wearable':150,'display':50},'150wearables50display')
# Per-product invariants: canonical provenance, buyer length, sole main photo and floors.
for x in p:
 id=x['id'];s=x['shipping'];v=x['planning'];j=x['jumia'];copy=' '.join(t['text'] for t in x['description_sections']);n=len(re.findall(r"\b[\w’'-]+\b",copy))
 check(x['category']=='Fashion&Display' and x['author']=='DAVE ADEX',f'Identity{id}');check(150<=n<=200 and n==x['description_word_count'],f'Buyerlength{id}');check([a['heading'] for a in x['description_sections']]==['What the Product is?','What are the clear benefits of the Product','Features of the Product'],f'Headings{id}')
 check(x['brand']=='Other' or re.fullmatch('[A-Za-z0-9 .,&-]+',x['brand']) is not None,f'Englishbrand{id}');check(re.fullmatch(r'https://detail\.1688\.com/offer/\d+\.html',x['source_url']) is not None,f'Canonicalurl{id}');check(len(x['images'])==1 and x['images'][0]['role']=='main',f'Mainonly{id}');check((R/x['images'][0]['local_path']).is_file(),f'Image{id}')
 check(v['source_floor_cny']>=5.2 and v['shipping_floor_ngn']>=2000,f'Floors{id}');check(v['compare_at_ngn']>v['sale_ngn'],f'Compare{id}');check(j['access']['query']==x['name'],f'Namesearch{id}');check(j['source_url'].startswith('https://www.jumia.com.ng/') and j['price_ngn']>0,f'Pricedcontext{id}')
 if s['estimated_ngn'] is not None:
  check(bool(x['supplier_detail']) and s['supplier_weight_g']>0,f'Freightevidence{id}');expected=round(s['chargeable_kg_scenario']*(cfg['air_usd_kg']*cfg['usd_ngn']+cfg['clearing_ngn_kg']),2);check(abs(expected-s['estimated_ngn'])<.011,f'Freightarithmetic{id}')
 cost=max(5.2,x['source_price_cny'])*cfg['cny_ngn']+max(2000,s['estimated_ngn'] or 0);check(math.ceil(cost*1.25/100)*100==v['sale_ngn'],f'Pricing{id}')
check(len(list((R/'assets/images').glob('*-main.jpg')))==200,'200mainfiles');check(len({x['images'][0]['catalogue_dom_url'] for x in p})==200,'200distinctimageURLs')
with (R/'data/products.csv').open(encoding='utf-8-sig') as f:check(len(list(csv.DictReader(f)))==200,'CSV200rows')
excluded=json.loads((R/'data/evidence/excluded-earlier-fashion-offers.json').read_text())['urls'];check(not set(excluded).intersection(x['source_url'] for x in p),'Portableearlier80exclusions')
old=R.parent/'fashion-display-product-hunt/data/products.json'
if old.exists():
 prior={x['source_url'] for x in json.loads(old.read_text())['products']};check(not prior.intersection(x['source_url'] for x in p),'NoearlierFashionoffersreused')
report=dict(result='PASS' if not errors else 'FAIL',products=200,days=dict(Counter(x['day_number'] for x in p)),wearables=150,display=50,main_images=200,supplier_detail_pages=20,conditional_freight=sum(x['shipping']['estimated_ngn']is not None for x in p),weight_only_lower_bounds=sum(x['shipping']['estimated_ngn']is not None and not x['shipping']['supplier_package_cm'] for x in p),pending_freight=sum(x['shipping']['estimated_ngn']is None for x in p),priced_jumia_context=sum(x['jumia']['price_ngn']is not None for x in p),verified_identical_jumia=0,description_words_min=min(x['description_word_count'] for x in p),description_words_max=max(x['description_word_count'] for x in p),errors=errors)
(R/'data/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not errors
