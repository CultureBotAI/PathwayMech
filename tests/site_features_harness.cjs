/* Run the shipped theme and browse scripts against small DOM fixtures, without a browser. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const [script, scenario] = process.argv.slice(2);
const source = fs.readFileSync(script, 'utf8');

function element() {
  return {
    attributes: {}, events: {}, hidden: false, value: '',
    setAttribute(name, value) { this.attributes[name] = String(value); },
    getAttribute(name) { return this.attributes[name] ?? null; },
    addEventListener(name, callback) { this.events[name] = callback; },
    focus() {},
  };
}

// Theme: a fresh page per case, with the reader's saved choice and OS preference.
function themePage({saved = null, osDark = false} = {}) {
  const root = element();
  const button = element();
  const store = saved ? {'mech-theme': saved} : {};
  const ready = [];
  const context = {
    localStorage: {getItem: key => store[key] ?? null, setItem: (key, value) => { store[key] = value; }},
    window: {matchMedia: () => ({matches: osDark, addEventListener() {}})},
    document: {
      documentElement: root, readyState: 'loading',
      getElementById: id => (id === 'theme-toggle' ? button : null),
      addEventListener(name, callback) { assert.equal(name, 'DOMContentLoaded'); ready.push(callback); },
    },
  };
  vm.runInNewContext(source, context);
  const beforeParse = root.getAttribute('data-theme');
  ready.forEach(callback => callback());
  return {root, button, store, beforeParse, click: () => button.events.click()};
}

// A <select> that behaves like the browser's: a value no option carries selects nothing.
function select(values) {
  const control = element();
  control.options = values.map(value => ({value}));
  control.index = 0;
  Object.defineProperty(control, 'value', {
    get() { return control.index >= 0 ? control.options[control.index].value : ''; },
    set(value) { control.index = control.options.findIndex(option => option.value === String(value)); },
  });
  Object.defineProperty(control, 'selectedIndex', {get: () => control.index});
  return control;
}

const scenarios = {
  saved_choice_applies_before_the_page_parses() {
    const page = themePage({saved: 'dark', osDark: false});
    assert.equal(page.beforeParse, 'dark', 'the saved theme must be set before first paint');
    assert.equal(page.button.getAttribute('aria-pressed'), 'true');
    page.click();
    assert.equal(page.root.getAttribute('data-theme'), 'light');
    assert.equal(page.store['mech-theme'], 'light');
    assert.equal(page.button.getAttribute('aria-pressed'), 'false');
  },
  first_click_flips_the_os_theme() {
    const dark = themePage({osDark: true});
    assert.equal(dark.beforeParse, null, 'no choice means the OS preference applies');
    assert.equal(dark.button.getAttribute('aria-pressed'), 'true');
    dark.click();
    assert.equal(dark.root.getAttribute('data-theme'), 'light', 'OS dark: first click is light');
    assert.equal(dark.store['mech-theme'], 'light');
    const light = themePage({osDark: false});
    assert.equal(light.button.getAttribute('aria-pressed'), 'false');
    light.click();
    assert.equal(light.root.getAttribute('data-theme'), 'dark', 'OS light: first click is dark');
    assert.equal(light.store['mech-theme'], 'dark');
  },
  unknown_url_values_select_the_defaults() {
    const controls = {
      'pathway-search': element(), 'pathway-query': element(), 'pathway-status': element(),
      'pathway-empty': element(), 'pathway-list': {appendChild() {}},
      'pathway-type': select(['', 'amino-acid-biosynthesis']),
      'pathway-taxon': select(['', 'Escherichia coli']),
      'pathway-grounding': select(['', 'protein-grounded']),
      'pathway-sort': select(['label-asc', 'label-desc', 'type-asc']),
    };
    const rows = ['alpha', 'beta'].map(name => ({hidden: false, dataset: {
      search: name, label: name, id: 'X:' + name, edges: '1', type: 'amino-acid-biosynthesis',
      taxa: 'Escherichia coli', grounding: 'protein-grounded'}}));
    const ready = [];
    const location = {href: 'https://pathway.test/browse.html',
                      search: '?q=alph&type=10+mechanistic+edges&taxon=Escherichia+coli&sort=bogus'};
    const context = {
      URL, URLSearchParams,
      window: {location, addEventListener() {}},
      history: {replaceState() {}},
      document: {
        getElementById: id => controls[id],
        querySelectorAll: () => rows,
        addEventListener(name, callback) { assert.equal(name, 'DOMContentLoaded'); ready.push(callback); },
      },
    };
    vm.runInNewContext(source, context);
    ready.forEach(callback => callback());
    const type = controls['pathway-type'], sort = controls['pathway-sort'];
    assert.equal(type.selectedIndex, 0, 'a retired type value must select "All pathway types"');
    assert.equal(type.value, '');
    assert.equal(sort.value, 'label-asc', 'an unknown sort must fall back to the default order');
    assert.equal(controls['pathway-taxon'].value, 'Escherichia coli', 'a known value is restored');
    assert.equal(controls['pathway-query'].value, 'alph');
    assert.equal(rows[0].hidden, false);
    assert.equal(rows[1].hidden, true);
  },
};

scenarios[scenario]();
console.log(`Site feature passed: ${scenario}`);
