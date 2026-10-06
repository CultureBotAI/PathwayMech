const assert = require('node:assert/strict'), fs = require('node:fs'), vm = require('node:vm');
const localeLower = String.prototype.toLocaleLowerCase;
String.prototype.toLocaleLowerCase = function () { return localeLower.call(this, 'tr'); };
function element(text = '') { return {textContent: text, hidden: false, value: '', events: {},
  addEventListener(name, fn) { this.events[name] = fn; }, focus() { this.focused = true; }}; }
const rows = [element('CHEBI:42 Compound'), element('CHEBI:99 Other')];
rows.forEach(row => { row.dataset = {search: row.textContent}; });
const group = {querySelectorAll() { return rows; }, hidden: false};
const elements = Object.fromEntries(['pathway-query','pathway-status','pathway-empty','pathway-search'].map(id => [id, element()]));
const ready = [], lifecycle = {};
global.window = {location: {href: 'https://pathway.test/browse.html', search: ''},
  addEventListener(name, fn) { lifecycle[name] = fn; }};
global.history = {replaceState(_state, _title, url) {
  window.location.href = url.href; window.location.search = url.search;
}};
global.document = {getElementById(id) { return elements[id]; },
  querySelectorAll(selector) { return selector === '.browse-group' ? [group] : rows; },
  addEventListener(name, fn) { assert.equal(name, 'DOMContentLoaded'); ready.push(fn); }};
vm.runInThisContext(fs.readFileSync(process.argv[2], 'utf8'));
ready.forEach(fn => fn());
const query = elements['pathway-query'], form = elements['pathway-search'];
query.value = 'chebi:42'; query.events.input();
assert.equal(rows[0].hidden, false, 'ASCII identifiers must match in every user locale');
assert.equal(rows[1].hidden, true);
query.value = '<script>alert(1)</script>'; query.events.input();
assert(rows.every(row => row.hidden)); assert.equal(elements['pathway-empty'].hidden, false);
form.events.reset({preventDefault() {}});
assert(rows.every(row => !row.hidden)); assert.equal(query.value, ''); assert.equal(query.focused, true);
window.location.search = '?q=chebi%3A42'; query.value = ''; lifecycle.pageshow();
assert.equal(query.value, 'chebi:42'); assert.equal(rows[1].hidden, true);
console.log('Literal locale-independent search and reset passed');
