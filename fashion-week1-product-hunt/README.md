# Fashion&Display — NEW Week1
**Author: DAVE ADEX · Research checked: 02 November 2026**

200 distinct 1688 offers, five daily grids of40. This is a NEW catalogue; the earlier80-product Fashion catalogue and completed Electronics, Kitchen and Interiors projects remain unchanged. No earlier Fashion offer URL is reused. The original `fashion-display-product-hunt` warm-paper/oxblood design, serif hero, two-column image/title cards, expandable buyer copy, research panels and main-image viewer are retained, with five-day navigation and current evidence handling.

## Open or share
- **Standalone:** `fashion-week1-product-listings.html` beside this project folder in the ZIP. All200 main images, data, CSS and JavaScript are embedded. No network needed to browse; source links naturally require internet.
- **Modular:** extract the entire ZIP, then open this folder's `index.html`. Keep `assets/` and `data/` together. No server or installation needed for normal browsing.
- **Team data:** `data/products.csv`, `data/products.json`, `data/market-observations.json` and `data/evidence/`.
- **QA:** `data/validation.json` and `data/browser-qa.json`. A PASS certifies structural/arithmetic/UI checks, **not import readiness or supplier authenticity**.

## Five days
| Day | Record IDs | Product families | Products |
|---|---|---|---:|
|01|1–40|Scarves, caps, fashion sunglasses, belts|40|
|02|41–80|Wallets/purses, handbags, shoulder/crossbody bags, totes|40|
|03|81–120|Cosmetic pouches, hair clips/pins, headbands, necklaces|40|
|04|121–160|Earrings/cuffs, bracelets, rings, jewellery boxes|40|
|05|161–200|Jewellery stands, watch cases, backing cards, wardrobe/drying hangers|40|

150 wearable/accessory offers and50 organisation/display offers. There is also an all200 view. Filters combine with the selected day: use “All five days” for a catalogue-wide family search.

## What each product contains
English editorial name; supported original English brand where captured, otherwise **Other**; category **Fashion&Display**;150–200-word buyer-focused copy(actual range152–174, excluding headings); canonical1688 link; observed CNY price; one actual supplier main image with browser provenance; approximate conditional freight or a clear pending marker; Jumia indexed contextual price, quantity and caveats; exact-name Jumia search; separate scenario proposals. The exact buyer-copy headings are:
1. What the Product is?
2. What are the clear benefits of the Product
3. Features of the Product

Only main product images are supplied. Supplier photography may itself show several variants/props; a catalogue main image is not proof of the exact selected option or first position in every detail gallery. No support-image galleries are included.

## Read evidence limits before ordering
### Supplier evidence
All200 offer cards/titles and main-image mappings were browser-inspected.20 representative detail pages were checked. Other items lack verified selected-option technical/packing sheets. Starting catalogue price need not equal a chosen colour, size, material, supplied quantity or MOQ. The three confirmed detail-price corrections are ID111 ¥10.90; ID121 ¥2.90 per pair; ID171 ¥1.80 drawer option. Foreign-currency detail-reader displays are not relabelled CNY.

Original English brands are preserved where supported; transliterated Chinese names and digit-heavy style/model codes are not treated as verified English brands. “Other” is intentional, not a fabricated brand. Editorial benefits are plausible uses, not independent product tests. Unauthenticated UV, precious-metal, leather, gem, health/luck or anti-allergy claims are not adopted.

### Freight —16 conditional /184 pending
The Dechaser China–Nigeria guide supplies the published **normal-goods20kg+ Lagos-door USD14.88/kg +₦1,500/kg clearing** reference. Small shipments have different tiers. Published normal7–10-day transit is not supplier dispatch or a guaranteed arrival date. Full source URL and alternate tiers are in `data/evidence/freight-reference.json`.

Reference FX: USD/NGN1344.52; CNY/USD0.150229; cross-rate CNY/NGN201.98589508. Source links and date are in settings/template. Reference conversion is not a live payment quote.

Scenario formula: `max(weight_g/1000, L×W×H/6000) × (14.88×1344.52 +1500)`.
-6000 is an explicit planning divisor, **not a confirmed carrier rule**.
- Eight IDs(1,21,51,71,91,111,121,191) have weight-only lower bounds; some weights are just bare items/pendants, not complete protected packs. Do not order against those values as packed freight quotes.
- Eight other IDs have conditional selected-unit dimensions. ID151 is explicitly an unboxed unit; dimensions do not establish an export-ready carton.
- IDs11,31,61,181 have explicit unresolved/conflicting mass or quantity findings. No freight amount is assigned to them or to180 other unverified records.
- Outer cartons, allocation, repacking, minimums/rounding, insurance, China transport, duties/VAT, other charges and selected-unit completeness remain unresolved. Obtain a current forwarder quote and verify acceptance, particularly magnetic components.

### Jumia —200 contextual prices, zero identical matches
All200 exact-name direct searches returned blocks. Search-index evidence supplied200 numeric contextual assignments across39 records, not200 verified current product detail pages. Every assignment includes its comparator title, URL, observed whole price, quantity and limitations. Some contexts are deliberately broad family examples. No checkout, current stock, identical size/material/pack, delivery fee or actual savings is verified. ID-specific notes matter.

**Keep whole packs whole:**100 backing cards,15 mini claws,300 U-pins,10 clip hangers and other multi-packs are not compared as one item. No silent per-piece conversion is used. The source supplied pack is itself sometimes unresolved. The 40-clip sock rack is one rack, not40 individual hangers.

### Proposed prices — not observed offers
The batch desk permits floors at or above **¥5.20 and₦2,000**; lower input values are clamped by the calculation. Original supplier and market observations never change.

`draft_sale = ceil100(1.25 × [max(observed_CNY, source_floor) × CNY_FX + max(conditional_freight_at_planning_USD_FX, shipping_floor)])`.

Where freight is pending,₦2,000 is **only a proposal placeholder**, never a researched fee. A25% uplift is a draft budget rule, not a verified margin; no exchange spread, fees, tax or full landed cost is established. Proposals remain per unconfirmed supplier quoted unit/pack.

Compare-at is a second proposed figure: roughly12% reduction if sale<₦5,000;10% if<₦15,000;8% otherwise, with compare-at rounded up to₦100. Thus actual displayed proposed reduction can differ slightly. No former price is claimed or struck through as a genuine past offer. Affordability is not proven by an unrelated Jumia context. A review filter flags proposals above single-context prices; multi-pack unit savings are not inferred.

Current browser CSV export includes all200 records and current planning assumptions. The fixed CSV uses reference defaults. Browser edits are intentionally session-local; persist approved changes through the team source files.

## Modular source map / team ownership
- `template.html`: semantic HTML shell; disclosures, five-day labels and UI controls.
- `assets/css/styles.css`: original-fashion design system plus a commented Week1 responsive extension.
- `assets/js/app.js`: separated modules for escaping/data, proposals, cards, filters, image viewer and CSV.
- `assets/js/products.js`: generated data mirror; do not hand-edit.
- `assets/images/`: exactly200 locally saved JPEG main images, named by stable product ID.
- `data/evidence/selected.json`: canonical selection, English naming, original observations/brand field.
- `data/evidence/detail-notes.json`:20 representative findings; never copy a sibling's weight to another offer.
- `data/evidence/guides.json`:20 consumer-copy family guides, combined with product-specific facts.
- `data/market-observations.json`: indexed contextual comparator assignments; update exact ID coverage carefully.
- `data/evidence/{browser-inspection,jumia-access}.json`: browser provenance and direct search outcomes.
- `data/evidence/excluded-earlier-fashion-offers.json`: old80 URLs excluded from this selection.
- `data/image-manifest.json`: download/provenance log.
- `data/settings.json`: reference FX/rates; update date/source evidence before changing.
- `scripts/assemble.py`: merge reviewed inputs into full products; enforce word counts.
- `scripts/build.py`: generate modular page, standalone HTML, CSV and data mirror.
- `scripts/validate.py`: structural, arithmetic, count, uniqueness, image and evidence checks.
- `scripts/browser-qa.cjs`: optional Playwright offline desktop/mobile regression.
- `scripts/pack.py`: create the team ZIP only after successful validation/QA.

## Rebuild
Python3 standard library only for assemble/build/validate/pack:
```sh
python scripts/assemble.py
python scripts/build.py
python scripts/validate.py
# Optional browser QA (Node.js; install Playwright and its Chromium browser):
npm install playwright
npx playwright install chromium
node scripts/browser-qa.cjs
python scripts/pack.py
```
Paths resolve relative to scripts, not the working directory. Browser QA screenshots are only saved when the original research folder exists; screenshots are not required to use the package. The supplied ZIP deliberately excludes dependencies, raw research HTML, other catalogues and caches. The offline file is rebuilt beside the project folder. Stable IDs, source offer URLs and main-image filenames should not be changed casually. Rerun validation after every merge. Do not regenerate the selection from old research scripts without reviewing enrichment changes.

## Publication checklist
Reconfirm supplier identity/design permission, selected SKU/unit/pack, material/skin safety, price/MOQ, current stock and mainland dispatch; get actual packed-carton dimensions and mass; reconfirm freight/FX, tax/duty and carrier acceptance; verify equivalent Jumia offers/pack quantities and checkout totals; approve pricing before publishing any promotion. Preserve prior catalogues and retain this ZIP until the user requests deletion.
