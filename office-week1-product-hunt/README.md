# Office accessories — Week 1
**Author: DAVE ADEX · Checked 04 November 2026 · 250 offers · 5 days × 50**

## Open the catalogue
- `../office-week1-product-listings.html` — main deliverable. Standalone/offline HTML with all250 main images embedded. No network dependency for viewing.
- `index.html` — editable modular version; keep this folder and its local assets together. Open locally in a browser. The in-app isolated file viewer may not resolve separate local files; use the standalone page there.
- `data/products.csv` —250 rows, original source observations, selected options, freight basis, Jumia whole-pack context and all three buyer-copy sections.
- `data/products.json` — assembled records and metadata.

**No ZIP is created.** Earlier catalogue files are not overwritten.

## Five stable daily grids
| Day | Product IDs | Families |
|---|---|---|
|01|1–50|Ballpoint pens,gel pens,highlighters,whiteboard markers,pencils|
|02|51–100|Erasers,rulers,sharpeners,notebooks,notes/tabs|
|03|101–150|Staplers,staples,paper clips,binder clips,scissors|
|04|151–200|Tape dispensers,glue sticks,folders,clipboards,file racks|
|05|201–250|Pen holders,small organisers,mouse pads,laptop supports,cable clips|

Ten distinct1688 offers per family; fifty per day. English names are editorial translations. A supported original English brand is retained; otherwise`Other`. This does not certify authenticity.

## Team editing map
| Owner | Source file | Responsibility |
|---|---|---|
|Curation|`data/evidence/selected.json`|Stable IDs,names,original brand field,source URL,starting price,day/group|
|Supplier research|`data/evidence/detail-notes.json`|Selected variant,facts,weight/dimensions,carton allocation,price corrections and cautions|
|Buyer copy|`data/evidence/guides.json`|Three consumer-facing paragraphs per family; assembler inserts each name and observed facts|
|Market research|`data/market-observations.json`|Indexed Jumia price,title,URL,assigned IDs,whole-pack description and limitations|
|Images|`data/image-manifest.json`, `assets/images/`|Exactly one main image per product; original URL and browser provenance retained|
|Freight/FX|`data/settings.json`|Published freight reference and dated conversion inputs|
|Design|`template.html`, `assets/css/styles.css`|Layout,disclosures,labels and responsive visual system|
|Interface|`assets/js/app.js`|Filters,calculator,viewer,CSV export; no external library|
|Build/QA|`scripts/`|Assembly,offline build,structural validation and browser regression|

Do not edit generated`assets/js/products.js`,`data/products.json`,`index.html`or the standalone HTML directly: the next build replaces them. Edit the inputs above instead. Do not propagate a representative weight to nine sibling products. Recheck price unit,MOQ,pack count and source variant when changing a record.

Buyer descriptions contain161–185 words and use exactly:
1. **What the Product is?**
2. **What are the clear benefits of the Product**
3. **Features of the Product**

Copy teaches buyers what to choose and check; it does not give resale instructions. Title-based attributes are supplier claims,not independent tests.

## Rebuild — portable standard-library pipeline
From this folder:
```sh
python scripts/assemble.py
python scripts/build.py
python scripts/validate.py
```
Run from another directory with full script paths if preferred. All paths resolve relative to the project folder. Assembly deliberately rejects descriptions outside150–200 words. Build emits both HTML versions,the generated JavaScript mirror and CSV.

Optional UI regression requires Node.js,Playwright and Chromium:
```sh
npm install playwright
npx playwright install --with-deps chromium
node scripts/browser-qa.cjs
```
The browser test blocks external HTTP requests,loads all250 embedded images,checks fifty cards on each day,all250 view,search,exact headings,freight/pack filters,FX and floor arithmetic,immutable observations,CSV export,image viewer/focus,mobile overflow and local modular output. Browser tests may write screenshots under`../research/office-week1/`if that directory exists. They do not certify product quality or current supplier information.

`data/validation.json`and`data/browser-qa.json`record the latest PASS results. Preservation validation compares twelve earlier standalone/catalogue data files against the SHA256 baseline in`data/evidence/preserved-catalogues-sha256.json`. Moving this project alone to another computer removes those earlier files; the preservation part then intentionally fails until the original siblings are supplied or the preservation check is consciously adapted. Assembly and build themselves remain portable.

## Evidence boundaries — read before using prices
### Supplier and images
250 catalogue offers and exact offer-ID/main-image associations were browser inspected.244 associations used live catalogues;six used saved public catalogue HTML when live rankings changed.25 representative rendered supplier detail pages were inspected; the other225 do not have selected-option technical sheets. The image manifest retains sourceCDN URLs and browser provenance. Local JPEGs are size-optimised for an offline catalogue; image permission and exact selected-colour matching are not established. No support images are included. Supplier photos may themselves show multiple items or props.

Original offer553339987300 was excluded because its detail page explicitly stated no ready stock and gave contradictory mass. Product91 now uses offer858408089598. The exclusion is retained in`data/evidence/excluded-offers.json`.

Catalogue prices are starting observations,not final quotations. They can refer to a cheaper option,accessory or pack. The representative scissors(ID141)uses an explicit selected option¥1.20 while preserving the original starting observation separately. Neither this correction nor any brand/dispatch claim guarantees stock,authenticity or order acceptance.

### Freight:19 conditional /231 pending
-5 selected-unit dimensional scenarios:IDs31,121,141,221,241.
-1 carton scenario:ID151 uses55×34×45.5cm,20kg gross,80units. Volumetric mass=14.1808kg; actual carton mass dominates,so allocation=20/80=0.25kg per unit.
-13 weight-only **lower bounds**,not full protective-pack quotes.
-6 inspected representatives lack credible variant-specific packing; the other225 have no selected packing data. These231 amounts remain pending,not invented.

Reference normal-goods rate:Dechaser China–Nigeria guide,20kg+ consolidated Lagos-doorUSD14.88/kg+₦1,500/kg clearing. Smaller tiers differ. Scenario uses max(actual kg,volume in cm³/6000). Confirm divisor,carrier acceptance,current quote,rounding/minimums,additional export packaging and fees. Duties/VAT,insurance,China transport and onward delivery beyond Lagos are excluded/unconfirmed. Ink/glue acceptance and safety documentation may change the applicable service/rate. Published7–10working-day normal transit is not a guaranteed dispatch or delivery date.

FX:03 November2026 reference USD/NGN1344.57×CNY/USD0.15004=CNY/NGN201.7392828. Checked04 November2026,not live bank/payment rates. URLs are in`settings.json`.

### Jumia:context,not identical-SKU comparison
All250 exact English-name direct requests were blocked; their queries,URLs and statuses are retained in`data/evidence/jumia-access.json`.48 indexed observations are assigned across250 records. **Zero identical-SKU matches are verified.** Whole-pack amounts are not divided into per-piece prices. Some contexts are broad functional comparisons,unknown quantities or starting ranges; read each note. Neither live stock/checkout nor Jumia delivery fees are verified. Do not present these as direct savings comparisons.

### Editable pricing proposals
Default source floor≥¥5.20;shipping floor≥₦2,000. Floors never replace observed source/freight fields.

`proposed sale=ceil_to_₦100(1.25×[max(observedCNY,sourceFloor)×CNYFX+max(conditionalFreight,shippingFloor)])`

Missing freight uses the floor only as an unverified placeholder. Compare-at proposal is rounded up from a target reduction of12% below₦5,000,10% below₦15,000,otherwise8%;displayed reduction reflects rounding. These are not historical prices,live offers,landed costs or profit guarantees. Fees and source pack quantities remain unresolved. Cheap stationery can be cheaper locally in multi-packs; the floor-based scenario is not proof of affordability. Do not cap proposals against non-identical Jumia prices to fabricate savings.

## Published references
-https://dechaser.com/china-to-nigeria-shipping/
-https://dechaser.com/shipping-from-china-to-nigeria/
-https://www.forbes.com/advisor/money-transfer/currency-converter/usd-ngn/
-https://www.forbes.com/advisor/money-transfer/currency-converter/cny-usd/
-Product-specific1688,Jumia evidence and exact-name search links are in each record.
