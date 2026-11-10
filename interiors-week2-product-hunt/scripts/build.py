"""BUILD MODULE — embed exactly one main image per product for offline standalone HTML.
No network fetches;no support galleries;never makes a ZIP orchanges old catalogues.
"""
from pathlib import Path
import json,base64
R=Path(__file__).resolve().parents[1];rows=json.loads((R/'data/products.json').read_text())
for r in rows:r['image_data']='data:image/jpeg;base64,'+base64.b64encode((R/r['image_record']['local']).read_bytes()).decode()
s=(R/'templates/catalogue.html').read_text()
for key,value in [('CSS',(R/'assets/css/styles.css').read_text()),('APP',(R/'assets/js/app.js').read_text()),('DATA',json.dumps(rows,ensure_ascii=False).replace('</','<\\/'))]:s=s.replace('/*__'+key+'__*/',value)
f=R.parent/'interiors-week2-product-listings.html';f.write_text(s);print(f.name,len(s.encode()),'bytes')
