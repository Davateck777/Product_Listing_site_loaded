"""TEAM PACKAGE: archive ONLY this project and its generated standalone page.
Requires both QA reports PASS. Existing ZIPs are preserved by selecting a version suffix.
"""
import json,hashlib,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1];standalone=R.parent/'fashion-week1-product-listings.html'
for f in ['data/validation.json','data/browser-qa.json']:
 assert json.loads((R/f).read_text())['result']=='PASS','Run validation/browser QA first: '+f
assert standalone.is_file(),'Run build.py first'
# Integrity map has no recursive self-hash. Generated dependencies/caches are never archived.
def allowed(p):return p.is_file() and not any(s in {'.git','node_modules','__pycache__','.cache','.pytest_cache'} for s in p.parts) and p.suffix not in {'.pyc','.zip'}
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(R.rglob('*')) if allowed(p) and p.name!='file-integrity.json'}
manifest['../'+standalone.name]=hashlib.sha256(standalone.read_bytes()).hexdigest();(R/'data/file-integrity.json').write_text(json.dumps(manifest,indent=2))
base=R.parent/'fashion-week1-DAVE-ADEX-team-package.zip';target=base;n=2
while target.exists():target=base.with_name(base.stem+'-v'+str(n)+'.zip');n+=1
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 z.write(standalone,standalone.name)
 z.writestr('START-HERE.txt','DAVE ADEX — NEW Fashion&Display Week1\n\nOpen fashion-week1-product-listings.html for the self-contained catalogue.\nExtract everything before opening fashion-week1-product-hunt/index.html.\nTeam handoff and evidence limitations: fashion-week1-product-hunt/README.md.\n200offers,5days×40;16conditionalfreight/184pending;200non-identicalJumiacontexts.\nPrior catalogues and ZIPs are preserved. Retain this ZIP until the user requests deletion.\n')
 for p in sorted(R.rglob('*')):
  if allowed(p):z.write(p,str(Path(R.name)/p.relative_to(R)))
with zipfile.ZipFile(target) as z:
 assert z.testzip() is None;entries=len(z.namelist());assert sum('/assets/images/' in s for s in z.namelist())==200
print(json.dumps(dict(zip=str(target),bytes=target.stat().st_size,entries=entries,testzip='PASS',sha256=hashlib.sha256(target.read_bytes()).hexdigest()),indent=2))
