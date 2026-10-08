#!/usr/bin/env node
// CPython/Node prospective cross-runtime transport: no summary trust, no row drops.
import assert from "node:assert/strict";
import fs from "node:fs";
import {createHash} from "node:crypto";
const [pyPath,nodePath,receiptPath]=process.argv.slice(2);
if(!pyPath||!nodePath)throw new Error("usage: node transport-join.mjs <python-census.json> <node-census.json> [receipt.json]");
const pyRaw=fs.readFileSync(pyPath),nodeRaw=fs.readFileSync(nodePath);
const p=JSON.parse(pyRaw),n=JSON.parse(nodeRaw);
assert.equal(p.candidate,"CPython UTF-8 predictive collision census");
assert.equal(p.implementation,"CPython");
assert.match(p.runtime,/^3\.12\.12(?:\s|$)/);
assert.equal(p.source_commit_expected,"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5");
assert.equal(n.candidate,"Node.js WHATWG TextDecoder transport");
assert.equal(n.node_version,"22.16.0");
assert.equal(n.source_commit_expected,"9774069718d9f80578079d252dddf37ae6fd550d");
assert.equal(p.rows.length,1920);assert.equal(n.rows.length,1920);
const pref=Array.from({length:30},(_,i)=>0xc2+i);
const suff=Array.from({length:64},(_,i)=>0x80+i);
assert.deepEqual(p.population.prefixes,pref.map(x=>x.toString(16)));
assert.deepEqual(p.population.suffixes,suff.map(x=>x.toString(16)));
assert.deepEqual(n.prefixes,pref.map(x=>x.toString(16)));
assert.deepEqual(n.suffixes,suff.map(x=>x.toString(16)));
assert.equal(p.counts.repeated_census_identical,true);
assert.equal(n.repeat_exact,true);
let match=0,interventionCollisionEdges=0;
const edgePairs=new Set();
for(let i=0;i<1920;i++){
 const suffix=suff[Math.floor(i/30)],prefix=pref[i%30];
 const a=p.rows[i],b=n.rows[i];
 for(const obj of [a,b]){
  assert.equal(obj.prefix,prefix);
  assert.equal(obj.suffix,suffix);
  assert.equal(obj.current,"");
  assert.equal(obj.future.ok,true);
 }
 assert.equal(a.pending_hex,prefix.toString(16));
 assert.equal(a.pending_length,1);assert.equal(a.state_flag,0);
 assert.equal(b.prefix_history_hex,prefix.toString(16));
 const predicted=Buffer.from(String.fromCodePoint(((prefix&31)<<6)|(suffix&63)),"utf8").toString("hex");
 assert.equal(a.future.utf8,predicted);
 assert.equal(b.future.utf8,predicted);
 assert.equal(a.future.utf8,b.future.utf8);
 match++;
}
for(const suffix of suff){
 const start=(suffix-0x80)*30;
 for(let i=0;i<30;i++)for(let j=i+1;j<30;j++){
  const ap=p.rows[start+i],bp=p.rows[start+j],an=n.rows[start+i],bn=n.rows[start+j];
  const pc=ap.future.utf8!==bp.future.utf8;
  const nc=an.future.utf8!==bn.future.utf8;
  assert.equal(pc,nc);
  if(pc){interventionCollisionEdges++;edgePairs.add(pref[i]+":"+pref[j]);}
 }
}
assert.equal(match,1920);
assert.equal(interventionCollisionEdges,27840);
assert.equal(edgePairs.size,435);
assert.deepEqual(p.bit_cover.all_minimal_bases,[[0,1,2,3,4]]);
const out={
 stage:"G8 LAW-R1-P30",
 verdict:"PASS_BOUNDED_CROSS_RUNTIME_TRACE_TRANSPORT__SAME_UTF8_SPEC__NOT_INDEPENDENT_MECHANISM__LAW_R2_NOT_AUTHORIZED",
 python_source:"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5",
 node_source:"9774069718d9f80578079d252dddf37ae6fd550d",
 python_raw_sha256:createHash("sha256").update(pyRaw).digest("hex"),
 node_raw_sha256:createHash("sha256").update(nodeRaw).digest("hex"),
 matched_trace_rows:match,
 matched_collision_edges:interventionCollisionEdges,
 minimum_basis:[0,1,2,3,4],
 correspondence_type:"bounded trace correspondence after explicit route-normalizing projection",
 no_full_bisimulation_claim:true,
 independent_semantic_specification:false,
 p30_closed:false,
 law_r2_authorized:false
};
console.log(JSON.stringify(out,null,2));
if(receiptPath)fs.writeFileSync(receiptPath,JSON.stringify(out,null,2)+"\n");
