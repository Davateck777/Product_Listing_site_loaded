"""Structural QA, not a claim that pending supplier facts were verified."""
import json,re,math
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1];p=json.loads((R/'data/products.json').read_text());errors=[]
def check(b,s):
 if not b:errors.append(s)
check(len(p)==200,'Count200');check(len({x['url'] for x in p})==200,'Uniqueoffers');check(Counter(x['day'] for x in p)=={1:40,2:40,3:40,4:40,5:40},'Five40grids')
for x in p:
 id=x['id'];check(re.fullmatch(r'https://detail\.1688\.com/offer/\d+\.html',x['url']) is not None,f'Canonicalurl{id}')
 check(150<=len(re.findall(r"\b[\w’'-]+\b",' '.join(d['text'] for d in x['details'])))<=200,f'Copylength{id}')
 check([d['heading'] for d in x['details']]==['What the Product is?','What are the clear benefits of the Product','Features of the Product'],f'Headings{id}')
 check(x['brand']=='Other' or re.fullmatch('[A-Za-z0-9 .&-]+',x['brand']) is not None,f'Englishbrand{id}')
 check((R/x['main_image']['local']).is_file(),f'Image{id}');check(x['main_image']['role']=='main',f'Mainonly{id}')
 check(x['planning_source_cny']>=5.2 and x['planning_shipping_ngn']>=2000,f'Floors{id}');check(x['proposed_compare_at_ngn']>x['proposed_sale_ngn'],f'Compareat{id}')
 if x['shipping_estimate_ngn'] is not None:check(bool(x['weight_g']) and bool(x['supplier_detail']),f'Freightevidence{id}')
 else:check(x['planning_shipping_ngn']==2000,f'Pendingplaceholder{id}')
cfg=json.loads((R/'data/settings.json').read_text())
check(sum(x['shipping_estimate_ngn'] is not None for x in p)==15,'15 supported packing scenarios')
check(sum(bool(x['market_comparison']) for x in p)==198,'198 priced non-identical contexts')
for x in p:
 check(x['category']=='Electronics','Electronics category')
 check(x['jumia_name_search']['query']==x['name'],f"Updated name-search{x['id']}")
 if x['shipping_estimate_ngn'] is not None:
  rate=cfg['battery_usd_kg'] if x['cargo_class']=='battery' else cfg['air_usd_kg']
  expected=round(x['chargeable_kg']*(rate*cfg['usd_ngn']+cfg['clearing_ngn_kg']),2)
  check(abs(expected-x['shipping_estimate_ngn'])<.011,f"Route-specific freight{x['id']}")
check(len({x['main_image']['catalogue_dom_url'] for x in p})==200,'200 distinct main image URLs')
report=dict(result='PASS' if not errors else 'FAIL',products=len(p),days=dict(Counter(x['day'] for x in p)),main_images=len(list((R/'assets/images').glob('*-main.jpg'))),supplier_detail_pages=sum(bool(x["supplier_detail"]) for x in p),conditional_freight=sum(x["shipping_estimate_ngn"] is not None for x in p),pending_freight=sum(x["shipping_estimate_ngn"] is None for x in p),broad_jumia_context=sum(bool(x["market_comparison"]) for x in p),pending_jumia=sum(not x["market_comparison"] for x in p),identical_jumia_matches=0,description_words_min=min(x['detail_word_count'] for x in p),description_words_max=max(x['detail_word_count'] for x in p),errors=errors)
(R/'data/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));assert not errors
