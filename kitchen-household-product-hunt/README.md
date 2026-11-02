# Kitchen & Household — 200 product research candidates
**Author: DAVE ADEX · Captured 02 November 2026**

This is a NEW, separate project. Do not merge it into or overwrite the completed fashion or electronics catalogues.

## Open / use
- `index.html`: modular offline webpage. Keep the folder structure intact. No internet, build system or CDN needed to browse.
- `../kitchen-household-product-listings.html`: generated single-file offline HTML, all 200 main images embedded.
- `data/products.csv`: spreadsheet handoff with all descriptions and source/comparison URLs.
- Use the five Day tabs for **40 products per day**; search and filters work inside the selected day. “View all 200” searches everything.
- Product Details shows the 150–200-word buyer copy under the exact three requested headings, followed by separate evidence notes.
- Calculator edits affect only current planning proposals. CSV export includes the current scenario. Reset restores defaults.

## Important research limitations — do not remove these labels
- 200 distinct canonical 1688 offers, 20 catalogue groups, 200 catalogue main images.
- Chromium inspected the **20 catalogue pages**, not all 200 detail galleries. Image URLs were matched by offer ID; selected-SKU image correspondence and first detail-gallery position remain unverified. **Main images only; no support galleries.**
- **20 representative supplier detail pages** inspected using rendered reader text. Other 180 are catalogue-card candidates, not fully verified purchase-ready SKUs.
- **15 conditional freight calculations / 185 pending.** Some of the 15 are weight-only lower bounds because packed dimensions are missing. Never transfer a representative's weight to another product.
- **All 200 direct Jumia English-name requests were blocked (HTTP403).** Indexed research provides **193 broad comparables**, often with substantial pack, material, shape or size differences. **Seven comparisons pending, zero identical-SKU matches.** Indexed observations are not checkout-confirmed prices and exclude delivery. Some are deliberately weak category context; use the per-record caveat.
- Original observed CNY catalogue starting price is retained separately. Selected variant prices replace accessory minima where established. Six selected prices were shown in USD: a clearly labelled **CNY equivalent** uses the recorded USD/NGN and CNY/NGN cross-rate. This is NOT an original CNY quote.
- English brands only where supported by the source catalogue; Chinese/translated names become **Other**. No independent authenticity or trademark clearance is implied.
- Buyer copy is editorial, based on titles and available detail text. No independent food-contact certification, temperature rating, safety test, insulation duration or performance test has been performed.

## Pricing assumptions
Published source: https://dechaser.com/china-to-nigeria-shipping/ — 20kg+ Lagos door-to-door air scenario **USD14.88/kg + NGN1,500/kg clearing**. This is a consolidated allocation, not an individual small-parcel quote. Smaller consignments use different rates.

FX observations from Forbes currency converter, 02 Nov2026: USD/NGN1344.46; CNY/NGN202.082958. Live market rates may differ.

Chargeable kg = max(supplier packed kg, packed L×W×H cm /6000). Divisor6000 is an assumption, not a confirmed forwarder rule. Missing dimensions => weight-only lower bound. Outer cartons, freight rounding, domestic China delivery, insurance, handling, taxes/other charges may increase costs.

Planning proposal = ceil100[(max(source/equivalent CNY,5.20)×FX + max(conditional freight,2000))×1.25]. If freight is unknown, NGN2000 is **only the requested floor**, never researched freight. Most proposals are therefore floor-based drafts, not confirmed landed-cost prices. No artificial cap forces proposals below Jumia. Heavy products may be unsuitable for air freight.

Proposed compare-at = ceil100[proposal /0.90]. Discount is recalculated from the two rounded numbers. Both prices are **proposals**, not a historical sale or verified saving. Confirm cost, MOQ, pack, margin and exact market match before adopting any price.

## Team file map / ownership
- `data/products.json`: **source of truth** for names, buyer copy, SKU notes, pricing evidence and product-level status. Copy/content team edits only supported product facts.
- `data/settings.json`: scenario defaults; finance/logistics team owns these assumptions.
- `data/market-observations.json`: indexed Jumia evidence and explicit mismatch notes. Market team should replace broad context with exact functional/size/pack matches where possible.
- `data/image-manifest.json`: source URLs, local files and browser provenance. Asset team must preserve main-only policy.
- `data/evidence/detail-notes.json`: representative supplier packed weights, variant prices and contradictions.
- `data/evidence/browser-inspection.json`: catalogue DOM observations.
- `data/evidence/jumia-access.json`: exact-name queries, URLs, status codes for all200 attempts.
- `data/evidence/catalogue-selection.json`: original Chinese titles, catalogue prices and canonical source links.
- `assets/images/`: exactly200 actual supplier main JPEGs.
- `assets/css/style.css`: kitchen-only visual styling.
- `assets/js/app.js`: rendering, accessible dialog, filters, CSV export and transparent calculator; no external dependency.
- `template.html`: static page shell; edit then rebuild. Do not hand-edit generated index/standalone.
- `scripts/build.py`: regenerates modular/standalone/CSV using Python standard library.
- `scripts/validate.py`: structural checks. PASS does **not** mean pending factual research is complete.

## Updating safely
1. Assign reviewers by day or family, retaining stable IDs and canonical offer URLs.
2. Obtain selected-SKU packed weight, dimensions, carton quantity, unit price and MOQ for pending products. Record the source, date and any conflict before making a value numeric.
3. Verify exact Jumia item/pack comparability and live delivery-inclusive price separately. Do not divide a set price into assumed unit prices.
4. Never replace missing freight with a competitor's weight or a generic family estimate. Preserve lower-bound labels when dimensions/outer-carton allocations are unknown.
5. Edit `data/products.json` and the appropriate evidence record together. Updating evidence files alone does not automatically merge into products. Keep all descriptions within150–200words and retain exact headings.
6. Run `python scripts/build.py`, then `python scripts/validate.py` from this folder. Recheck browser behavior on desktop/mobile and repackage the project folder.

The collection is a useful, fully browsable **research draft**; supplier verification and exact market matching remain incomplete. No purchase-ready or universally affordable claim is made.
