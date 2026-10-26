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

// A map page: the controls its script reads, a canvas stub, and the data table.
function node(tag) {
  const el = element();
  el.tagName = tag.toUpperCase();
  el.children = [];
  el.appendChild = child => { el.children.push(child); return child; };
  el.replaceChildren = (...nodes) => {
    el.children = nodes.flatMap(n => (n.isFragment ? n.children : [n]));
  };
  Object.defineProperty(el, 'text', {get() {
    return el.children.length ? el.children.map(c => c.text ?? c.textContent).join('') : el.textContent;
  }});
  return el;
}
function mapPage(prefix, payload, values = {}) {
  const ids = {};
  const get = id => (ids[id] ||= Object.assign(node('div'), {value: values[id] ?? ''}));
  get(`${prefix === 'map' ? 'corpus' : 'seq'}-map-data`).textContent = JSON.stringify(payload);
  Object.assign(get(`${prefix}-canvas`), {width: 920, height: 620,
    getContext: () => new Proxy({}, {get: (t, k) => (k in t ? t[k] : () => {}), set: (t, k, v) => { t[k] = v; return true; }}),
    getBoundingClientRect: () => ({left: 0, top: 0, width: 920, height: 620})});
  get(`${prefix}-table`).open = false;
  const ready = [];
  const context = {
    URL, URLSearchParams, Math, JSON, Number, String, Array, Map,
    window: {location: {href: `https://pathway.test/${prefix}.html`, search: ''}, addEventListener() {}},
    history: {replaceState() {}},
    document: {
      getElementById: get,
      createElement: tag => node(tag),
      createDocumentFragment: () => Object.assign(node('fragment'), {isFragment: true}),
      createTextNode: text => ({textContent: text, text}),
      addEventListener(name, callback) { assert.equal(name, 'DOMContentLoaded'); ready.push(callback); },
    },
  };
  vm.runInNewContext(source, context);
  ready.forEach(callback => callback());
  const rows = () => get(`${prefix}-table-body`).children;
  const open = () => { get(`${prefix}-table`).open = true; get(`${prefix}-table`).events.toggle(); };
  return {get, rows, open};
}
const MARKUP = '<img src=x onerror=alert(1)>';

const scenarios = {
  map_table_lists_the_plotted_records_and_follows_the_search() {
    const point = (id, label, url) => ({id, label, url, x: 0.5, y: 0.5, pathway_type: 'cofactor-biosynthesis',
      top_taxon: 'E. coli', taxa: ['E. coli'], has_proteins: false});
    const page = mapPage('map', {points: [point('GO:1', MARKUP, 'records/GO_1.html'),
      point('GO:2', 'unpublished pathway', ''), point('GO:3', 'thiamin biosynthesis', 'records/GO_3.html')]});
    assert.equal(page.rows().length, 0, 'rows are built only when the disclosure opens');
    page.get('map-query').value = 'pathway';
    page.get('map-query').events.input();
    assert.equal(page.rows().length, 0, 'filtering a closed table builds no rows');
    page.get('map-query').value = '';
    page.get('map-query').events.input();
    page.open();
    assert.equal(page.rows().length, 3);
    assert.deepEqual(page.get('map-table-head').children[0].children.map(c => c.textContent),
      ['Pathway', 'Identifier', 'Pathway class', 'Primary taxon']);
    const [first, second] = page.rows();
    assert.equal(first.children[0].tagName, 'TH');
    const link = first.children[0].children[0];
    assert.equal(link.tagName, 'A');
    assert.equal(link.href, 'records/GO_1.html');
    assert.equal(link.textContent, MARKUP, 'a label is set as text, never parsed as markup');
    assert.equal(second.children[0].children[0].tagName, undefined, 'no page, no link');
    page.get('map-query').value = 'thiamin';
    page.get('map-query').events.input();
    assert.equal(page.rows().length, 1, 'the table follows the search');
    assert.equal(page.rows()[0].children[0].children[0].href, 'records/GO_3.html');
    assert.equal(page.get('map-table-count').textContent, '1 of 3 plotted pathways, as filtered above.');
  },
  sequence_table_links_each_proteins_pathways() {
    const protein = {id: 'UniProtKB:P1', label: 'enzyme', x: 0.4, y: 0.4, pathway_type: 'c', taxon: 'E. coli',
      taxa: ['E. coli'], pathway_labels: ['first pathway', 'unpublished', 'third pathway'],
      pathway_urls: ['records/A.html', '', 'records/C.html'], url: 'records/A.html'};
    const page = mapPage('seq', {proteins: [protein], pathways: []}, {'seq-mode': 'proteins', 'seq-color': 'pathway_type'});
    page.open();
    assert.equal(page.rows().length, 1);
    const cells = page.rows()[0].children;
    assert.deepEqual(page.get('seq-table-head').children[0].children.map(c => c.textContent),
      ['Protein', 'UniProtKB', 'Organism', 'Pathway records']);
    const links = cells[3].children.filter(c => c.tagName === 'A');
    assert.deepEqual(links.map(a => [a.textContent, a.href]),
      [['first pathway', 'records/A.html'], ['third pathway', 'records/C.html']]);
    assert.equal(cells[3].text, 'first pathway, unpublished, third pathway');
  },
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
