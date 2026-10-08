#!/usr/bin/env node
// Synthetic regression fixtures. They are NOT SQLite world measurements.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
const root=fs.mkdtempSync(path.join(os.tmpdir(),"p31-court-regression-"));
const file=path.join(root,"raw.json");
const hs=[0,3,7,11],ms=[5,9],actions=["NOOP","RESERVE"];
const snap={
 schema:[
  {type:"table",name:"events",tbl_name:"events",sql:"CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT NOT NULL)"},
  {type:"table",name:"sqlite_sequence",tbl_name:"sqlite_sequence",sql:"CREATE TABLE sqlite_sequence(name,seq)"}
 ],
 rows:[],count:[{n:0}],journal:[{journal_mode:"delete"}],
 foreign_keys:[{foreign_keys:0}],read_uncommitted:[{read_uncommitted:0}]
};
const rows=[];
for(let r=0;r<3;r++)for(const m of ms)for(const h of hs)for(const a of actions){
 const reserve=a==="RESERVE",after=reserve?Math.max(h,m-1):h;
 rows.push({
  round:r,minimum_id:m,initial_h:h,action:a,
  source_schema:"events(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)",
  snapshot_before:structuredClone(snap),seq_before:[{name:"events",seq:h}],
  treatment:reserve?"BEGIN; INSERT_EXPLICIT_SENTINEL; DELETE_SENTINEL; COMMIT;":"NO_EXTRA_WRITE",
  extra_write_transactions:Number(reserve),extra_mutation_statements:reserve?2:0,
  seq_after:[{name:"events",seq:after}],snapshot_after:structuredClone(snap),
  delivery_verified_before_future:true,
  future_sql:"INSERT INTO events(note) VALUES('next') RETURNING id;",
  future:[{id:after+1}],file_bytes_before:4096,file_bytes_after:4096,
  file_size_delta:0,action_elapsed_ns:reserve?1000:0,
  independent_file_database:true,fresh_sqlite_process_per_statement:true
 });
}
const base={stage:"G8 LAW-R1-P31",
candidate:"SQLite Allocation-Threshold State-Aware Structural Policy",
expected_source_sha:"f3d536d37825302e31ed0eddd811c689f38f85a3",
expected_fossil_uuid:"c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33",
runtime_version:"3.46.1",source_executable_sha256:"a".repeat(64),
population:{rounds:3,high_water_values:hs,thresholds:ms,structural_actions:actions,trajectories:48},
rows,
authorities:{state_aware_policy_predeclared:true,source_pinned_in_hosted_workflow:true,
mechanism_transport_established:false,real_maintenance_demand:false,
law_r2_authorized:false,p31_closed:false}};
const target="tools/law-r1-p31-sqlite-policy-court.mjs";
const trial=obj=>{
 fs.writeFileSync(file,JSON.stringify(obj));
 return spawnSync(process.execPath,[target,file],{encoding:"utf8"});
};
try{
 const baseline=trial(base);
 assert.equal(baseline.status,0,"Untampered fixture must pass: "+baseline.stderr);
 const probes=[
 x=>x.rows[0].future[0].id=2,
 x=>x.rows[0].seq_before[0].seq=2,
 x=>x.rows[1].seq_after[0].seq=2,
 x=>x.rows[0].snapshot_after.count[0].n=1,
 x=>x.rows[1].snapshot_before.rows.push({id:1,note:"leak"}),
 x=>x.rows[1].extra_write_transactions=0,
 x=>x.rows[0].extra_mutation_statements=2,
 x=>x.rows[1].delivery_verified_before_future=false,
 x=>x.rows[1].file_size_delta=1,
 x=>x.rows[0].minimum_id=7,
 x=>x.rows[0].action="RESERVE",
 x=>x.rows[0].round=2,
 x=>x.rows.pop(),
 x=>x.rows[0].future_sql="SELECT 1;",
 x=>x.rows[0].snapshot_before.journal[0].journal_mode="wal",
 x=>x.expected_source_sha="unknown",
 x=>x.authorities.law_r2_authorized=true,
 x=>x.population.trajectories=47
 ];
 let rejected=0;
 for(const mutate of probes){
  const candidate=structuredClone(base);
  mutate(candidate);
  assert.notDeepEqual(candidate,base,"Mutation must not be a no-op");
  const result=trial(candidate);
  assert.notEqual(result.status,0,"Invalid evidence must fail at mutation "+rejected);
  rejected++;
 }
 console.log("P31_POLICY_COURT_SYNTHETIC_POSITIVE=PASS");
 console.log("P31_POLICY_COURT_MUTATION_REJECTION="+rejected+"/"+rejected);
 console.log("P31_POLICY_REAL_WORLD_EVIDENCE=NOT_CLAIMED");
}finally{fs.rmSync(root,{recursive:true,force:true});}
