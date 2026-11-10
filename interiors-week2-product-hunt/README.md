# Interior Designs — Week 2
**Author: DAVE ADEX** · 200 new supplier offers · five daily grids of 40

## Open the catalogue
Open `../interiors-week2-product-listings.html`. It is a standalone, offline HTML file with all 200 main JPEGs embedded. No external fonts, scripts or image servers are needed. Search covers all five days. The CSV button exports the complete 200-row shortlist. No ZIP was created.

## Evidence limitations — read before procurement
- All 200 source offer URLs are distinct and exclude the earlier Interior Designs catalogue's 200 URLs. A distinct supplier offer is not a guarantee of a distinct manufactured design; some suppliers offer similar products.
- The original Chinese title, public source price, catalogue URL and image association are retained. English names are editorial descriptions. Only individually supported original Latin brands are retained: **hy, NBC and BONGO**; all others are **Other**. Automatically translated brands are not adopted.
- Chromium inspected the saved public supplier catalogue DOM for **all 200 exact offer/image associations**. The images were decoded and visually reviewed. This is not a physical product inspection, an independently verified colour/pack choice, or confirmation that the image is first in the live detail gallery. Only one main image per offer is included; no support-image grid. Some supplier main images themselves depict multiple options or props.
- **21 supplier detail pages** were individually reviewed. Other records retain catalogue-level evidence and cautious buyer guidance, not invented detailed specifications.
- **9 conditional freight allocations: 3 with supplier folded-piece dimensions and 6 weight-only lower bounds. The remaining 191 are pending.** Source-option mismatches, implausible weights and generic multi-size weights were rejected. No sibling or Jumia weight was borrowed. A lower-bound `+` is not a full shipping estimate.
- Published normal-cargo planning tier: **USD20.50/kg + ₦1,500/kg**, within a consolidated 1–10kg batch. Dimensions use divisor6,000 where credible. Fractional allocations are not individually bookable parcel quotes. Carrier minima/rounding, protected packing, China inland transport, insurance, government duties/taxes and final-mile costs remain excluded or unresolved. Long rails and bulky foam may be expensive by volume. Obtain a fresh carrier quote.
- FX is a rounded editable **scenario**, USD/NGN1,350 and CNY/USD0.15, not verified current payment FX. The forwarder uses its own exchange rate. Published guide: https://dechaser.com/china-to-nigeria-shipping/ — checked27October2026.
- All **200 exact English product-name Jumia Nigeria searches returned access-blocked responses**. **19 family-market observations** provide related-category context for190 offers; the ten ring/eyelet offers have no usable comparator. **Zero equivalent matched SKUs** are claimed. Pack, size, material and product-type differences are stated. A Jumia index price is not a verified checkout price or availability guarantee.
- Source budget floor **¥5.20** and shipping allowance floor **₦2,000** affect proposals only. A ₦2,000 placeholder does not fill missing freight evidence. Sale and compare-at figures are proposals, not historical retail prices, real savings or confirmed landed costs. Starting source prices may apply to a smaller item, metre of fabric or different pack.
- Supplier dispatch language concerns mainland-China handling, not guaranteed Nigerian delivery or stock. Test compatibility, material/care, installation, label language, design permissions and safe use before purchase. No independent fire, acoustic, antimicrobial, food-contact, load or slip-resistance certification is asserted.

## Team modules
| Path | Responsibility |
|---|---|
| `data/evidence/selected.json` | Original observations and English editorial names |
| `data/evidence/detail-notes.json` | Individual offer facts, rejected packing and selected variants |
| `data/evidence/browser-inspection.json` | 200 exact DOM offer/image associations |
| `data/evidence/jumia-access.json` | 200 exact-name access attempts, queries and status |
| `data/evidence/freight-guide.json` | Published rates, exclusions and scenario assumptions |
| `data/market-observations.json` | Non-equivalent Jumia contexts and source citations |
| `data/guides.json` | Consumer-focused description sections by family |
| `data/settings.json` | Default pricing scenario;floors and currency inputs |
| `data/image-manifest.json` + `assets/images/` | Exactly200 required main JPEGs and provenance |
| `scripts/assemble.py` | Editorial/data assembly, conditional freight and proposals |
| `scripts/build.py` | Offline standalone HTML compiler |
| `templates/catalogue.html` | Document structure and transparent research disclosures |
| `assets/css/styles.css` | Responsive presentation |
| `assets/js/app.js` | Five grids, search, bounded proposal controls and CSV export |
| `scripts/validate.py` | Count, uniqueness, embedded-image and preservation checks |
| `scripts/browser-qa.cjs` | Real Chromium navigation, search, mobile and image checks |
| `data/products.json`, `data/products.csv` | Compiled product outputs |

### Rebuild from this project folder
```bash
python scripts/assemble.py
python scripts/build.py
python scripts/validate.py
```
The rebuild uses only Python standard-library modules. No research access or network is required. If changing FX/formula assumptions, update both `data/settings.json` and the explicitly labelled formula in `assets/js/app.js` and methodology copy. Do not overwrite observed prices with proposal floors.

Optional browser QA requires Node.js, Playwright and Chromium:
```bash
npm install playwright
npx playwright install chromium
node scripts/browser-qa.cjs
```
The structural report is `data/validation.json`;browser checks are `data/browser-qa.json`. Optional QA screenshots are disposable and not a required product asset.

## Preservation and workspace
Existing completed catalogue HTMLs were hash-checked unchanged. Required new and earlier Week2 main images remain. Raw research pages/duplicate research JSON may be losslessly gzip-compressed to conserve workspace;completed project inputs are readable and uncompressed. Optional replay helper, run from workspace root: `python research/restore_raw_sources.py interiors-week2`. Restoring raw sources is not necessary for the catalogue or rebuild and uses extra space. Do not restore previously authorised-deleted images or ZIPs.
