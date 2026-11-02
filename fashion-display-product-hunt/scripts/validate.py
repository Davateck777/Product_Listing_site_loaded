#!/usr/bin/env python3
"""Validate the combined catalogue without rewriting any record."""
import json,re,csv,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];data=json.loads((R/'data/products.json').read_text());ps=data['products'];old=json.loads((R/'data/evidence/day1-original.json').read_text())
assert len(ps)==80 and [p['id'] for p in ps]==list(range(1,81))
assert ps[:40]==old['products'],'Original Day01 records changed'
assert len({p['source_url'] for p in ps})==80
assert [sum(p['day']==d for p in ps) for d in ['Day 01','Day 02']]==[40,40]
assert data['metadata']['product_count']==80
assert sum(p['group'] in ('earrings','necklaces','hair','bags','sunglasses','scarves') for p in ps)==54
expected=['What the Product is?','What are the clear benefits of the Product','Features of the Product']
for p in ps:
 assert p['author']=='DAVE ADEX' and p['category']=='Fashion&Display'
 assert [s['heading'] for s in p['description_sections']]==expected
 words=len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b",' '.join(s['text'] for s in p['description_sections'])))
 assert 150<=words<=200,(p['id'],words)
 assert len(p['images'])==1 and p['images'][0]['role']=='main'
 im=p['images'][0];assert im['status']=='downloaded' and (R/im['local_path']).read_bytes()[:2]==b'\xff\xd8'
 assert p['source_price_cny'] is None or p['source_price_cny']>0
for i,p in enumerate(ps[40:],1):
 assert p['day_product_number']==i
 q=p['day2_original_proposal'];assert q['sale_ngn']<q['compare_at_ngn']
assert len(list((R/'assets/images').glob('*')))==80
rows=list(csv.DictReader((R/'data/products.csv').open(encoding='utf-8-sig')));assert len(rows)==80
assert [r['Day'] for r in rows].count('Day 02')==40
text=(R.parent/'fashion-display-product-listings.html').read_text()
assert text.count('data:image/jpeg;base64,')==80
assert '<option value="Day 02">' in text and 'DAYS 01 + 02' in text
assert 'src="assets/' not in text and 'href="assets/' not in text
with zipfile.ZipFile(R.parent/'fashion-display-product-hunt.zip') as z:assert z.testzip() is None;assert len([p for p in z.namelist() if '/assets/images/' in p])==80
print('PASS: 80 unique offers;40 per day;Day01 records unchanged;54/26 split;80 main JPEGs;buyer copy150–200 words;CSV/offline HTML/ZIP valid.')
