#!/usr/bin/env node
// Phase II-H: prospectively frozen, fidelity-first SQLite H equalization Court.
import assert from "node:assert/strict";
import fs from "node:fs";
const [input,output]=process.argv.slice(2);
if(!input)throw new Error("usage: node law-r1-p30-sqlite-verified-equalization-court.mjs <raw> [receipt]");
const x=JSON.parse(fs.readFileSync(input,"utf8"));
assert.equal(x.stage,"G8 LAW-R1-P30");
assert.equal(x.candidate,"SQLite verified sequence equalization");
assert.equal(x.source_commit_expected,"f3d536d37825302e31ed0eddd811c689f38f85a3");
assert.equal(x.fossil_uuid_expected,"c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33");
assert.equal(x.version,"3.46.1");
assert.equal(x.rounds,3);
assert.deepEqual(x.target_values,[0,7]);
assert.deepEqual(x.arm_order,["ROUND_{r}_HISTORY_0_TARGET_{t}","ROUND_{r}_HISTORY_1_TARGET_{t}"]);
assert.match(x.sqlite_binary_sha256,/^[0-9a-f]{64}$/);
assert.equal(x.claim_ceiling,"Local causal predictive repair only, not LAW-R2");
assert.equal(x.rows.length,12);
const byKey=new Map();
for(const row of x.rows){
 const {round,history,target_seq}=row;
 assert.ok(Number.isInteger(round)&&round>=0&&round<3);
 assert.equal(typeof history,"boolean");
 assert.ok(target_seq===0||target_seq===7);
 const arm="ROUND_"+round+"_HISTORY_"+Number(history)+"_TARGET_"+target_seq;
 assert.equal(row.arm,arm);
 assert.ok(!byKey.has(arm),"duplicate prospective arm");
 byKey.set(arm,row);
 const expectedBefore=history?[{"name":"events","seq":1}]:[];
 const expectedAfter=[{"name":"events","seq":target_seq}];
 assert.deepEqual(row.H_before,expectedBefore);
 assert.deepEqual(row.H_after,expectedAfter);
 assert.equal(row.treatment_branch,history?"UPDATE_IF_EXISTS":"INSERT_IF_MISSING");
 const expectedSql=history?
    "UPDATE sqlite_sequence SET seq="+target_seq+" WHERE name='events';":
    "INSERT INTO sqlite_sequence(name,seq) VALUES('events',"+target_seq+");";
 assert.equal(row.treatment_sql,expectedSql);
 assert.equal(row.fidelity_verified_before_future,true);
 assert.equal(row.fresh_cli_process_per_sql_operation,true);
 assert.deepEqual(row.before,row.after);
 const b=row.before;
 assert.deepEqual(b.visible,[]);
 assert.deepEqual(b.count,[{"n":0}]);
 assert.deepEqual(b.journal_mode,[{"journal_mode":"delete"}]);
 assert.deepEqual(b.foreign_keys,[{"foreign_keys":0}]);
 assert.deepEqual(b.read_uncommitted,[{"read_uncommitted":0}]);
 assert.ok(Array.isArray(b.schema));
 assert.equal(b.schema.length,2);
 assert.equal(b.schema.filter(t=>t.name==="events"&&t.type==="table"&&/AUTOINCREMENT/.test(t.sql)).length,1);
 assert.equal(b.schema.filter(t=>t.name==="sqlite_sequence"&&t.type==="table").length,1);
 assert.deepEqual(row.future,[{"id":target_seq+1}]);
}
for(let round=0;round<3;round++){
 for(const target of [0,7]){
  const a=byKey.get("ROUND_"+round+"_HISTORY_0_TARGET_"+target);
  const b=byKey.get("ROUND_"+round+"_HISTORY_1_TARGET_"+target);
  assert.ok(a&&b);
  assert.deepEqual(a.before,b.before);
  assert.deepEqual(a.H_after,b.H_after);
  assert.deepEqual(a.future,b.future);
 }
 const lo=byKey.get("ROUND_"+round+"_HISTORY_0_TARGET_0");
 const hi=byKey.get("ROUND_"+round+"_HISTORY_0_TARGET_7");
 assert.deepEqual(lo.before,hi.before);
 assert.notDeepEqual(lo.future,hi.future);
}
const receipt={
 stage:"G8 LAW-R1-P30",
 verdict:"PASS_SQLITE_FIDELITY_VERIFIED_SEQUENCE_EQUALIZATION__LOCAL_PREDICTIVE_RESCUE__LAW_R2_NOT_AUTHORIZED",
 source_commit:x.source_commit_expected,
 fossil_uuid:x.fossil_uuid_expected,
 sqlite_binary_sha256:x.sqlite_binary_sha256,
 measurements:x.rows.length,
 independently_reopened_operations:true,
 successfully_equalized_history_pairs:6,
 treatment_non_delivery_observations:0,
 history_pairs_with_divergence_after_same_H:0,
 prospectively_targeted_seq:[0,7],
 corresponding_future_ids:[1,8],
 raw_row_validation:true,
 no_external_universal_transport_claim:true,
 p30_closed:false,
 law_r2_authorized:false
};
console.log(JSON.stringify(receipt,null,2));
if(output)fs.writeFileSync(output,JSON.stringify(receipt,null,2)+"\n");
