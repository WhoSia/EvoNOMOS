#!/usr/bin/env node
// Adversarial mutations of an actually measured Phase II-H raw artifact.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import {spawnSync} from "node:child_process";
const input=process.argv[2];
if(!input)throw new Error("usage: node law-r1-p30-sqlite-verified-equalization-court.test.mjs <raw>");
const base=JSON.parse(fs.readFileSync(input,"utf8"));
const folder=fs.mkdtempSync(path.join(os.tmpdir(),"p30-sqlite-IIH-tamper-"));
const fixture=path.join(folder,"case.json");
const program="tools/law-r1-p30-sqlite-verified-equalization-court.mjs";
const run=obj=>{
 fs.writeFileSync(fixture,JSON.stringify(obj));
 return spawnSync(process.execPath,[program,fixture],{encoding:"utf8"});
};
try{
 const good=run(base);
 assert.equal(good.status,0,"unmodified measured evidence failed: "+good.stderr);
 const tamper=[
  x=>x.rows[0].future=[{"id":9}],
  x=>x.rows[1].future=[{"id":1}],
  x=>x.rows[0].H_after[0].seq=1,
  x=>x.rows[1].H_after[0].seq=7,
  x=>x.rows[0].H_before=[{"name":"events","seq":1}],
  x=>x.rows[1].H_before=[],
  x=>x.rows[0].treatment_branch="UPDATE_IF_EXISTS",
  x=>x.rows[1].treatment_branch="INSERT_IF_MISSING",
  x=>x.rows[0].treatment_sql="INSERT OR REPLACE INTO sqlite_sequence(name,seq) VALUES('events',0);",
  x=>x.rows[0].fidelity_verified_before_future=false,
  x=>x.rows[0].before.visible=[{"id":4,"note":"leak"}],
  x=>x.rows[0].after.count=[{"n":1}],
  x=>x.rows[0].before.schema=[],
  x=>x.rows[0].before.journal_mode=[{"journal_mode":"wal"}],
  x=>x.rows[0].round=2,
  x=>x.rows.pop(),
  x=>x.rows[0].fresh_cli_process_per_sql_operation=false,
  x=>x.source_commit_expected="wrong",
  x=>x.fossil_uuid_expected="wrong",
  x=>x.sqlite_binary_sha256="corrupted",
  x=>x.target_values=[0,9],
  x=>x.version="3.45.3",
  x=>x.claim_ceiling="LAW-R2 authorized"
 ];
 let n=0;
 for(const mutation of tamper){
  const copy=structuredClone(base);mutation(copy);
  const actual=run(copy);
  assert.notEqual(actual.status,0,"tampered outcome accepted: "+n);
  n++;
 }
 console.log("P30_SQLITE_IIH_GENUINE_BASELINE=PASS");
 console.log("P30_SQLITE_IIH_REJECTED_TAMPERS="+n+"/"+n);
 console.log("P30_SQLITE_IIH_FAILED_PREVIOUS_UPSERT_REJECTED=PASS");
}finally{fs.rmSync(folder,{recursive:true,force:true});}
