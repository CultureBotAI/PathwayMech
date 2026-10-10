/* Progressive enhancement: the complete SVG and evidence links work without JS. */
(function () {
  'use strict';
  const section = document.querySelector('.pathway-network');
  if (!section) return;
  const viewport = section.querySelector('.graph-viewport');
  const svg = section.querySelector('.pathway-network-svg');
  const tools = section.querySelector('.graph-tools');
  if (!viewport || !svg || !tools) return;

  const width = Number(svg.getAttribute('width'));
  const height = Number(svg.getAttribute('height'));
  if (!(width > 0 && height > 0)) return;
  const nodes = Array.from(svg.querySelectorAll('.graph-node'));
  const edges = Array.from(svg.querySelectorAll('.graph-edge'));
  const picker = section.querySelector('#graph-node-picker');
  const status = section.querySelector('.graph-status');
  let scale = 1;
  let fitted = true;
  let selected = '';

  function fitScale() { return Math.min(1, Math.max(1, viewport.clientWidth) / width); }
  function resize(next, center) {
    scale = Math.min(3, Math.max(Math.min(0.15, fitScale()), next));
    svg.style.width = (width * scale) + 'px';
    svg.style.height = (height * scale) + 'px';
    if (center) {
      viewport.scrollLeft = center.x * scale - viewport.clientWidth / 2;
      viewport.scrollTop = center.y * scale - viewport.clientHeight / 2;
    }
  }
  function announce() {
    const node = nodes.find(item => item.dataset.nodeId === selected);
    const incident = edges.filter(edge =>
      edge.dataset.subject === selected || edge.dataset.object === selected);
    status.textContent = nodes.length + ' nodes · ' + edges.length + ' relationships · ' +
      Math.round(scale * 100) + '% size' + (node ?
        '. Highlighting ' + node.dataset.nodeLabel + ': ' + incident.length +
        ' connected relationships. All relationships remain in the diagram.' : '.');
  }
  function fit() {
    fitted = true;
    resize(fitScale());
    viewport.scrollLeft = 0;
    viewport.scrollTop = 0;
    announce();
  }
  function highlight(identifier) {
    selected = identifier;
    const connected = new Set([identifier]);
    edges.forEach(edge => {
      const incident = edge.dataset.subject === identifier || edge.dataset.object === identifier;
      edge.classList.toggle('graph-connected', Boolean(identifier) && incident);
      edge.classList.toggle('graph-muted', Boolean(identifier) && !incident);
      if (incident) { connected.add(edge.dataset.subject); connected.add(edge.dataset.object); }
    });
    nodes.forEach(node => {
      node.classList.toggle('graph-selected', node.dataset.nodeId === identifier);
      node.classList.toggle('graph-muted', Boolean(identifier) && !connected.has(node.dataset.nodeId));
    });
    const node = nodes.find(item => item.dataset.nodeId === identifier);
    if (node) {
      fitted = false;
      const box = node.getBBox();
      resize(Math.max(1, scale), {x: box.x + box.width / 2, y: box.y + box.height / 2});
    }
    announce();
  }
  tools.querySelectorAll('[data-graph-action]').forEach(button => {
    button.addEventListener('click', function () {
      const action = button.dataset.graphAction;
      if (action === 'fit') { fit(); return; }
      const center = {
        x: (viewport.scrollLeft + viewport.clientWidth / 2) / scale,
        y: (viewport.scrollTop + viewport.clientHeight / 2) / scale
      };
      fitted = false;
      resize(scale * (action === 'zoom-in' ? 1.4 : 1 / 1.4), center);
      announce();
    });
  });
  if (picker) picker.addEventListener('change', function () { highlight(picker.value); });
  viewport.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      if (picker) picker.value = '';
      highlight('');
    }
  });
  window.addEventListener('resize', function () { if (fitted) fit(); });
  const nativeSize = section.querySelector('.graph-native-size');
  if (nativeSize) {
    nativeSize.checked = false;
    nativeSize.hidden = true;
    const label = section.querySelector('label[for="' + nativeSize.id + '"]');
    if (label) label.hidden = true;
  }
  tools.hidden = false;
  fit();
}());
