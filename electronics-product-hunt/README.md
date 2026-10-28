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
Final editorial pass: 28 October 2026. All forty products have source-based English
Product Details with a Simple tone for Consumers. Each description has 150–200 words
and connects supported features with practical benefits: connection convenience,
listening choices, suitable device matching, controls, packaging and style options.
Benefits are reasonable implications of the features, not independent test claims.
Unsupported performance, medical, authenticity, waterproofing and compatibility
promises are not added. Important consumer limitations remain in the copy; detailed
supplier conflicts and procurement notes stay expandable beneath each description.

### Resolved supplier access
T70 (#27) and the Jisiyuan vertical mouse (#34) became readable on recheck. Their
attributes and packing data now replace the earlier missing-specification status.
See `data/supplier-recheck.json`. T70 has conflicting Bluetooth and runtime claims;
24-hour marketing is not treated as established playback time. The vertical-mouse
offer mixes power, connection and hand-orientation variants. Those distinctions are
preserved rather than combining the best features into one imaginary version.
The other 38 supplier extractions are retained from the earlier review; this pass
claims a fresh fetch only for the two previously blocked offers.

### Data and handoff
`description` is the current long consumer text. `product_details` stores full
structured extraction, with source URL, check date, extraction basis and verification
notes in dedicated fields. `description_word_count`, `description_tone`,
`description_audience` and `description_approach` describe the editorial treatment.
`data/long-product-descriptions.csv` is the current consumer-copy handoff.
`data/supplier-product-details.csv` includes all forty current extraction statuses.
Earlier brief descriptions and their CSV are archived historical copy; especially
the old blocked-page summaries must not supersede the current long descriptions.

Product Attributes and Packing are clearly distinguished from readable Product
Details prose. No image-only text was transcribed or OCRed, and no support/detail
images were added. All forty main images are retained. No sourcing prices, Jumia
references, shipping allowances, retail proposals or override controls were changed.
Author DAVE ADEX and Day 01 capacity of forty remain unchanged.
