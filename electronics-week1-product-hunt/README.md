# Electronics · Week 1 — DAVE ADEX

A NEW mixed-electronics research catalogue: **200 unique 1688 offers, five days ×40**, 20 families. Earlier Electronics, Fashion, Kitchen and Interior Designs catalogues are not modified.

## Open the catalogue
- Easiest: open the supplied `electronics-week1-product-listings.html`. CSS, scripts, data and all200 main images are embedded; no connection is needed for browsing.
- For the team: extract this ZIP completely, then open `electronics-week1-product-hunt/index.html`. Keep its neighbouring folders together.
- 1688, Jumia, original-image and reference links require internet. No backend, account, CDN or external font is needed.
- Browser CSV export is available; some sandboxed previews block downloads, so open the downloaded HTML in a browser if needed. A fixed CSV is included in `data/products.csv`.

## What is included
| Day | Collection | Records |
| --- | --- | --- |
| 1 | Listen & connect: wired earphones, earbuds, speakers, headphones |1–40|
| 2 | Charge & power: chargers, cables, power banks, wireless charging |41–80|
| 3 | Computer essentials: mice, keyboards, hubs, webcams |81–120|
| 4 | Light & cool: desk lights, sensor lights, torches, fans |121–160|
| 5 | Create & travel: microphones, stands, car accessories, watches |161–200|

Each record has an English name, supported original English brand or Other, Electronics category, one browser-inspected catalogue main image, a canonical1688link, source ¥ observation, market research, proposals and158–181words of buyer-focused details under the three requested headings. Chinese supplier wording and brand fields are retained in evidence for auditing; original photographs are not translated or embellished. No support-image galleries are included.

## Research boundaries — read before procurement
- **20 representative supplier-detail inspections**. Other offers have catalogue-card evidence, not a verified selected-SKU technical/packing sheet. The ambiguous capsule power-bank offer was replaced; reasons are retained.
- **15 conditional freight scenarios;185 pending**. Three are weight-only lower bounds without packed dimensions. Weights are never propagated to sibling products. Several supplier values conflict; no numeric freight is shown for those offers. Heavy/generic rows remain visibly conditional.
- Freight reference: Dechaser China→Nigeria guide, normal20kg+ Lagos-door allocation **USD14.88/kg +₦1,500/kg**; battery route **USD15.50/kg +₦1,500/kg**. Battery final-mile coverage is not explicit. Normal published transit7–10days, battery15–25working days; these are not delivery guarantees. Minimum charges, cargo acceptance, duties/VAT, insurance, cartons, rounding and domestic transport need a forwarder quote. Volumetric divisor6000 is an assumption, not an established provider rule.
- All200 direct Jumia name searches were blocked. **198 have priced indexed functional/model-wording contexts, two pending (#004,#178); zero verified identical-SKU matches.** Competitor brands, kits, lengths and capacity often differ. #056 uses the UPPER end of an indexed₦3,119–5,773 cable range, not a verified selected5m price. #110 compares a four-port powered ORICO hub with a ten-port candidate; it is broad context only. Search index prices may be stale and exclude delivery. Do not describe these as proven savings.
- FX observation02Nov2026: USD/NGN1,344.52; CNY/USD0.150229; calculated CNY/NGN201.98589508. Reference URLs are in settings and the page. Reconfirm rates.
- Source prices are observations, generally STARTING amounts, not binding quotes. Selected variants, MOQ, packs, included accessories and dispatch must be quoted. #061's boxed10000mAh price is unverified; a different lower reader price was not substituted. #191 is selected as the D8silicone watch; earbuds inclusion from the broader title is unconfirmed.
- Battery116/normal-candidate84 is a provisional research classification, not carrier approval. Request battery documents (including MSDS/UN38.3 as applicable), exact chemistry/Wh and forwarder confirmation. Verify mains input/plug suitability, USB protocols, receivers, app/OS support and certifications. No supplier stock, quick-dispatch, medical, waterproof, airline or safety claim is independently established.
- Two offer URLs (#015/#022) also appeared in an older electronics catalogue; all200 in THIS catalogue are unique. This is a new compilation, not a guarantee of200 historically unseen offers.

## Price proposals, not fabricated offers
`planning source = max(observed ¥,5.20)`; `planning freight = max(conditional freight,₦2,000)`. If freight is unknown,₦2,000is only the requested proposal floor, **not researched shipping**. Draft sale rounds up to₦100after25%cost markup. Proposed compare-at rounds up from sale÷0.90; displayed reduction is a planning proposal, never a past selling price. Affordability is not established; proposals above the broad Jumia context are flagged. Do not publish floor-only drafts as confirmed landed-cost offers.

## Modular file map and team ownership
- `template.html`: semantic layout and research disclosures; content/layout team.
- `assets/css/style.css`: responsive styling; design team.
- `assets/js/app.js`: commented day navigation, filters, detail dialog, route-aware calculator and CSV export. No external libraries. UI team.
- `assets/images/NNN-main.jpg`: exactly200 optimised main photographs; image team. Replace only with inspected MAIN images, recording provenance in the manifest.
- `data/products.json`: assembled editorial/evidence records; generated from reviewed inputs below.
- `data/evidence/selected.json`: curated200-offer master; maintain stable IDs/day assignments.
- `data/evidence/guides.json`: buyer-language family copy; assembly integrates per-product names/facts. No seller training.
- `data/evidence/detail-notes.json`: per-offer supplier findings. Only this offer's packing may support its freight; preserve unresolved conflicts.
- `data/evidence/browser-inspection.json`, `data/image-manifest.json`: exact-offer image provenance and local paths.
- `data/evidence/jumia-access.json`, `data/market-observations.json`: searches, blocks, observations, explicit mismatch notes and indexed-source URLs.
- `data/evidence/freight-reference.json`, `data/settings.json`: published rate evidence and planning assumptions. Update together, including HTML disclosures, if rates change.
- `data/products.csv`: fixed200-row export with buyer copy, cargo/dispatch and source caveats.
- `data/validation.json`, `data/browser-qa.json`: structural and browser reports; PASS does not certify research completeness, electrical safety or import readiness.

## Safe review and rebuild workflow
Assign stable ID ranges across product hunters. Keep one reviewer responsible for merging changes. Check source offer/variant, original brand, quote/MOQ, packing, battery classification, compatibility, dispatch and Jumia differences separately. Do not silently turn unknowns into estimates or transfer a sibling's weights. Do not add supporting images. Retain audit notes when replacing an offer.

For revised source records, update the relevant inputs above, then run:
```sh
python scripts/assemble.py
python scripts/build.py
python scripts/validate.py
```
Run from any working directory using the script paths. Python3 standard library is sufficient. `assemble.py` refreshes descriptions, cargo-specific estimates and initial proposals from reviewed source inputs. For direct editorial changes to generated `products.json`, run build/validate only; a later assemble will regenerate them. Calculator edits are temporary browser scenarios and do not change saved evidence.

Optional automated browser regression:
```sh
npm install playwright
npx playwright install --with-deps chromium
node scripts/browser-qa.cjs
```
Checks five40-card grids, all200view, search, evidence filters, exact headings, dialogs/Escape, calculator/reset, separate battery rate, CSV export, all200embedded images, mobile overflow, modular offline loading and JavaScript errors. Screenshots are for QA, not product support images.

The standalone build is written beside this project folder. It never overwrites older catalogue filenames. Keep the approved ZIP until DAVE ADEX decides whether to delete it.
