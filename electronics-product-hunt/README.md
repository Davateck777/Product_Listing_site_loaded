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
Five products. P9 has 1 main plus 9 support images, supplied by the user; other products have a main image and pending-support notice. Galleries are visible grids. Prices are carried forward, not newly revalidated. Product data contains original remote image URLs; displayed copies are local.

## Important verification checks
Confirm exact offer/variant, quote, MOQ, image rights, package weight, landed costs and certificate scope before publication. P9 attributes are supplier-stated. Compare-at prices and discounts are proposals, not proven historical pricing. Enter your actual exchange rate before evaluating costs.

## Comments and code sections
HTML regions have descriptive comments. CSS sections and JavaScript functions explain their purpose; JavaScript validation, calculation and download steps have inline comments. JSON does not support comments, so its purpose is documented here and in `products.js`.

## Changes made in the browser
Apply overrides before exporting. The export captures the current in-memory product records. Browser changes are not automatically saved into these project files.
