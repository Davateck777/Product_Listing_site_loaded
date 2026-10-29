#!/usr/bin/env python3
"""Rebuild modular HTML, offline HTML and CSV from data/products.json.
Run from any directory: python scripts/build.py. Python standard library only.
The JSON is authoritative. Image filenames remain stable across edits.
"""
from pathlib import Path
import json,base64,csv,io,zipfile
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/products.json').read_text())
# Keep the JavaScript data mirror generated, never hand-edited.
serialized=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
(ROOT/'assets/js/products.js').write_text('/* Generated from data/products.json by scripts/build.py. */\nwindow.CATALOG='+serialized+';',encoding='utf-8')
body='''<header><div class="mast"><b>DAVE ADEX / PRODUCT RESEARCH</b><span class="stamp">DAY 01 · 29 OCT 2026</span></div><div class="hero-bottom"><div><h1>Fashion.<br>Form. Everyday.</h1><p>A considered selection of wearable accessories, jewellery displays and everyday organisers. Forty supplier-led product stories, written for buyers.</p></div><div class="numbers"><div><strong>40</strong><small>Products</small></div><div><strong>24</strong><small>Wearables</small></div><div><strong>16</strong><small>Display & storage</small></div></div></div></header>
<main><aside class="notice"><strong>Research draft · evidence before estimates</strong>1688 browser inspection reached login or verification screens. Facts and image URLs use readable public-page extracts. Only the main product image is included for each item, per your session preference. Jumia figures are labelled comparables, not identical-SKU prices. Shipping is a conditional estimate using a published rate and assumed FX, not a carrier quote.</aside>
<section class="controls" aria-label="Batch planning assumptions"><div class="control-head"><h2>Batch planning desk</h2><span class="badge">Overrides do not rewrite source evidence</span></div><div class="fields"><label>Source floor / CNY<input id="sourceFloor" type="number" min="5.2" step="0.1" value="5.2"></label><label>Shipping floor / NGN<input id="shipFloor" type="number" min="2000" step="100" value="2000"></label><label>Assumed CNY → NGN<input id="cnyFx" type="number" min="1" step="1" value="210"></label><label>Assumed USD → NGN<input id="usdFx" type="number" min="1" step="1" value="1500"></label></div><p class="fine">FX values are editable assumptions, not live rates. Planning price = 1.25 × [max(source, source floor) × CNY FX + max(weight-only shipping allocation, shipping floor)], rounded up to ₦100. Missing weights use the floor as an unverified placeholder. Compare-at = planning price ÷ 0.90, rounded up: a proposed reference, not an actual former price. Do not advertise a discount without a genuine lawful basis. Market affordability and margin are not guaranteed.</p></section>
<section class="toolbar" aria-label="Filter products"><input id="search" type="search" placeholder="Search product, brand, feature or number…" aria-label="Search catalogue"><select id="group" aria-label="Product type"></select><select id="status" aria-label="Research status"><option value="">All evidence statuses</option><option value="jumia">Jumia price pending</option><option value="shipping">Weight estimate pending</option></select><button id="expand" type="button">Expand buyer copy</button><span id="resultCount" class="result-count" aria-live="polite"></span></section><section id="catalog" class="grid" aria-label="Day 01 product grid"></section><noscript>JavaScript is needed for the interactive grid. The supplied CSV and JSON contain all 40 product records and descriptions.</noscript>
<footer><div><b>DAVE ADEX</b><br>Day 01 · Fashion&amp;Display · 40 products</div><div>Research date: 29 October 2026<br>Freight source dated 20 January 2026 · Re-quote before ordering</div></footer></main>
<div id="modal" class="modal" role="dialog" aria-modal="true" aria-label="Supplier product image" hidden><button id="closeModal" aria-label="Close image viewer">×</button><img id="modalImage" alt=""><p id="modalCaption"></p></div>'''
head='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="author" content="DAVE ADEX"><title>Fashion &amp; Display — Day 01 / DAVE ADEX</title>'
modular=head+'<link rel="stylesheet" href="assets/css/styles.css"></head><body>'+body+'<script src="assets/js/products.js"></script><script src="assets/js/app.js"></script></body></html>'
(ROOT/'index.html').write_text(modular,encoding='utf-8')
# Embed each image once in the standalone file; only main images are included in the offline grid.
offline=json.loads(json.dumps(data))
for p in offline['products']:
 for img in p['images']:
  if img.get('local_path'):
   img['local_path']='data:image/jpeg;base64,'+base64.b64encode((ROOT/img['local_path']).read_bytes()).decode()
css=(ROOT/'assets/css/styles.css').read_text();js=(ROOT/'assets/js/app.js').read_text()
standalone=head+'<style>'+css+'</style></head><body>'+body+'<script>window.CATALOG='+json.dumps(offline,ensure_ascii=False).replace('</','<\\/')+';</script><script>'+js+'</script></body></html>'
(ROOT.parent/'fashion-display-product-listings.html').write_text(standalone,encoding='utf-8')
# Excel-friendly UTF-8 BOM, explicit quote/assumption/proposal separation, full buyer copy.
fields=['ID','Day','Author','EnglishProductName','Brand','Category','SourcePriceCNY','SourcePriceStatus','SourceURL','PriceOnJumiaNGN','JumiaMatch','JumiaTitle','JumiaURL','JumiaNote','JumiaSearchURL','SupplierWeightG','SupplierPackageCM','ApproxShippingNGN','ShippingStatus','RateSource','FXAssumptionUSDNGN','FXAssumptionCNYNGN','ProposedSourceFloorCNY','ProposedShippingFloorNGN','ProposedSaleNGN','ProposedCompareAtNGN','ProposedDiscountPercent','ProductDetails','DescriptionWordCount','SupplierCaveat','MainImageURL','ImageArchiveStatus','BrowserStatus']
with (ROOT/'data/products.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for p in data['products']:
  j=p['jumia'];s=p['shipping'];ship=s['estimated_ngn'];cost=max(5.2,p['source_price_cny'])*210+max(2000,ship or 0);import math
  sale=math.ceil(cost*1.25/100)*100;compare=math.ceil(sale/.9/100)*100
  w.writerow(dict(zip(fields,[p['id'],p['day'],p['author'],p['name'],p['brand'],p['category'],p['source_price_cny'],p['source_price_note'],p['source_url'],j['price_ngn'],j['match'],j.get('title',''),j.get('source_url',''),j['note'],j['search_url'],s['supplier_weight_g'],s['supplier_package_cm'],ship,s['status']+'; '+s['conditions'],s['rate_source'],1500,210,5.2,2000,sale,compare,round((1-sale/compare)*100),'\n\n'.join(x['heading']+'\n'+x['text'] for x in p['description_sections']),p['description_word_count'],p['supplier_caveat'],p['images'][0]['url'],p['image_archive_status'],p['browser_status']])))
# A reproducible handoff archive containing the modular project (not a redundant embedded HTML).
archive=ROOT.parent/'fashion-display-product-hunt.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for path in sorted(ROOT.rglob('*')):
  if path.is_file() and '__pycache__' not in path.parts:z.write(path,path.relative_to(ROOT.parent))
print('Built:',ROOT/'index.html',ROOT.parent/'fashion-display-product-listings.html',ROOT/'data/products.csv',archive,sep='\n')
