const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const contract = JSON.parse(fs.readFileSync('evonomos-media-contract.json', 'utf8'));
const manifestSource = fs.readFileSync('media-manifest.js', 'utf8');
const scriptSource = fs.readFileSync('script.js', 'utf8');

function catalog(label) {
  return {
    hero: {
      mode: 'real',
      src: `/${label}.webp`,
      alt: label,
      caption: label
    }
  };
}

function boot(mode, { includeAlternate = true } = {}) {
  const document = {
    documentElement: { dataset: {} },
    querySelector: () => null,
    querySelectorAll: () => []
  };
  const storage = new Map();
  const localStorage = {
    getItem: key => storage.get(key) ?? null,
    setItem: (key, value) => storage.set(key, String(value))
  };
  const window = { scrollY: 0 };
  const context = {
    window,
    document,
    localStorage,
    matchMedia: () => ({ matches: true }),
    addEventListener: () => {},
    Image: class {},
    console
  };
  window.window = window;
  window.document = document;
  window.localStorage = localStorage;
  vm.createContext(context);
  vm.runInContext(manifestSource, context, { filename: 'media-manifest.js' });

  const canonical = window.KODO_MEDIA;
  window.KODO_MEDIA_PREVIEW = includeAlternate ? catalog('preview') : undefined;
  window.KODO_MEDIA_STAGING = includeAlternate ? catalog('staging') : undefined;
  window.KODO_MEDIA_MODE = mode;

  vm.runInContext(scriptSource, context, { filename: 'script.js' });
  assert.equal(typeof window.KODO_RESOLVE_MEDIA, 'function', 'resolver contract must be exposed');
  return { window, canonical };
}

function resolvedCaption(mode, options) {
  const { window, canonical } = boot(mode, options);
  const resolved = window.KODO_RESOLVE_MEDIA();
  return { caption: resolved?.hero?.caption ?? null, canonicalCaption: canonical?.hero?.caption ?? null };
}

{
  const r = resolvedCaption(undefined);
  assert.equal(r.caption, r.canonicalCaption, 'default mode must resolve canonical catalog');
}

{
  const r = resolvedCaption(contract.alternate_label);
  assert.equal(r.caption, contract.alternate_label, 'current alternate label must resolve alternate catalog');
}

{
  const r = resolvedCaption(contract.alternate_label, { includeAlternate: false });
  assert.equal(r.caption, r.canonicalCaption, 'missing alternate catalog must fall back to canonical');
}

{
  const r = resolvedCaption('unknown-mode');
  assert.equal(r.caption, r.canonicalCaption, 'unknown mode must fall back to canonical');
}

if (contract.retired_label) {
  const r = resolvedCaption(contract.retired_label);
  assert.equal(r.caption, r.canonicalCaption, 'retired label must no longer select alternate catalog');
}

console.log(JSON.stringify({
  status: 'PASS',
  alternate_label: contract.alternate_label,
  retired_label: contract.retired_label
}));
