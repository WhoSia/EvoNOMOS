#!/usr/bin/env node
// Independent raw-evidence Court for prospective SQLite 3.46.1 durable-history
// experiment. Do not trust precomputed similarity or outcome flags.
import assert from "node:assert/strict";
import fs from "node:fs";

const [rawPath,receiptPath]=process.argv.slice(2);
if(!rawPath) throw new Error("usage: node law-r1-p30-sqlite-history-court.mjs <raw-json> [receipt-json]");
const raw=JSON.parse(fs.readFileSync(rawPath,"utf8"));
assert.equal(raw.stage,"G8 LAW-R1-P30");
assert.equal(raw.candidate,"SQLite durable history predictive collision");
assert.equal(raw.expected_sqlite_source_commit,"f3d536d37825302e31ed0eddd811c689f38f85a3");
assert.equal(raw.observed_sqlite_version,"3.46.1");
assert.equal(raw.rounds,3);
assert.deepEqual(raw.arm_order,["AUTO_FRESH","AUTO_HISTORY","ROWID_FRESH","ROWID_HISTORY"]);
assert.match(raw.source_binary_sha256,/^[0-9a-f]{64}$/);
assert.equal(raw.rows.length,12);
assert.equal(raw.evidence_note,"Each SQL statement is a new sqlite3 process against a file database. Current view is captured before future INSERT.");

const expectedFuture={"AUTO_FRESH":1,"AUTO_HISTORY":2,"ROWID_FRESH":1,"ROWID_HISTORY":1};
const autoPattern=/AUTOINCREMENT/;
const seen=new Set();
const records=[];
for(const row of raw.rows){
 assert.ok(Number.isInteger(row.round)&&row.round>=0&&row.round<3);
 assert.ok(Object.hasOwn(expectedFuture,row.arm));
 const pairName=(row.autoincrement?"AUTO":"ROWID")+(row.history?"_HISTORY":"_FRESH");
 assert.equal(row.arm,pairName);
 assert.equal(row.reopened_process_per_operation,true);
 const key=row.round+":"+row.arm;
 assert.ok(!seen.has(key),"duplicate round/arm");
 seen.add(key);
 const b=row.before;
 assert.equal(b.Q,1);
 assert.equal(b.R,"exact-source-sqlite3-file-cli");
 assert.deepEqual(b.O_now,[]);
 assert.deepEqual(b.G.visible_rows,[]);
 assert.deepEqual(b.G.row_count,[{"n":0}]);
 assert.equal(b.G.autoincrement,row.autoincrement);
 assert.equal(b.G.intervention_sql,"INSERT INTO events(note) VALUES ('probe') RETURNING id;");
 assert.deepEqual(b.G.journal_mode,[{"journal_mode":"delete"}]);
 assert.deepEqual(b.G.foreign_keys,[{"foreign_keys":0}]);
 assert.deepEqual(b.G.read_uncommitted,[{"read_uncommitted":0}]);
 assert.ok(Array.isArray(b.G.schema));
 const event=b.G.schema.find(x=>x.name==="events");
 assert.ok(event);
 assert.equal(event.type,"table");
 assert.equal(event.tbl_name,"events");
 assert.equal(typeof event.sql,"string");
 assert.equal(autoPattern.test(event.sql),row.autoincrement);
 assert.equal(b.G.schema.some(x=>x.name==="sqlite_sequence"),row.autoincrement);
 assert.equal(b.G.schema.length,row.autoincrement?2:1);
 if(row.autoincrement){
   assert.deepEqual(row.H_sequence,row.history?[{"name":"events","seq":1}]:[]);
 }else{
   assert.equal(row.H_sequence,null);
 }
 assert.deepEqual(row.future,[{"id":expectedFuture[row.arm]}]);
 records.push(row);
}

for(let round=0;round<3;round++){
 const group=records.filter(x=>x.round===round);
 assert.equal(group.length,4);
 for(const auto of [true,false]){
  const fresh=group.find(x=>x.autoincrement===auto&&!x.history);
  const history=group.find(x=>x.autoincrement===auto&&x.history);
  assert.ok(fresh&&history);
  // No route or structured-G change is permitted within the compared pair.
  assert.deepEqual(fresh.before,history.before);
  if(auto){
   assert.notDeepEqual(fresh.future,history.future);
   assert.notDeepEqual(fresh.H_sequence,history.H_sequence);
  } else {
   assert.deepEqual(fresh.future,history.future);
   assert.deepEqual(fresh.H_sequence,history.H_sequence);
  }
 }
}
const verdict={
 stage:"G8 LAW-R1-P30",
 verdict:"PASS_SQLITE_DURABLE_PREDICTIVE_COLLISION__AUTOINCREMENT_HISTORY_GATED__PROSPECTIVE_SEQUENCE_RESCUE__LAW_R2_NOT_AUTHORIZED",
 sqlite_version:"3.46.1",
 rounds:3,
 measurements:12,
 matched_visible_state_pairs:6,
 prospective_persistent_history_collisions:3,
 rowid_negative_control_equalities:3,
 preserved_hidden_coordinate:"sqlite_sequence(name,seq) system-table row presence and seq",
 independently_reopened_cli_processes:true,
 source_binary_sha256:raw.source_binary_sha256,
 raw_rows_revalidated:true,
 distinct_semantic_mechanism_from_UTF8_decoder:true,
 shared_unique_hidden_coordinate_across_mechanisms:false,
 law_r2_authorized:false,p30_closed:false
};
console.log(JSON.stringify(verdict,null,2));
if(receiptPath)fs.writeFileSync(receiptPath,JSON.stringify(verdict,null,2)+"\n");
