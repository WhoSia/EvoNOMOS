#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
const [input,output]=process.argv.slice(2);
if(!input)throw new Error("usage: node law-r1-p30-node-transport-court.mjs raw.json [receipt.json]");
const r=JSON.parse(fs.readFileSync(input,"utf8"));
const prefixes=Array.from({length:30},(_,i)=>0xc2+i);
const suffixes=Array.from({length:64},(_,i)=>0x80+i);
assert.equal(r.stage,"G8 LAW-R1-P30");
assert.equal(r.candidate,"Node.js WHATWG TextDecoder transport");
assert.equal(r.source_commit_expected,"9774069718d9f80578079d252dddf37ae6fd550d");
assert.equal(r.node_version,"22.16.0");
assert.ok(typeof r.icu_version==="string"&&r.icu_version.length>0);
assert.deepEqual(r.prefixes,prefixes.map(p=>p.toString(16)));
assert.deepEqual(r.suffixes,suffixes.map(s=>s.toString(16)));
assert.equal(r.rows.length,1920);
assert.equal(r.repeat_exact,true);
assert.deepEqual(r.claims,{same_UTF8_specification:true,cross_runtime_implementation:true,independent_mechanism_law:false,law_r2_authorized:false});
const grouped=new Map(suffixes.map(s=>[s,[]]));
for(let idx=0;idx<r.rows.length;idx++){
 const row=r.rows[idx],suffix=suffixes[Math.floor(idx/30)],prefix=prefixes[idx%30];
 assert.equal(row.prefix,prefix);
 assert.equal(row.suffix,suffix);
 assert.equal(row.current,"");
 assert.equal(row.prefix_history_hex,prefix.toString(16));
 assert.deepEqual(row.coarse_W,[1,"node-textdecoder-utf8",["fatal",true,"prefix-stream",true,"suffix-stream",false],1]);
 const cp=((prefix&31)<<6)|(suffix&63);
 assert.deepEqual(row.future,{ok:true,utf8:Buffer.from(String.fromCodePoint(cp),"utf8").toString("hex")});
 grouped.get(suffix).push(row);
}
const pair=r.rows.filter(row=>row.suffix===0xa9&&(row.prefix===0xc2||row.prefix===0xc3));
assert.deepEqual(r.pair,pair);
assert.equal(pair.length,2);
assert.deepEqual(pair.map(row=>row.future.utf8),["c2a9","c3a9"]);
const combinations=30*29/2;
let totalEdges=0,uniquePairs=new Set();
for(const s of suffixes){
 const rows=grouped.get(s);
 let count=0;
 for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++)
  if(rows[i].future.utf8!==rows[j].future.utf8){
   count++;
   uniquePairs.add(rows[i].prefix+":"+rows[j].prefix);
  }
 assert.equal(count,combinations);
 totalEdges+=count;
}
function separates(bits){return [...uniquePairs].every(key=>{
 const [a,b]=key.split(":").map(Number);
 return bits.some(bit=>((a>>bit)&1)!==((b>>bit)&1));
});}
let minimal=[];
for(let k=0;k<=8;k++){
 for(let m=0;m<256;m++){
  const bits=Array.from({length:8},(_,i)=>i).filter(i=>m&(1<<i));
  if(bits.length===k&&separates(bits))minimal.push(bits);
 }
 if(minimal.length)break;
}
assert.deepEqual(minimal,[[0,1,2,3,4]]);
const receipt={
 stage:"G8 LAW-R1-P30",
 verdict:"PASS_NODE_TEXTDECODER_BOUNDED_PREDICTIVE_SPLIT__IMPLEMENTATION_TRANSPORT_ONLY__LAW_R2_NOT_AUTHORIZED",
 exact_node_version:r.node_version,
 icu_version:r.icu_version,
 measurements:r.rows.length,
 collision_edges:totalEdges,
 distinct_collision_pairs:uniquePairs.size,
 minimum_bit_basis:minimal,
 deletion_necessary:minimal[0].every(bit=>!separates(minimal[0].filter(x=>x!==bit))),
 pair_split:["c2a9","c3a9"],
 evidence_scope:"Node v22.16.0 TextDecoder same UTF-8 specification, separate runtime implementation",
 no_independent_mechanism_law:true,
 p30_closed:false,law_r2_authorized:false
};
console.log(JSON.stringify(receipt,null,2));
if(output)fs.writeFileSync(output,JSON.stringify(receipt,null,2)+"\n");
