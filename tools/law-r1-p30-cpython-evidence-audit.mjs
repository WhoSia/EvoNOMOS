#!/usr/bin/env node
// G8 LAW-R1-P30: independent audit of raw evidence, NOT a replacement for the frozen Court.
import assert from "node:assert/strict";
import fs from "node:fs";

const path=process.argv[2];
if (!path) throw new Error("usage: node law-r1-p30-cpython-evidence-audit.mjs <probe-json> [receipt-json]");
const r=JSON.parse(fs.readFileSync(path,"utf8"));
const a=r.arm_a,b=r.arm_b;
function requireShape(arm,label) {
  assert.ok(arm && typeof arm==="object",label);
  assert.ok(arm.before && arm.future,label+" measurements");
  const p=arm.before;
  assert.equal(p.Q,1);
  assert.equal(p.R,"cpython-codecs-utf8-incremental");
  assert.deepEqual(p.G,[1,1,1,1]);
  assert.ok(Number.isSafeInteger(p.H_pending_length)&&p.H_pending_length>=0);
  assert.match(p.H_pending_hex,/^(?:[0-9a-f]{2})*$/);
  assert.equal(p.H_pending_hex.length,p.H_pending_length*2);
  assert.ok(Number.isSafeInteger(p.H_flag));
  assert.equal(typeof p.O_now,"string");
  assert.equal(typeof arm.future.ok,"number");
  assert.ok(arm.future.ok===0||arm.future.ok===1);
  if(arm.future.ok===1){
    assert.equal(typeof arm.future.unicode,"string");
    assert.equal(typeof arm.future.utf8,"string");
    assert.match(arm.future.utf8,/^(?:[0-9a-f]{2})*$/);
    assert.equal(Buffer.from(arm.future.unicode,"utf8").toString("hex"),arm.future.utf8);
  } else {
    assert.equal(arm.future.error,"UnicodeDecodeError");
  }
}
requireShape(a,"arm_a");requireShape(b,"arm_b");
assert.equal(r.stage,"G8 LAW-R1-P30");
assert.equal(r.candidate,"CPython UTF-8 incremental decoder");
assert.equal(r.implementation,"CPython");
assert.match(r.runtime,/^3\.12\.12(?:\s|$)/);
assert.equal(a.before.H_pending_hex,"c2");
assert.equal(b.before.H_pending_hex,"c3");
const coarse=x=>[x.Q,x.R,x.G,x.H_pending_length];
const equal=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const recalculated={
 current_equal:a.before.O_now===""&&b.before.O_now==="",
 same_W:equal(coarse(a.before),coarse(b.before)),
 future_different:!equal(a.future,b.future),
 prospective_pending_content_separates:a.before.H_pending_hex!==b.before.H_pending_hex
};
for (const [k,value] of Object.entries(recalculated)) assert.equal(r[k],value,"untrusted summary mismatch: "+k);
assert.equal(a.future.ok,1);
assert.equal(b.future.ok,1);
assert.equal(a.future.utf8,"c2a9");
assert.equal(b.future.utf8,"c3a9");
assert.ok(Object.values(recalculated).every(Boolean));
const receipt={
 status:"PASS_RAW_EVIDENCE_INTEGRITY",
 candidate:"CPython v3.12.12 UTF-8 temporal split",
 source_commit:"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5",
 exact_runtime_checked:true,
 raw_field_recomputation:true,
 matched_coarse_state:true,
 matched_current_output:true,
 divergent_future_output:true,
 prospective_pending_content_rescue:true,
 prior_frozen_court_untouched:true,
 law_r2_authorized:false
};
console.log(JSON.stringify(receipt,null,2));
if(process.argv[3])fs.writeFileSync(process.argv[3],JSON.stringify(receipt,null,2)+"\n");
