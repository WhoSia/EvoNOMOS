#!/usr/bin/env node
// Independent Court: use raw SQLite observations, not probe-computed verdicts.
import fs from "node:fs";
import assert from "node:assert/strict";
const [file,receipt]=process.argv.slice(2);
if(!file)throw Error("Usage: node law-r1-p31-sqlite-policy-court.mjs RAW.json [receipt]");
const x=JSON.parse(fs.readFileSync(file,"utf8"));
const hs=[0,3,7,11],ms=[5,9],as=["NOOP","RESERVE"];
assert.equal(x.stage,"G8 LAW-R1-P31");
assert.equal(x.candidate,"SQLite Allocation-Threshold State-Aware Structural Policy");
assert.equal(x.runtime_version,"3.46.1");
assert.equal(x.expected_source_sha,"f3d536d37825302e31ed0eddd811c689f38f85a3");
assert.equal(x.expected_fossil_uuid,"c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33");
assert.match(x.source_executable_sha256,/^[0-9a-f]{64}$/);
assert.deepEqual(x.population,{rounds:3,high_water_values:hs,thresholds:ms,structural_actions:as,trajectories:48});
assert.deepEqual(x.authorities,{state_aware_policy_predeclared:true,source_pinned_in_hosted_workflow:true,mechanism_transport_established:false,real_maintenance_demand:false,law_r2_authorized:false,p31_closed:false});
assert.equal(x.rows.length,48);
const snapshots=new Map(),arms=new Map();
for(let i=0;i<48;i++){
 const z=x.rows[i],r=Math.floor(i/16),m=ms[Math.floor(i/8)%2],h=hs[Math.floor(i/2)%4],a=as[i%2];
 assert.deepEqual([z.round,z.minimum_id,z.initial_h,z.action],[r,m,h,a]);
 assert.equal(z.source_schema,"events(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)");
 assert.equal(z.future_sql,"INSERT INTO events(note) VALUES('next') RETURNING id;");
 assert.equal(z.delivery_verified_before_future,true);
 assert.equal(z.independent_file_database,true);
 assert.equal(z.fresh_sqlite_process_per_statement,true);
 assert.deepEqual(z.seq_before,[{name:"events",seq:h}]);
 assert.deepEqual(z.seq_after,[{name:"events",seq:a==="RESERVE"?Math.max(h,m-1):h}]);
 assert.deepEqual(z.snapshot_before,z.snapshot_after);
 const s=z.snapshot_before;
 assert.deepEqual(s.rows,[]);assert.deepEqual(s.count,[{n:0}]);
 assert.deepEqual(s.journal,[{journal_mode:"delete"}]);
 assert.deepEqual(s.foreign_keys,[{foreign_keys:0}]);
 assert.deepEqual(s.read_uncommitted,[{read_uncommitted:0}]);
 assert.equal(s.schema.length,2);
 assert.equal(s.schema.filter(t=>t.name==="events"&&t.type==="table"&&t.sql.includes("AUTOINCREMENT")).length,1);
 assert.equal(s.schema.filter(t=>t.name==="sqlite_sequence").length,1);
 const k=r+":"+m;
 if(snapshots.has(k))assert.deepEqual(s,snapshots.get(k));
 else snapshots.set(k,s);
 assert.equal(z.treatment,a==="NOOP"?"NO_EXTRA_WRITE":"BEGIN; INSERT_EXPLICIT_SENTINEL; DELETE_SENTINEL; COMMIT;");
 assert.equal(z.extra_write_transactions,a==="NOOP"?0:1);
 assert.equal(z.extra_mutation_statements,a==="NOOP"?0:2);
 assert.ok(Number.isSafeInteger(z.action_elapsed_ns)&&z.action_elapsed_ns>=0);
 assert.ok(Number.isSafeInteger(z.file_bytes_before)&&z.file_bytes_before>0);
 assert.ok(Number.isSafeInteger(z.file_bytes_after)&&z.file_bytes_after>0);
 assert.equal(z.file_size_delta,z.file_bytes_after-z.file_bytes_before);
 assert.deepEqual(z.future,[{id:a==="NOOP"?h+1:Math.max(h,m-1)+1}]);
 arms.set(r+":"+m+":"+h+":"+a,z);
}
let failures=0,unnecessary=0,repairs=0;
for(let r=0;r<3;r++)for(const m of ms){
 const classes=new Set();
 for(const h of hs){
  const noop=arms.get(r+":"+m+":"+h+":NOOP");
  const reserve=arms.get(r+":"+m+":"+h+":RESERVE");
  assert.deepEqual(noop.snapshot_before,reserve.snapshot_before);
  const bit=Number(h+1<m);classes.add(bit);
  failures+=Number(noop.future[0].id<m);
  unnecessary+=Number(noop.future[0].id>=m);
  repairs+=bit;
  const picked=bit?reserve:noop;
  assert.equal(picked.future[0].id<m,false);
  assert.equal(picked.extra_write_transactions,bit);
 }
 assert.deepEqual([...classes].sort(),[0,1]);
}
assert.deepEqual({failures,unnecessary,repairs},{failures:15,unnecessary:9,repairs:15});
const verdict={stage:"G8 LAW-R1-P31",verdict:"PASS_BOUNDED_DECISION_SUFFICIENT_ONE_BIT__STATE_AWARE_POLICY_DISCRIMINATES__LAW_R2_NOT_AUTHORIZED",
source_commit:x.expected_source_sha,exe_digest:x.source_executable_sha256,
trajectories:48,paired_decision_cells:24,
comparison:{NOOP:{violations:15,extra_transactions:0},RESERVE:{violations:0,extra_transactions:24,redundant:9},H_AWARE:{violations:0,extra_transactions:15,redundant:0}},
minimum_feature_bits_on_frozen_support:1,
exact_future_ID_from_one_bit:false,
real_maintenance_demand:false,p31_closed:false,law_r2_authorized:false};
console.log(JSON.stringify(verdict,null,2));
if(receipt)fs.writeFileSync(receipt,JSON.stringify(verdict,null,2)+"\n");
