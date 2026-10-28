# Electronics Product Hunt — Team Handoff

## Open the project
Download and extract the ZIP. Open `index.html` in a browser. Keep the folders together. No installation, network access or build step is required.

## File structure
```text
electronics-product-hunt/
├── index.html              # Commented markup: five product cards and image grids
├── assets/
│   ├── css/styles.css      # Layout, typography, responsive grid and print styles
│   ├── js/app.js           # Override validation, cost calculations and JSON export
│   └── images/             # Local image copies used by the HTML
├── data/
│   ├── products.js         # Runtime product records; loaded before app.js
│   └── products.json       # Same initial records, for team/tool interchange
└── README.md               # Setup, editing and verification notes
```

## Editing guide
- **Product Details / gallery layout:** edit the labelled sections in `index.html`.
- **Colours, spacing and grid:** edit `assets/css/styles.css`.
- **Calculation and export behaviour:** edit `assets/js/app.js`.
- **Pricing / source records:** edit `data/products.js`; synchronize `data/products.json` and the static HTML display when changing initial values. The JSON file is an interchange copy, not loaded by the page.
- **Images:** place images in `assets/images/` and update the HTML `src`. Retain original supplier URLs in the data for provenance.
- Static card content and runtime data are deliberately separate in this no-build handoff; they do not automatically synchronize.

## Current state
AUTHOR: DAVE ADEX. Five current products grouped into Day 1 (5 / 40 capacity). Each daily grid holds up to 40 product cards. Main images only: all support and comparison galleries were removed for this session. Prices are carried forward, not newly revalidated. Product data contains original remote image URLs; displayed copies are local.

## Important verification checks
Confirm exact offer/variant, quote, MOQ, image rights, package weight, landed costs and certificate scope before publication. P9 attributes are supplier-stated. Compare-at prices and discounts are proposals, not proven historical pricing. Enter your actual exchange rate before evaluating costs.

## Comments and code sections
HTML regions have descriptive comments. CSS sections and JavaScript functions explain their purpose; JavaScript validation, calculation and download steps have inline comments. JSON does not support comments, so its purpose is documented here and in `products.js`.

## Changes made in the browser
Apply overrides before exporting. The export captures the current in-memory product records. Browser changes are not automatically saved into these project files.

## Daily grid maintenance
Add product cards and matching data records in groups of up to 40. After Day 1 reaches 40 records, create Day 2 using the same `.day-section` / `.day-grid` structure. Current five records remain unchanged; empty slots are not fake products. Keep product IDs aligned with data indices for pricing controls.

## Brand policy
Use the original product brand when supported by source evidence; otherwise use `Other`. Never substitute the manufacturer, model name or compatible-device brand. Current records: G200 = Hongxikang (pinyin romanization of supplier-listed 鸿熙康; official English trade name unverified); the remaining four = Other pending original-brand evidence.

Brand display uses English/Latin letters. Prefer an established official English name; otherwise clearly label romanization. Use Other when the original brand is not established.

## Day 1 completed: 40 records
35 additional Step 2 sourcing leads were added to the original five. The new records include supplier links, card prices, original titles, main image URLs and English brand labels (or Other). New Jumia and retail fields are null/pending, not zero. `data/new-35-products.csv` contains only the added records. Audio and computing accessories dominate this shortlist; it is not a balanced survey of all electronics categories. Source claims, variant pricing, MOQ, stock, authenticity and image rights require checking before procurement.

## Step 3.1 — Jumia comparison audit (28 October 2026)
All 40 records reviewed: 30 extracted price references, 10 unresolved. 14 references use accessible Jumia page evidence; 16 use search-index extracts. Aigo T98 and HM11 indexed prices conflict with empty direct-search results and remain unconfirmed references, not verified active offers. Brand/model-name, model-family and functional-comparable classifications are recorded separately. No identical-SKU guarantees. Prices exclude Jumia delivery. Null means no accepted price, not zero.

`data/jumia-price-comparisons.csv` is the full audit with source URLs and caveats. Product-brand fields were not overwritten by Jumia retail brands. Commercial retail/compare-at proposals for the 35 new products remain pending. Main images only, as requested.

## Step 4 — Supplier Product Details

Checked 28 October 2026. 38/40 supplier pages yielded readable specifications; T70 (#27) and Jisiyuan vertical mouse (#34) returned CAPTCHA, so invented/generic specifications were removed and these remain pending.

Each Product Details section identifies its basis (attributes, packing, readable detail prose). No image-only text was transcribed or OCRed and no detail/support images were added. Product #19 (Q10) uses readable attributes only from the returned page chunk; deeper packing/detail sections were not retrieved. The supplier-product-details.csv audit contains all 40 sources, English extracts, statuses and verification notes.

`product_details` stores structured English facts; `description` stores the current long English product description; the full extracted facts and warnings remain in the dedicated fields. Dedicated fields retain the source URL, check date, extraction basis, status and verification notes. Conflicting units/weights, feature contradictions and mixed-model offers are intentionally flagged, not silently corrected. Waterproofing, runtime, chipsets and certification are supplier claims, not independently verified. Warranty and customization statements require written seller confirmation.

Source prices, base shipping, Jumia evidence and retail proposals were not changed in this step. Main-image-only policy and author DAVE ADEX are retained.

### Optimal-long Product Details — current presentation
Each card now presents a simple, consumer-facing, multi-paragraph English description, with 150–200 words
for each of the 38 readable supplier listings. T70 (#27) and the Jisiyuan vertical
mouse (#34) remain shorter, clearly marked provisional descriptions because their
supplier pages returned CAPTCHA. Copy was expanded only from previously extracted
supplier text, not from Jumia or unrelated products. No fresh page recheck is claimed. The tone is Simple and the audience is Consumers.
Copy explains uses, connections, choices and relevant limits without freight, MOQ,
factory codes, certification numbers or reseller terms dominating the description.
Research and supplier conflicts remain available in the expandable specifications.

The complete structured extraction and verification notes remain expandable on every
card. `description` contains the long text; `brief_description` preserves the earlier
short version. `description_word_count`, `description_basis` and the editorial date
support handoff. `data/long-product-descriptions.csv` is the long-copy export, while
`data/brief-product-descriptions.csv` retains the brief-copy export. Both remain drafts
requiring supplier verification, especially for mixed variants and inconsistent fields.

No prices, Jumia references, shipping allowances, retail proposals or main images were
changed by this editorial update. No support images or transcribed image text added.
