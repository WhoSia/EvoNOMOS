'use strict';

const telemetryStore = require('../lib/telemetryStore');
const DashboardServer = require('../lib/dashboardServer');

let capturedUiInstance;

jest.mock('@homebridge/plugin-ui-utils', () => ({
  HomebridgePluginUiServer: class {
    constructor() { capturedUiInstance = this; this._routes = {}; }
    onRequest(route, handler) { this._routes[route] = handler; }
    ready() {}
  },
}));

jest.mock('../lib/nutClient', () => ({ queryNUT: jest.fn() }));
require('../homebridge-ui/server');

const usableOlder = {
  t: '2026-08-01T00:00:00.000Z',
  inV: 0,
  outV: null,
  bat: null,
  load: null,
  runtime: null,
};
const usableNewer = {
  t: '2026-08-01T00:01:00.000Z',
  inV: null,
  outV: 229,
  bat: null,
  load: null,
  runtime: null,
};
const allNull = {
  t: '2026-08-01T00:02:00.000Z',
  inV: null,
  outV: null,
  bat: null,
  load: null,
  runtime: null,
};

function standaloneWith(points) {
  jest.spyOn(telemetryStore, 'readHistory').mockReturnValue(points);
  const server = new DashboardServer({
    storagePath: '/tmp/evonomos-wc2',
    upsNames: ['ups'],
    log: { info() {}, error() {} },
  });
  return server._lastKnownGoodFor('ups');
}

function uiWith(points) {
  jest.spyOn(telemetryStore, 'readHistory').mockReturnValue(points);
  return capturedUiInstance._lastKnownGoodFor('/tmp/evonomos-wc2', 'ups');
}

function assertContract(read) {
  expect(read([usableOlder, allNull])).toEqual(usableOlder);
  jest.restoreAllMocks();
  expect(read([usableOlder, usableNewer, allNull])).toEqual(usableNewer);
  jest.restoreAllMocks();
  expect(read([allNull, { ...allNull, t: '2026-08-01T00:03:00.000Z' }])).toBeNull();
  jest.restoreAllMocks();
  expect(read([usableOlder])).toEqual(usableOlder); // numeric zero is meaningful
}

afterEach(() => {
  jest.restoreAllMocks();
});

describe('EvoNOMOS WC2 phase0 standalone last-known-good contract', () => {
  test('skips trailing all-null samples, selects newest usable, and accepts numeric zero', () => {
    assertContract(standaloneWith);
  });
});

if (process.env.EVONOMOS_WC2_PHASE === 'phase1') {
  describe('EvoNOMOS WC2 phase1 Homebridge UI parity contract', () => {
    test('matches the standalone last-known-good semantics', () => {
      assertContract(uiWith);
    });
  });
}
