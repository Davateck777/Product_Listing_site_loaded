# Fashion&Display · Day 01
**Author: DAVE ADEX · Research date: 29 October 2026**

## Open the deliverable
Open `index.html` from this folder, with its assets beside it. For a single-file, fully offline version, use the separately delivered `fashion-display-product-listings.html`. No server, CDN, external font, API key or package installation is needed. The offline file embeds all 40 main-image JPEGs. External supplier, Jumia and freight links naturally require internet access.

## What is included
- Exactly **40 new Fashion&Display records**: 24 wearable accessories and 16 display/storage items. The earlier electronics project is separate and unchanged.
- English product names; original English brand text where recorded, otherwise `Other`. A supplier brand attribute is not trademark ownership verification.
- Buyer-facing **Product Details**, 151–170 words each (body-only count), in the three requested sections: What the Product is? / What are the clear benefits of the Product / Features of the Product.
- 1688 offer links, observed CNY prices, option/price limitations, supplier facts and specific contradictions.
- **40 main images only**, all downloaded. Support images, support-image URLs and gallery grids have been removed by user instruction. Click a main image to enlarge it. Main images only will be used for the rest of this session.
- **29 Jumia Nigeria priced comparables**, explicitly not verified identical SKUs; 11 prices pending. Pack-count, size and material differences are retained. Some outliers are flagged rather than used to imply market value.
- **29 conditional weight-based shipping allocations** and 11 pending usable-weight estimates. No product has a confirmed final carrier charge.
- Editable batch proposal floors: source **¥5.20 minimum**, shipping **₦2,000 minimum**. These never overwrite recorded source evidence.
- Search, product-type and research-gap filters; expandable buyer copy; evidence panels; offline image viewer; CSV and JSON handoff.

## Important unfinished acceptance criteria
**This is a research draft, not a fully verified publication batch.**
1. **Main-image-only policy.** All support images have been removed from the HTML, JSON, CSV, manifest, assets and ZIP by user instruction. The 40 retained main images came from public page-reader evidence; browser checks reached login or verification screens. Do not describe them as browser-verified. Original main-image URLs are retained in `data/image-manifest.json`. Confirm image-use permission.
2. **Shipping: conditional only.** Confirm the shipment tier, actual/volumetric chargeable weights, carrier minimums/rounding, packed dimensions, variant-specific weights and fresh quote. Supplier weights can be generic or refer to another variant; do not treat them as final billable weights.
3. **Jumia: exact matches not established.** Eleven product prices remain pending. Category/search landing-page figures are public search-index observations, not proof of current checkout price or stock. Product-name search links are prepared for every record; evidence quality varies. Do not use prices from Jumia Kenya/Egypt as NGN.
4. **Source quotes and MOQ: pending.** Catalogue starting prices are not universal variant prices, and MOQ is not consistently established. In particular necklace 5 may start at a bracelet option; necklace bust 26 has size-dependent detail prices; PET basket 32 needs size matching; eyeglasses box 37 spans ¥25–29 by option. Confirm before ordering.
5. **No live FX research has been claimed.** The USD and CNY conversions are editable assumptions. The carrier states it uses its own approved exchange rate.

## Real freight-rate basis
Source: https://dechaser.com/fcel-china-to-lagos-rate-card-2026/

Public rate card dated **20 January 2026**, read during this research; NOT a fresh October quotation. Normal cargo, consolidated **20 kg+**, Lagos door-to-door: **USD 14.88/kg + ₦1,500/kg clearing**. Stated transit: 7–10 working days. Carrier reconfirmation is required. The 20 kg threshold is for the shipment, not one product. Do not apply this bracket to an individual small parcel without a qualifying consolidated shipment.

At the explicit **assumed ₦1,500/USD**, weight-only allocation is:

`(supplier grams ÷ 1000) × (14.88 × 1500 + 1500) = kg × ₦23,820`

Volumetric adjustment is not applied because final packing and the carrier divisor are not established. Government duties, taxes, levies, origin pickup and storage are excluded by the cited card. Standalone 1–10 kg cargo is listed at USD 20.50/kg + ₦1,500/kg; it is not the chosen planning scenario. Placeholder 1 g packing for product 1 is rejected. Conflicting 428 g / 1,000 g for product 14 is not averaged. Unitless weights on products 30 and 31 are not silently converted into grams.

## Proposed prices and discounts
Defaults: source floor ¥5.20; shipping floor ₦2,000; **assumed** CNY/NGN 210; **assumed** USD/NGN 1,500.

`planning price = ceil_to_100(1.25 × [max(source observation, source floor) × CNY FX + max(conditional weight allocation, shipping floor)])`

If no weight is usable, the shipping floor is an **unsupported placeholder**, not researched shipping. The 25% uplift is on this incomplete planning cost, not a verified net profit margin. Other import/retail expenses are excluded.

`proposed compare-at = ceil_to_100(planning price ÷ 0.90)`

The rounded proposed discount is displayed. This compare-at is **not a historical price**. Do not publish savings claims until there is a genuine, lawful reference price. Some proposals exceed Jumia category comparables; affordability and margins are not assured, especially where pack quantities or materials differ. Changing the controls changes the HTML scenario only; it does not save back to JSON/CSV. The supplied CSV uses documented defaults.

## Fast team handoff
| File | Ownership / purpose |
|---|---|
| `data/products.json` | Canonical 40 records; copy, evidence, images, price observations and assumptions |
| `data/products.csv` | Generated spreadsheet export, UTF-8 BOM; one row per product |
| `data/jumia-evidence.json` | Comparable titles, prices, direct evidence/search links and match limitations |
| `data/image-manifest.json` | Original URLs, delivered filenames, dimensions, status and main-image-only policy notes |
| `data/evidence/browser-inspection.json` | Actual browser outcomes; login/CAPTCHA, not a successful product inspection |
| `data/evidence/selected.json` | Original Chinese catalogue selections and collection URLs |
| `data/RESEARCH-QUEUE.md` | Open source/variant/image/price checks |
| `assets/images/` | 40 resized main-image JPEGs; original URL preserved, not original-resolution files |
| `assets/css/styles.css` | Responsive design tokens and layout |
| `assets/js/app.js` | Rendering, filters, pricing proposals and image viewer |
| `assets/js/products.js` | Generated mirror; do not edit manually |
| `scripts/build.py` | Standard-library-only HTML/CSV/offline/ZIP rebuild |
| `scripts/validate.py` | Batch integrity, copy-length and asset checks |

### Rebuild after edits
1. Edit canonical `data/products.json`; retain nulls for missing evidence, never use zero for unknown prices.
2. Update companion evidence/manifest files when changing sources or images.
3. Run `python scripts/validate.py` and `python scripts/build.py`.
4. The builder writes `index.html`, `assets/js/products.js`, `data/products.csv`, and the standalone HTML + ZIP beside this project folder. It does not fetch prices or images.
5. Recheck descriptions if edited: body word count excludes headings. Recheck sample fit/material and source options before publishing.

Original facts, caveats and proposals are separate fields to support a large team without accidental evidence overwrites. Comments identify each rendering, pricing and export responsibility. No earlier electronics files are modified.
