# Electronics — Week 2 · DAVE ADEX

## Open the catalogue
- **Main deliverable:** `../electronics-week2-product-listings.html` — standalone HTML, all 200 sole supplier main images embedded. Works offline without a server/CDN.
- **Team/modular version:** `index.html` — keep this whole folder together so local CSS, JavaScript and images resolve.
- Five daily grids of 40; default Day 01. Choose “All five days” for all 200.
- Search, type/evidence filters, buyer-copy expansion, main-image viewer, editable batch planning and CSV export are included.

## Evidence status — read before use
- 200 distinct 1688 offer URLs; none repeats earlier Electronics catalogue offer URLs.
- Twenty families × ten offers. Relevant home/study/business electronics, including some destination-specific travel adapters.
- 200 catalogue main-image/offer associations inspected in saved public catalogue HTML using Chromium; exactly one downloaded main image per record. No support gallery. This is **not** live first-gallery, exact selected-colour or product-quality verification.
- 20 representative supplier detail pages inspected; the other 180 records rely on public catalogue title/price observations rather than selected-option technical sheets.
- **12 conditional freight scenarios:** nine weight-only lower bounds, three with dimensions. **188 amounts pending.** No sibling offer inherits a representative's weight.
- UPS/battery cargo and contradictory/unmapped packing remain pending. Published normal-goods rates are not battery approval or quotes.
- All 200 direct Jumia English-name requests were blocked. Twenty family search themes produced indexed context; 28 differentiated observation entries are stored, reused for **130 non-identical price assignments**. Seventy prices are pending. One advanced tester observation is deliberately not assigned to a basic/different tester. **Zero verified identical live-checkout matches.** Some indexed contexts are old; the Konka comparator is out of stock.
- 151–171 words of buyer-facing explanation per product, under the exact three requested headings.
- Electrical safety, radio approval, authenticity, stock, current dispatch and import readiness are not certified. No guaranteed quick-dispatch claim.

## Important variant corrections
- #21: 1m copper-clad-aluminium RJ45 lead, ¥1.25 observation; not certified Cat5e/PoE.
- #51: selected USB3 enclosure ¥13, not the cheaper USB2 option.
- #61: 19V 2.37A **45W** replacement, ¥20; promotional title/photo says65W. Acer is compatibility, not manufacturer.
- #161: UPS **body ¥85**, not the ¥15 charger-only starting option. Battery freight pending.
- #1: starting ¥0.20 may refer to an adapter, not the selected reader; source USB2 attribute conflicts with USB3 headline/photo. No verified USB3 speed.
- Original supported Latin manufacturer labels are retained; translated Chinese brands and compatibility names are not invented as original English brands. Listing a brand does not prove authenticity.

## Planning assumptions — never rewrite evidence
Source floor ≥¥5.20; freight budget floor ≥₦2,000. Rounded editable FX scenarios: CNY/USD0.15 and USD/NGN1,350 → CNY/NGN202.50. Retrieved Forbes pages show09November2026, later than the session date27October2026; those snapshots are not accepted as current FX. Get a current settlement quote.

Published normal-goods1–10kg freight tier: USD20.50/kg plus ₦1,500/kg clearing, Dechaser. Chargeable=max(actual kg, L×W×Hcm÷6000), subject to carrier rules, acceptance, minimums and protected export packing. A sub-kilo allocation is not a verified isolated-parcel charge. Other shipment tiers differ. Taxes, insurance, rounding/repacking, China transport and onward delivery beyond Lagos are excluded/unresolved.

Draft sale = ceil-to-₦100(1.25 × [max(observedCNY, floor) × CNYFX + max(conditionalFreight, budgetFloor)]). A pending fee uses the budget floor **only as an unverified placeholder**. Compare-at and roughly12%/10%/8% reductions are proposed planning values, not former prices, proven savings or live offers. Supplier unit/pack and full landed costs are not established.

## Modular team workflow
1. `data/evidence/selected.json`: English identities, original source titles/links, starting price observations and dispatch claims.
2. `data/evidence/detail-notes.json`: selected-option facts, observed packing, conflicts and freight holds. Never propagate weight to siblings.
3. `data/evidence/guides.json`: family-specific buyer copy in three blocks. Product names/detail facts supply record-specific content.
4. `data/market-observations.json`: indexed comparator observations, explicit IDs, model/pack/stock caveats. Never describe a family benchmark as an exact match.
5. `data/settings.json`: editable reference scenarios and published freight sources; do not present as live FX.
6. `data/image-manifest.json`: sole main-image source, browser provenance and local file path.
7. `template.html`, `assets/css/styles.css`, `assets/js/app.js`: separately commented layout, styling and interactions. JavaScript escapes dynamic text.
8. Rebuild only the NEW Week2 outputs:
   ```bash
   python electronics-week2-product-hunt/scripts/assemble.py
   python electronics-week2-product-hunt/scripts/build.py
   python electronics-week2-product-hunt/scripts/validate.py
   node electronics-week2-product-hunt/scripts/browser-qa.cjs
   ```
   Python assembly/build use standard library; validation also needs Pillow. Browser QA requires Playwright + Chromium. Regeneration writes `data/products.json`, CSV, JS data mirror, modular index and the NEW standalone HTML only.
9. `data/validation.json`: structural/arithmetic checks and hashes of162 protected previous files. `data/browser-qa.json`:29 offline/browser behaviour checks. PASS does not certify procurement readiness.

## Preservation and storage
Earlier catalogue HTML, JSON/CSV and code remain unchanged;162 protected-file hashes verified. Earlier workspace image files were intentionally deleted under the user's prior image-only authorization; their old standalone embedded images remain. No old image assets were restored. No ZIP was created. Optional audit screenshots are not part of the deliverable.
