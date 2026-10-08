#!/usr/bin/env node
import fs from "node:fs";
import assert from "node:assert/strict";

const input=process.argv[2],output=process.argv[3];
if(!input)throw new Error("usage: node law-r1-p30-cpython-sweep-court.mjs <sweep.json> [verdict.json]");
const r=JSON.parse(fs.readFileSync(input,"utf8"));
assert.equal(r.stage,"G8 LAW-R1-P30");
assert.equal(r.implementation,"CPython");
assert.match(r.runtime,/^3\.12\.12(?:\s|$)/);
assert.equal(r.source_commit_expected,"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5");
const prefixes=Array.from({length:30},(_,i)=>0xC2+i);
const suffixes=Array.from({length:64},(_,i)=>0x80+i);
assert.deepEqual(r.population.prefixes,prefixes.map(i=>i.toString(16)));
assert.deepEqual(r.population.suffixes,suffixes.map(i=>i.toString(16)));
assert.equal(r.rows.length,1920);
const bySuffix=new Map(suffixes.map(s=>[s,[]]));
for(const row of r.rows) {
 assert.ok(prefixes.includes(row.prefix));
 assert.ok(suffixes.includes(row.suffix));
 assert.equal(row.current,"");
 assert.equal(row.pending_hex,row.prefix.toString(16));
 assert.equal(row.pending_length,1);
 assert.equal(row.state_flag,0);
 assert.deepEqual(row.coarse_W,[1,"cpython-codecs-utf8-incremental",[1,1,1,1],1]);
 assert.equal(row.future.ok,true);
 assert.equal(typeof row.future.utf8,"string");
 const unicode = ((row.prefix & 0x1f) << 6) | (row.suffix & 0x3f);
 const utf8=Buffer.from(String.fromCodePoint(unicode),"utf8").toString("hex");
 assert.equal(row.future.utf8,utf8);
 bySuffix.get(row.suffix).push(row);
}
let allEdges=0;
let edgeSet=new Set();
const counts={};
for(const suffix of suffixes) {
 const group=bySuffix.get(suffix);
 assert.equal(group.length,30);
 assert.deepEqual(group.map(x=>x.prefix),prefixes);
 let edges=0;
 for(let i=0;i<group.length;i++)for(let j=i+1;j<group.length;j++){
   const a=group[i],b=group[j];
   if(a.future.utf8!==b.future.utf8){
     edges++;
     edgeSet.add(a.prefix+":"+b.prefix);
   }
 }
 counts[String(suffix)]=edges;
 allEdges+=edges;
}
const distinctEdges=[...edgeSet].map(x=>x.split(":").map(Number));
const separable=(bits)=>distinctEdges.every(([a,b])=>bits.some(bit=>((a>>bit)&1)!==((b>>bit)&1)));
let minima=[];
for(let k=0;k<=8;k++){
 for(let mask=0;mask<256;mask++){
   const bits=Array.from({length:8},(_,i)=>i).filter(i=>mask&(1<<i));
   if(bits.length===k&&separable(bits))minima.push(bits);
 }
 if(minima.length)break;
}
assert.equal(r.counts.measurements,1920);
assert.equal(r.counts.collision_edges,allEdges);
assert.equal(r.counts.distinct_collision_pairs,edgeSet.size);
assert.deepEqual(r.counts.per_suffix_edges,counts);
assert.equal(r.counts.repeated_census_identical,true);
assert.deepEqual(r.bit_cover.all_minimal_bases,minima);
assert.equal(r.bit_cover.minimum_number_of_bits,minima[0].length);
for(const bit of minima[0])assert.equal(r.bit_cover.deletion_necessary[String(bit)],!separable(minima[0].filter(x=>x!==bit)));
assert.equal(r.claims.law_r2_authorized,false);
assert.equal(r.claims.external_mechanism_replications,0);
const verdict={
 stage:"G8 LAW-R1-P30",source:"CPython v3.12.12 exact-source restricted census",
 verdict:"PASS_BOUNDED_PREDICTIVE_COLLISION_CENSUS__MINIMAL_BIT_RESCUE_CONFIRMED__LAW_R2_NOT_AUTHORIZED",
 measurements:r.rows.length,
 collision_edges:allEdges,
 distinct_collision_pairs:edgeSet.size,
 minimum_bit_basis:minima,
 full_raw_rows_validated:true,
 predictive_state_failure:"coarse W only, under one-step suffix interventions",
 refinement:"pending-byte bits measured before future Y",
 law_r2_authorized:false,
 status:"CANDIDATE_EVIDENCE_ONLY__P30_NOT_CLOSED"
};
console.log(JSON.stringify(verdict,null,2));
if(output)fs.writeFileSync(output,JSON.stringify(verdict,null,2)+"\n");
