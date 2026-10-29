#!/usr/bin/env python3
"""Fail closed on record count, duplicate offers, buyer-copy length or missing assets."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/products.json').read_text());ps=d['products']
assert len(ps)==40 and sorted(p['id'] for p in ps)==list(range(1,41))
assert len({p['source_url'] for p in ps})==40
assert all(p['author']=='DAVE ADEX' and p['category']=='Fashion&Display' for p in ps)
assert sum(p['group'] in ('earrings','necklaces','hair','bags','sunglasses','scarves') for p in ps)==24
expected=['What the Product is?','What are the clear benefits of the Product','Features of the Product']
for p in ps:
 assert [s['heading'] for s in p['description_sections']]==expected,p['id']
 words=len(re.findall(r"\b[\w’-]+\b",' '.join(s['text'] for s in p['description_sections'])))
 assert 150<=words<=200 and words==p['description_word_count'],(p['id'],words)
 assert p['images'][0]['role']=='main'
 assert all(im['status']=='downloaded' and (ROOT/im['local_path']).is_file() for im in p['images']),p['id']
 assert len(p['images'])==1 and 'MAIN IMAGE ONLY' in p['image_archive_status']
 assert p['jumia']['price_ngn'] is None or p['jumia']['source_url'].startswith('https://www.jumia.com.ng/')
assert ps[32]['source_url'].endswith('535336707513.html')
print('PASS: 40 unique records; 24/16 split; all copy 150–200 words; 40 main-image assets present; main-only policy enforced.')
print('Jumia priced comparables:',sum(p['jumia']['price_ngn'] is not None for p in ps))
print('Conditional weight-only allocations:',sum(p['shipping']['estimated_ngn'] is not None for p in ps))
