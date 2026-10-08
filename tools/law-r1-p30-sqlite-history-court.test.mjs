#!/usr/bin/env node
// Execute this AFTER a raw exact-source SQLite probe. Generated mutations are
// deliberately invalid and must never be confused with world observations.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import {spawnSync} from "node:child_process";
const source=process.argv[2];
if(!source)throw new Error("usage: node law-r1-p30-sqlite-history-court.test.mjs <raw-json>");
const baseline=JSON.parse(fs.readFileSync(source,"utf8"));
const temp=fs.mkdtempSync(path.join(os.tmpdir(),"p30-sqlite-court-"));
const fixture=path.join(temp,"corrupted.json");
const court="tools/law-r1-p30-sqlite-history-court.mjs";
function check(obj){
 fs.writeFileSync(fixture,JSON.stringify(obj));
 return spawnSync(process.execPath,[court,fixture],{encoding:"utf8"});
}
try{
 const good=check(baseline);
 assert.equal(good.status,0,"exact-source baseline refused: "+good.stderr);
 const mutations=[
  x=>x.rows[1].future=[{"id":3}],
  x=>x.rows[1].H_sequence=[],
  x=>x.rows[0].H_sequence=[{"name":"events","seq":1}],
  x=>x.rows[0].before.G.visible_rows=[{"id":1,"note":"phantom"}],
  x=>x.rows[0].before.G.row_count=[{"n":1}],
  x=>x.rows[0].before.O_now=[{"id":1}],
  x=>x.rows[0].before.G.schema=[],
  x=>x.rows[0].before.G.intervention_sql="INSERT INTO events(note) VALUES ('different') RETURNING id;",
  x=>x.rows[0].before.G.journal_mode=[{"journal_mode":"wal"}],
  x=>x.rows[2].before.G.autoincrement=true,
  x=>x.rows[2].H_sequence=[{"name":"events","seq":1}],
  x=>x.rows[0].reopened_process_per_operation=false,
  x=>x.rows[0].round=1,
  x=>x.rows.pop(),
  x=>x.rows[0].arm="UNDECLARED",
  x=>x.rows[0].history=true,
  x=>x.rows[0].before.R="unknown-sqlite-route",
  x=>x.source_binary_sha256="not-a-hash",
  x=>x.expected_sqlite_source_commit="wrong",
  x=>x.observed_sqlite_version="3.45.0",
  x=>x.rounds=2,
  x=>x.arm_order.reverse()
 ];
 let rejected=0;
 for(const mutate of mutations){
  const x=structuredClone(baseline);
  mutate(x);
  const res=check(x);
  assert.notEqual(res.status,0,"mutated evidence escaped independent Court: "+rejected);
  rejected++;
 }
 console.log("P30_SQLITE_COURT_REAL_BASELINE=PASS");
 console.log("P30_SQLITE_COURT_ADVERSARIAL_MUTATIONS="+rejected+"/"+rejected);
 console.log("P30_SQLITE_COURT_UNMODIFIED_ARTIFACT=NOT_ALTERED");
}finally{
 fs.rmSync(temp,{recursive:true,force:true});
}
