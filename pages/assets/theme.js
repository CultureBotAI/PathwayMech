/* The one theme control for every page. Loaded in <head> without defer, so a
 * saved choice is on <html data-theme> before the first paint. Without a saved
 * choice the operating system's preference applies. The palettes themselves
 * live in style.css and pathway-network.css. */
(function () {
  'use strict';
  var KEY = 'mech-theme';
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem(KEY);
    if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
  } catch (e) {}

  function osDark() {
    return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }
  function current() {
    var chosen = root.getAttribute('data-theme');
    return chosen === 'dark' || chosen === 'light' ? chosen : (osDark() ? 'dark' : 'light');
  }
  function wire() {
    var button = document.getElementById('theme-toggle');
    if (!button) return;
    function show() { button.setAttribute('aria-pressed', current() === 'dark' ? 'true' : 'false'); }
    show();
    button.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      show();
    });
    if (window.matchMedia) {
      try {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', show);
      } catch (e) {}
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire);
  else wire();
}());
