/* Run the shipped enhancement with a small DOM fixture, without a browser dependency. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

class Element {
  constructor({dataset = {}, attributes = {}, box = null} = {}) {
    this.dataset = dataset;
    this.attributes = attributes;
    this.box = box;
    this.style = {};
    this.hidden = false;
    this.value = '';
    this.textContent = '';
    this.events = new Map();
    this.classes = new Set();
    this.classList = {
      toggle: (name, enabled) => {
        if (enabled) this.classes.add(name);
        else this.classes.delete(name);
      },
      contains: name => this.classes.has(name),
    };
  }
  addEventListener(name, callback) {
    const callbacks = this.events.get(name) || [];
    this.events.set(name, [...callbacks, callback]);
  }
  emit(name, event = {}) {
    for (const callback of this.events.get(name) || []) callback.call(this, event);
  }
  getAttribute(name) { return this.attributes[name] ?? null; }
  getBBox() { assert(this.box, 'A selected node needs its actual SVG bounds'); return this.box; }
}

const maliciousLabel = '<img src=x onerror="alert(1)"> & <script>bad()</script>';
function fixture({missingSection = false, missingSvg = false, width = 1000} = {}) {
  const nodes = ['a', 'b', 'c', 'd'].map(id => new Element({
    dataset: {nodeId: id, nodeLabel: id === 'a' ? maliciousLabel : id.toUpperCase()},
    attributes: {href: '#component-' + id},
    box: {x: 250, y: 200, width: 100, height: 40},
  }));
  // Both directions, a self-loop, and nonincident edges must retain their identities.
  const edges = [['a', 'b'], ['b', 'a'], ['a', 'a'], ['b', 'c'], ['c', 'd']]
    .map(([subject, object], index) => new Element({
      dataset: {subject, object, predicate: 'has_output'},
      attributes: {href: '#mechanism-edge-' + (index + 1)},
    }));
  const svg = new Element({attributes: {width: String(width), height: '800'}});
  svg.querySelectorAll = selector => {
    if (selector === '.graph-node') return nodes;
    if (selector === '.graph-edge') return edges;
    throw new Error('Unexpected SVG query: ' + selector);
  };
  const viewport = new Element();
  Object.assign(viewport, {clientWidth: 500, clientHeight: 300, scrollLeft: 0, scrollTop: 0});
  const buttons = Object.fromEntries(['fit', 'zoom-in', 'zoom-out'].map(action =>
    [action, new Element({dataset: {graphAction: action}})]));
  const tools = new Element();
  tools.hidden = true;
  tools.querySelectorAll = selector => {
    assert.equal(selector, '[data-graph-action]');
    return Object.values(buttons);
  };
  const picker = new Element(), status = new Element();
  Object.defineProperty(status, 'innerHTML', {
    set() { throw new Error('Status must display labels as plain text, never HTML'); },
  });
  const nativeSize = new Element(), nativeLabel = new Element();
  nativeSize.id = 'graph-native-size';
  nativeSize.checked = true;
  const elements = {
    '.graph-viewport': viewport,
    '.pathway-network-svg': missingSvg ? null : svg,
    '.graph-tools': tools,
    '#graph-node-picker': picker,
    '.graph-status': status,
    '.graph-native-size': nativeSize,
    'label[for="graph-native-size"]': nativeLabel,
  };
  const section = new Element();
  section.querySelector = selector => elements[selector] ?? null;
  const document = {
    querySelector(selector) {
      assert.equal(selector, '.pathway-network');
      return missingSection ? null : section;
    },
  };
  const window = new Element();
  vm.runInNewContext(fs.readFileSync(process.argv[2], 'utf8'), {document, window});
  return {nodes, edges, svg, viewport, buttons, tools, picker, status, nativeSize, nativeLabel, window};
}

function close(actual, expected, message) {
  assert(Math.abs(actual - expected) < 1e-8, `${message}: expected ${expected}, got ${actual}`);
}
function size(f, scale) {
  close(parseFloat(f.svg.style.width), 1000 * scale, 'Displayed width');
  close(parseFloat(f.svg.style.height), 800 * scale, 'Displayed height');
}
function select(f, id) { f.picker.value = id; f.picker.emit('change'); }
function selected(f) { return f.nodes.filter(n => n.classList.contains('graph-selected')); }
function countSummary(f) {
  assert.match(f.status.textContent, /4 nodes/);
  assert.match(f.status.textContent, /5 relationships/);
}
function noSelection(f) {
  assert.equal(selected(f).length, 0);
  for (const item of [...f.nodes, ...f.edges]) {
    assert.equal(item.classList.contains('graph-muted'), false);
    assert.equal(item.classList.contains('graph-connected'), false);
  }
  assert(!f.status.textContent.includes('Highlighting'));
  countSummary(f);
}

const scenarios = {
  zoom_and_fit() {
    const f = fixture();
    size(f, 0.5);
    assert.equal(f.tools.hidden, false);
    assert.equal(f.nativeSize.hidden, true);
    assert.equal(f.nativeLabel.hidden, true);
    assert.equal(f.nativeSize.checked, false);
    countSummary(f);
    assert.match(f.status.textContent, /50%/);
    f.viewport.scrollLeft = 90;
    f.viewport.scrollTop = 35;
    const center = {x: (90 + 250) / 0.5, y: (35 + 150) / 0.5};
    f.buttons['zoom-in'].emit('click');
    size(f, 0.7);
    close((f.viewport.scrollLeft + 250) / 0.7, center.x, 'Zoom preserves horizontal center');
    close((f.viewport.scrollTop + 150) / 0.7, center.y, 'Zoom preserves vertical center');
    f.buttons['zoom-out'].emit('click');
    size(f, 0.5);
    close(f.viewport.scrollLeft, 90, 'Zoom out restores horizontal position');
    close(f.viewport.scrollTop, 35, 'Zoom out restores vertical position');
    f.viewport.clientWidth = 250;
    f.window.emit('resize');
    size(f, 0.5); // An explicit user zoom survives a viewport resize.
    f.buttons.fit.emit('click');
    size(f, 0.25);
    assert.equal(f.viewport.scrollLeft, 0);
    assert.equal(f.viewport.scrollTop, 0);
    f.viewport.clientWidth = 800;
    f.window.emit('resize');
    size(f, 0.8); // Fit mode continues following the available width.
    f.viewport.clientWidth = 1500;
    f.window.emit('resize');
    size(f, 1); // Fitting a small graph does not force enlargement.
  },
  zoom_limits() {
    const f = fixture();
    for (let i = 0; i < 30; i++) f.buttons['zoom-in'].emit('click');
    size(f, 3);
    for (let i = 0; i < 50; i++) f.buttons['zoom-out'].emit('click');
    size(f, 0.15);
    // A graph wider than the minimum manual zoom must still fit on a narrow screen.
    f.viewport.clientWidth = 50;
    f.buttons.fit.emit('click');
    size(f, 0.05);
    assert.match(f.status.textContent, /5%/);
  },
  directed_selection_preserves_graph() {
    const f = fixture();
    const originalNodes = [...f.nodes], originalEdges = [...f.edges];
    const links = [...f.nodes, ...f.edges].map(item => item.getAttribute('href'));
    select(f, 'a');
    assert.deepEqual(selected(f), [f.nodes[0]]);
    assert.deepEqual(f.edges.map(e => e.classList.contains('graph-connected')), [true, true, true, false, false]);
    assert.deepEqual(f.edges.map(e => e.classList.contains('graph-muted')), [false, false, false, true, true]);
    assert.deepEqual(f.nodes.map(n => n.classList.contains('graph-muted')), [false, false, true, true]);
    assert.match(f.status.textContent, /3 connected relationships/); // Count a self-loop once.
    assert(f.status.textContent.includes(maliciousLabel), 'A label is announced literally');
    countSummary(f);
    size(f, 1);
    close(f.viewport.scrollLeft + 250, 300, 'Selection centers on the actual node bounds');
    close(f.viewport.scrollTop + 150, 220, 'Selection centers vertically on the actual node bounds');
    assert.deepEqual(f.nodes, originalNodes);
    assert.deepEqual(f.edges, originalEdges);
    assert.deepEqual([...f.nodes, ...f.edges].map(item => item.getAttribute('href')), links);
    for (const item of [...f.nodes, ...f.edges]) {
      assert.equal(item.hidden, false, 'Highlighting must not remove graph content');
      assert.notEqual(item.style.display, 'none');
      assert.notEqual(item.style.visibility, 'hidden');
    }
    select(f, 'c');
    assert.deepEqual(selected(f), [f.nodes[2]]);
    assert.deepEqual(f.edges.map(e => e.classList.contains('graph-connected')), [false, false, false, true, true]);
    assert.deepEqual(f.nodes.map(n => n.classList.contains('graph-muted')), [true, false, false, false]);
    assert.match(f.status.textContent, /2 connected relationships/);
  },
  clear_and_escape() {
    const f = fixture();
    select(f, 'a');
    select(f, '');
    noSelection(f);
    select(f, 'c');
    f.viewport.emit('keydown', {key: 'Enter'});
    assert.deepEqual(selected(f), [f.nodes[2]]);
    f.viewport.emit('keydown', {key: 'Escape'});
    assert.equal(f.picker.value, '');
    noSelection(f);
    f.viewport.emit('keydown', {key: 'Escape'});
    noSelection(f);
  },
  absent_or_invalid_graph() {
    for (const options of [{missingSection: true}, {missingSvg: true}, {width: 0}]) {
      const f = fixture(options);
      assert.equal(f.tools.hidden, true, 'Unavailable enhancement controls stay hidden');
      assert.equal(f.svg.style.width, undefined);
      assert.equal(f.nativeSize.hidden, false, 'The fallback stays available');
      assert.equal(f.buttons.fit.events.size, 0);
    }
  },
};
const name = process.argv[3];
assert(Object.hasOwn(scenarios, name), 'Unknown graph interaction scenario: ' + name);
scenarios[name]();
console.log('Graph interaction passed: ' + name);
