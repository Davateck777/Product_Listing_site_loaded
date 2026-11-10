"""EXPLICIT-REQUEST PACKAGING MODULE — run only when a ZIP is requested.
The ZIP's root index.html is the complete offline catalogue,not a missing-file redirect.
All project files andthe original standalone filename are also retained.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json
R=Path(__file__).resolve().parents[1];root=R.parent
html=root/'interiors-week2-product-listings.html';dest=root/'interiors-week2-catalogue.zip'
start='''# Interior Designs — Week 2 / DAVE ADEX

1. Extract the whole ZIP into a folder.
2. Open index.html in that folder. It is the complete offline 200-product catalogue.
3. The original interiors-week2-product-listings.html also opens the complete catalogue.
4. interiors-week2-product-hunt/index.html is an additional project entry page.

The project folder includes all 200 required main images, CSS, JavaScript, template,
CSV/JSON product data, evidence, settings, README, rebuild scripts and validation reports.
No web server, dependency install or internet connection is needed to view the catalogue.
Python standard-library rebuild instructions and optional browser QA are in the project README.
Research limitations and provisional freight/price assumptions remain disclosed in the catalogue.
'''
files=[html]+sorted(p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
with ZipFile(dest,'w',ZIP_DEFLATED,compresslevel=9) as z:
 z.writestr('index.html',html.read_bytes())
 z.writestr('START_HERE.md',start)
 for p in files:z.write(p,p.relative_to(root))
with ZipFile(dest) as z:
 assert z.testzip() is None
 names=set(z.namelist())
 assert all(x in names for x in ['index.html','START_HERE.md',R.name+'/index.html',R.name+'/data/products.json',R.name+'/assets/js/app.js',R.name+'/assets/css/styles.css'])
 products=json.loads((R/'data/products.json').read_text())
 for r in products:assert R.name+'/'+r['image_record']['local'] in names
 assert z.read('index.html')==html.read_bytes()
 print(f'PASS: {len(names)} files;200 required main assets;complete root index.html;ZIP CRC integrity. {dest.stat().st_size:,} bytes')
