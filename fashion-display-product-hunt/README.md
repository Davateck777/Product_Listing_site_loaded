# Fashion&Display — Days 01 + 02
**DAVE ADEX · 80 products · 40 per day · Original Day1 visual format**

## Open the same deliverable
`fashion-display-product-listings.html` remains the single-file offline entry point, now containing both days. Within this ZIP, open `index.html` with its local assets. There is no external script, stylesheet or font dependency. External source links need internet.

- **Day01 preserved:** the original40 product records, descriptions, observations, image paths and research dates are unchanged.
- **Day02 appended:**40 unique offers,30 wearables and10 display/storage items, added in the same cards, typography, colours and layout as Day01.
- **Combined:**80 products,54 wearables and26 display/storage; exactly80 main images, no support images.
- Use the new **day selector** for All days, Day01 or Day02. Existing search, product-type filters, research-gap filters, expandable buyer copy and image viewer work across both days.
- Global IDs1–40 are Day01;41–80 are Day02. Day02 retains its daily number1–40 in `day_product_number`; card tags show the day and daily number to avoid collisions.

## Files and regeneration
- `data/products.json`: canonical combined80-record catalogue. The first40 records equal `data/evidence/day1-original.json` exactly.
- `data/products.csv`: combined80-row Excel-friendly export.
- `data/evidence/day1-original.json` and `README-day1-original.md`: preserved original Day01 data and documentation.
- `data/evidence/day2/`: original Day02 records, methodology, Jumia evidence, manifest, queue and supplier/browser evidence.
- `assets/images/`: original40 Day01 images plus40 `day2-XX-main.jpg` files.
- `assets/css/styles.css`: original Day01 stylesheet, unchanged.
- `assets/js/app.js`: original card format extended for per-day data, pending source prices, day filtering and proposal defaults.
- `scripts/build.py`: run `python scripts/build.py` to regenerate the modular HTML, offline `fashion-display-product-listings.html`, CSV and `fashion-display-product-hunt.zip`.
- `scripts/validate.py`: run after building. It checks80 unique records, per-day counts, exact preservation of Day01, image policy, copy, CSV and ZIP.

## Pricing defaults and observations
Day01 retains its original planning assumptions: CNY/NGN210 and USD/NGN1500,25% cost uplift, proposed10% compare-at target. Day02 retains the reference converter observations used in its separate research: CNY/NGN202.082958 and USD/NGN1344.46 on02 November2026,25% uplift and variable proposed compare-at targets12%/10%/8% by sale band.

The controls display Day01 defaults. **Until you edit a planning field, each day uses its own original basis.** Editing a field explicitly applies the shared control values to both days. **Restore per-day defaults** reinstates each day's original basis. Overrides never mutate supplier or Jumia observations. Missing source amounts or freight use visibly flagged floor-only planning placeholders. Floors remain≥¥5.20 and≥₦2,000.

Day02 native USD observations are preserved; their CNY equivalents are explicitly indicative conversions, not supplier CNY quotations. One Day02 source price is hidden and remains pending. Compare-at values are proposed merchandising references, not evidence of a former price, a genuine discount or profitability. Unquoted costs remain excluded; confirm before publication.

## Research and freight limitations
Both days remain research drafts, not completed checkout or carrier quotes. Day01 retains its29 Jumia comparisons and29 conditional weight-only allocations. Day02 adds29 comparisons and33 conditional allocations, leaving11 Jumia prices and7 freight values pending for that day. No exact-SKU match is certified.

Day01 freight evidence is the20 January2026 rate card and its original assumed FX. Day02 uses the17 September2026 published normal-goods20kg+ Lagos door-to-door rate: USD14.88/kg+₦1500/kg clearing, reference conversion₦21,505.5648/kg. Where credible dimensions exist, the Day02 scenario uses max(actual weight,L×W×H/6000);6000 is a planning assumption, not a confirmed carrier rule. Missing dimensions mean a weight-only lower bound. Conflicting weights remain pending. See each card and `data/evidence/day2/methodology.json` for provenance.

Allocations require a qualifying consolidated20kg+ batch; they are not standalone tiny-parcel quotations. Current rates, carrier FX, rounding, minimums, packed dimensions, repacking, duties/VAT/levies, origin transport and agent/payment fees require confirmation. Native source prices, MOQ and pack contents must be reconfirmed. Jumia prices are indexed comparisons, not checkout verification.

Actual browser inspection encountered login/verification barriers. Main images came from supplier-page reader evidence; do not claim successful DOM verification. Image-use permission, pattern/IP clearance, material and lens-performance claims need checking. Main images may themselves be supplier collages showing multiple options; the gallery is not a promise that all pictured items are included.

The separate Day02 deliverables remain available. Electronics are untouched. A pre-merge Day01 standalone and ZIP were retained in `backups/fashion-day1-before-merge/` beside this project.
