# Kitchen Items — Week 2
**Author: DAVE ADEX · Research session: 27 October 2026**

## Deliverables
- `../kitchen-week2-product-listings.html`: self-contained offline HTML; all 200 main JPEGs, application, data and styles embedded. Open/download this for ordinary use.
- `index.html`: modular offline edition; retain its adjacent `assets` folder.
- `data/products.csv`: full 200-row spreadsheet export, including buyer copy, original observations, packing caveats, source links and proposal fields.
- `data/products.json`: assembled records and metadata.

200 distinct1688offer URLs; 20 families×10; five daily grids×40. Earlier Kitchen offer URLs are excluded. Related functions may recur. Every record has an English name, kitchen items category and one main image. Original Latin-script brand **hx** is supported for#151; other brands are **Other**, not invented translations. Buyer descriptions are158–189words, with the three requested exact headings.

## Research limits—read before procurement
- 200 public supplier catalogue title/price observations. Chromium inspected each saved page's actual DOM association between offer link and main img;200 genuine supplier main images were downloaded. This does **not** establish selected colour/pack, image permissions, or first live detail-gallery position. No support-image galleries, stock-photo substitutions or generated product photos.
- 20 representative detail attempts:19 readable;#41 captcha-blocked. The other181records do not have readable selected-option technical sheets. Findings and failed access are logged separately.
- **13 conditional freight allocations**:five use supplier piece dimensions;eight are weight-only **lower bounds**. **187 freight amounts remain pending**. No unknown packing mass, carton allocation, sibling weight or Jumia weight is invented.
- All200exact English-name Jumia direct requests returned access-blocked.20family query themes plus four refinement queries supplied30differentiated indexed observations, including an unassigned wood-pin alternative.173records are assigned **non-identical family/product contexts**;27have no assigned price. **Zero identical live-checkout matches verified**. Reusing a family reference is not independent research for each SKU. Whole-pack prices remain whole-pack prices;contents, materials, mechanism and quantity differences are explicit. No checkout-live/identical-price claim.
- Starting1688prices may quote one component,not a pictured set. The selected20cm304-labelled basin is¥18,not the cheaper12cm non-magnetic¥3.60variant.#199's¥0.80observation does not establish a24-piece full-set price.#161's¥0.01teaser is unconfirmed. Food-contact, heat ratings, authenticity, dispatch and stock are not certified.
- Dispatch is not transit. Some48hpromises cover only2items or have poor historical collection metrics;one rolling-pin page allows10days for3+items. No blanket quick-dispatch promise.

## Pricing / freight ownership
`data/settings.json` is the scenario configuration. Published normal-goods air tier:USD20.50/kg plus₦1,500/kg clearing;chargeable kg=max(actual, L×W×Hcm÷6000). The guide also mentions₦1,500–2,500/kg clearing elsewhere:re-quote the actual service. Source:https://dechaser.com/china-to-nigeria-shipping/ . Detailed assumptions and exclusions are in `data/evidence/freight-reference.json` and every product's shipping conditions.

USD/NGN1,350 and CNY/USD0.15, yielding CNY/NGN202.50, are **rounded editable assumptions,not verified current rates**. Prior retrieved FX pages had future dates relative to the authoritative session date and are not adopted as live FX. Sharp kitchen tools need carrier approval and protective packing. Food-contact goods need relevant documentation. Proportional allocations are not isolated-parcel quotes;minimums/rounding, additional protective cartons,China transport,taxes/VAT,insurance and onward delivery are unresolved/excluded.

Draft sale=ceil to₦100 of1.25×[max(source, floor≥¥5.20)×CNY FX + max(conditional freight, floor≥₦2,000)]. Pending shipping uses a **placeholder**,not researched freight. Compare-at and roughly12%/10%/8%reductions are draft proposals,**not former prices or proven savings**. No claimed affordability/landed-cost/profit guarantee. Particularly cheap/bulky tools may cost less locally than with small-lot air freight. The observed source values are never raised to the planning floor.

## Team modules / editing contract
```
template.html                 Page structure and visible methodology
assets/css/styles.css         Responsive design;no remote fonts/CDNs
assets/js/app.js              Filtering,calculator,CSV export,image viewer
assets/js/products.js         GENERATED mirror—do not edit
assets/images/NNN-main.jpg    Sole main image for each stable ID
scripts/assemble.py           Merge evidence+buyer copy+price scenarios
scripts/build.py              Generate offline/modular HTML,JS data andCSV
scripts/validate.py           Structural/arithmetic/image/preservation checks
scripts/browser-qa.cjs        Offline Chromium regression;no screenshot clutter by default
data/evidence/selected.json   Canonical IDs,names,source cards andbrand evidence
data/evidence/guides.json     20 family-specific buyer-copy modules
data/evidence/detail-notes.json   19readable supplier detail findings
data/evidence/detail-access.json  Attempt/captcha coverage
data/evidence/jumia-access.json   Exact-name direct access results
data/market-observations.json     Price contexts,whole-pack counts andsource URLs
data/image-manifest.json          Asset provenance/download results
data/evidence/browser-inspection.json 200saved-DOM main-image associations
data/evidence/excluded-earlier-kitchen.json Earlier Kitchen URLs excluded
data/evidence/preserved-sha256.json Prior189protected files
```
Edit canonical project inputs,then rebuild;do not patch generated HTML/JS/CSV. Research extraction/editorial bootstrap scripts under `../research/kitchen-week2` document earlier collection,not the recommended rebuild route:rerunning them can overwrite refinements. Keep stable IDs and ordered200-record arrays. New technical observations must have their own offer/variant evidence,not borrowed siblings. Pack prices must not become silent per-piece prices. Keep exact buyer headings. Do not turn supplier heat/steel/food-grade headlines into tested claims.

## Rebuild and QA
From workspace root:
```
python kitchen-week2-product-hunt/scripts/assemble.py
python kitchen-week2-product-hunt/scripts/build.py
python kitchen-week2-product-hunt/scripts/validate.py
node kitchen-week2-product-hunt/scripts/browser-qa.cjs
```
Python assembly/build use the standard library;validation requiresPillow. Browser regression requires Node+Playwright+Chromium with its OS libraries installed. Screenshots are opt-in via `KEEP_QA_SCREENSHOTS=1`;they are not deliverables.

**Final QA:** structural/arithmetic/image checks PASS;29browser checks PASS including5×40,all200view,search,exact headings,13/187freight filters,27pending Jumia,10perfamily,editable floors/FX,immutable observations,JS/Python arithmetic agreement,CSV download,all200embedded-image decoding,viewer/Escape/focus,390px mobile overflow andmodular file mode.189previous protected catalogue/data/code/archive files unchanged by SHA256,including the requested Electronics Week2ZIP. QA does not certify research completeness,safety,stock orprocurement readiness.

No Kitchen ZIP was created;the previous Electronics Week2ZIP remains untouched. Earlier image-only deletion is not reversed. New200main assets are retained;temporary image-audit sheets/screenshots are removed after review.

## Workspace budget
Raw research HTML pages and aggregate catalogue JSON were losslessly gzip-compressed (not the deliverable HTML) to keep the workspace near the snapshot budget. Their complete original bytes are retained;see `../research/compressed-source-pages.json`. Only for research replay,run `python research/restore_raw_sources.py kitchen-week2` from the workspace root first. Opening/building/validating the modular orstandalone catalogue does not need decompression. Completed prior catalogue project files and the requested Electronics ZIP are unchanged.
