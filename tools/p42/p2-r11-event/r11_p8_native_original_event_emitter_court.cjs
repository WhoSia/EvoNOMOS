'use strict';
const assert = require('node:assert/strict');
const EventEmitter = require('node:events').EventEmitter;
const EventEmitter3 = require(process.env.R11_P8_ORIGINAL_EVENTEMITTER3_DIR + '/index.js');

function observe(Emitter, name) {
  const old = new Emitter();
  let oldCalls = 0, value = null;
  old.on('tick', v => { oldCalls++; value = v; });
  const oldReturned = old.emit('tick', 2);
  assert.equal(oldReturned, true);
  assert.equal(oldCalls, 1);
  assert.equal(value, 2);

  const failures = [];
  const noHandler = new Emitter();
  let errored = false, result = null;
  try { result = noHandler.emit('error', new Error('bounded-research-error')); }
  catch (e) { errored = true; assert.equal(e.message, 'bounded-research-error'); }
  failures.push(errored);

  const meta = new Emitter();
  let metaCount = 0, observedEvent = null;
  meta.on('newListener', eventName => { metaCount++; observedEvent = eventName; });
  const before = metaCount;
  meta.on('ping', () => {});
  const autoMetaOnRegistration = metaCount > before && observedEvent === 'ping';

  const once = new Emitter();
  let onceCalls=0;
  once.once('only',() => onceCalls++);
  once.emit('only');once.emit('only');
  assert.equal(onceCalls, 1);

  const order = new Emitter();
  const observed=[];
  order.on('seq',()=>observed.push('A'));
  order.on('seq',()=>observed.push('B'));
  order.emit('seq');
  assert.deepEqual(observed,['A','B']);

  const resultObject = {
    source:name,
    old:{calls:oldCalls,value,emitter_return:oldReturned},
    error_unhandled:{throws:errored,return_if_not_thrown:result},
    newListener_on_subsequent_registration:autoMetaOnRegistration,
    once_calls:onceCalls,
    ordinary_listener_order:observed
  };
  const expected = name==='NodeCore'
      ? {throws:true,meta:true}
      : {throws:false,meta:false};
  assert.equal(errored,expected.throws,name + ' error contract');
  assert.equal(autoMetaOnRegistration,expected.meta,name + ' meta-event contract');
  if (name==='EventEmitter3') assert.equal(result,false);
  console.log('R11_P8_NATIVE_' + name.toUpperCase() + '_FORECAST_PASS');
  console.log(JSON.stringify(resultObject));
  return resultObject;
}
const node = observe(EventEmitter,'NodeCore');
const ee3 = observe(EventEmitter3,'EventEmitter3');
assert.equal(node.old.calls,ee3.old.calls);
assert.notEqual(node.error_unhandled.throws,ee3.error_unhandled.throws);
assert.notEqual(node.newListener_on_subsequent_registration,ee3.newListener_on_subsequent_registration);
console.log('R11_P8_TWO_ORIGINAL_EVENT_PARADIGM_OLD_CONTRACT_EQUIVALENCE_FUTURE_DEMAND_REVERSAL_PASS');
