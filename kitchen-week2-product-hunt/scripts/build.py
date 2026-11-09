"""BUILD: generate modular HTML, self-contained offline HTML, JavaScript data mirror and CSV.
Standard library only. Run from any directory. Never writes an earlier catalogue filename.
"""
import json,base64,csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'data/products.json').read_text());template=(R/'template.html').read_text()
def js(d):return '/* Generated; edit JSON inputs, not this mirror. */\nwindow.CATALOG='+json.dumps(d,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+';'
# Modular output: all references stay local after extracting the complete project folder.
(R/'assets/js/products.js').write_text(js(data))
mod=template.replace('<!--STYLE-->','<link rel="stylesheet" href="assets/css/styles.css">').replace('<!--DATA-->','<script src="assets/js/products.js"></script>').replace('<!--APP-->','<script src="assets/js/app.js"></script>')
(R/'index.html').write_text(mod)
# Standalone output: encode exactly one main image per product for network-free viewing.
inline=json.loads(json.dumps(data))
for p in inline['products']:
 im=p['images'][0];im['local_path']='data:image/jpeg;base64,'+base64.b64encode((R/im['local_path']).read_bytes()).decode()
standalone=template.replace('<!--STYLE-->','<style>'+(R/'assets/css/styles.css').read_text()+'</style>').replace('<!--DATA-->','<script>'+js(inline)+'</script>').replace('<!--APP-->','<script>'+(R/'assets/js/app.js').read_text()+'</script>')
(R.parent/'kitchen-week2-product-listings.html').write_text(standalone)
# Fixed CSV: quote observations, planning proposals and competitor pack counts separately.
fields=['id','day','daily_number','author','name','brand','category','kind','source_cny','source_price_status','catalogue_starting_cny','selected_variant','source_url','weight_g','packing_cm','chargeable_kg','approx_shipping_ngn','shipping_caveat','dispatch_claim','source_floor_cny','shipping_floor_ngn','proposed_sale_ngn','proposed_compare_at_ngn','planned_discount_percent','jumia_context_ngn','jumia_pack_quantity','jumia_context_title','jumia_url','jumia_name_search','jumia_match_note','main_image_url','description_word_count','what_product_is','clear_benefits','features']
extra=['carton_cm','carton_gross_weight_g','carton_units','freight_calculation_basis','jumia_pack_description']
fields+=extra
with (R/'data/products.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for p in data['products']:
  s=p['shipping'];j=p['jumia'];v=p['planning'];row=dict(zip(fields,[p['id'],p['day'],p['day_product_number'],p['author'],p['name'],p['brand'],p['category'],p['kind'],p['source_price_cny'],p['source_price_note'],p['catalogue_price_cny'],p['selected_variant'],p['source_url'],s['supplier_weight_g'],s['supplier_package_cm'],s['chargeable_kg_scenario'],s['estimated_ngn'],s['conditions'],p['dispatch_claim'],5.2,2000,v['sale_ngn'],v['compare_at_ngn'],v['discount_percent'],j['price_ngn'],j['pack_quantity'],j['title'],j['source_url'],j['search_url'],j['note'],p['images'][0]['url'],p['description_word_count'],*[x['text'] for x in p['description_sections']]]));row.update(dict(zip(extra,[s['supplier_carton_cm'],s['supplier_carton_weight_g'],s['supplier_carton_quantity'],s['calculation_basis'],j['pack_description']])));w.writerow(row)
print('Built new modular page, standalone HTML and200-row CSV; earlier catalogues untouched.')
