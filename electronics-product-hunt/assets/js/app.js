/** CURRENCY FORMATTING — Render whole-naira amounts consistently. */
const money = value => '₦' + value.toLocaleString('en-NG', {
  maximumFractionDigits: 0
});

/** BATCH OVERRIDES — Validate inputs, preserve original source prices,
 * replace shipping costs and refresh the cost check on each product card.
 * This estimate excludes unverified fees and must not be called net profit.
 */
function apply() {
  const floorInput = document.getElementById('floor');
  const shipInput = document.getElementById('ship');
  const rateInput = document.getElementById('fx');
  const floor = Number(floorInput.value);
  const shipping = Number(shipInput.value);
  const rate = Number(rateInput.value);

  // Reject invalid overrides before changing any product records.
  if (!Number.isFinite(floor) || floor < 5.2 ||
      !Number.isFinite(shipping) || shipping < 2000 ||
      (rateInput.value !== '' && (!Number.isFinite(rate) || rate <= 0))) {
    alert('Use a source floor of at least ¥5.20, shipping of at least ₦2,000, and a positive exchange rate (or leave the rate blank).');
    return;
  }

  // Update the editable data and matching card, without changing source evidence.
  products.forEach((product, index) => {
    product.price_override_cny = Math.max(product.source_price_cny, floor);
    product.shipping_override_ngn = shipping;
    const card = document.getElementById('p' + index);
    card.querySelector('.po').textContent = '¥' + product.price_override_cny.toFixed(2);
    card.querySelector('.so').textContent = money(shipping);
    const cost = product.price_override_cny * rate + shipping;
    const balance = product.sale_ngn == null ? null : product.sale_ngn - cost;
    card.querySelector('.econ').textContent = rate > 0
      ? balance == null ? 'Indicative sourcing cost: ' + money(cost) + ' — Jumia comparison and retail price pending.' : 'Indicative cost: ' + money(cost) + ' · Retail less indicative cost: ' +
        money(balance) + (balance <= 0
          ? ' — NOT VIABLE at these inputs.'
          : ' — before unverified fees; not net profit.')
      : 'Enter your actual exchange rate above to test cost viability.';
  });
}

/** JSON EXPORT — Download the current in-memory records and applied overrides.
 * Changes are not saved to disk automatically; use this export to keep them.
 */
function download() {
  const payload = {
    author: 'DAVE ADEX',
    products_per_day: 40,
    image_policy: 'main-image-only',
    research_date: '2026-10-27',
    status: 'draft',
    exchange_rate_ngn_per_cny: Number(document.getElementById('fx').value) || null,
    products
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], {
    type: 'application/json'
  });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'electronics-listing-drafts.json';
  link.click();
  // Release the temporary download URL after the browser starts the transfer.
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
