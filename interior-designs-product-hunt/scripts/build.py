"""Rebuild offline modular page, single-file HTML and CSV from the JSON source of truth.
Run from any working directory: python path/to/scripts/build.py
Standard library only. Does not touch any fashion/electronics deliverable.
"""
import base64,csv,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
products=json.loads((R/'data/products.json').read_text());settings=json.loads((R/'data/settings.json').read_text())
def js(data):return 'window.INTERIORS='+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';'
data={'products':products,'settings':settings};(R/'data/products.js').write_text(js(data))
template=(R/'template.html').read_text();css=(R/'assets/css/style.css').read_text();app=(R/'assets/js/app.js').read_text()
mod=template.replace('<!--STYLE-->','<link rel="stylesheet" href="assets/css/style.css">').replace('<!--DATA-->','<script src="data/products.js"></script>').replace('<!--APP-->','<script src="assets/js/app.js"></script>');(R/'index.html').write_text(mod)
inline=json.loads(json.dumps(data))
for p in inline['products']:
 path=R/p['main_image']['local'];p['main_image']['local']='data:image/jpeg;base64,'+base64.b64encode(path.read_bytes()).decode()
standalone=template.replace('<!--STYLE-->','<style>'+css+'</style>').replace('<!--DATA-->','<script>'+js(inline)+'</script>').replace('<!--APP-->','<script>'+app+'</script>')
(R.parent/'interior-designs-product-listings.html').write_text(standalone)
fields=['id','day','daily_number','name','brand','category','url','selected_variant','catalogue_price_cny','source_price_cny','price_basis','weight_g','packing_cm','shipping_estimate_ngn','shipping_status','planning_source_cny','planning_shipping_ngn','proposed_sale_ngn','proposed_compare_at_ngn','proposed_discount_percent','market_review','detail_word_count']
with (R/'data/products.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=fields+['supplier_price_usd','jumia_comparable_ngn','jumia_comparable_url','jumia_match_note','jumia_name_search_url','what_product_is','clear_benefits','features'],extrasaction='ignore');w.writeheader()
 for p in products:
  m=p['market_comparison'] or {};n=p['supplier_detail'] or {};w.writerow(dict(p,supplier_price_usd=n.get('selected_price_usd'),jumia_comparable_ngn=m.get('price_ngn'),jumia_comparable_url=m.get('url'),jumia_match_note=m.get('note','Pending'),jumia_name_search_url=p['jumia_name_search']['url'],what_product_is=p['details'][0]['text'],clear_benefits=p['details'][1]['text'],features=p['details'][2]['text']))
print('Built modular page, standalone HTML and200-row CSV.')
