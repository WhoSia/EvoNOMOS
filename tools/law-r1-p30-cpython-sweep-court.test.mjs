#!/usr/bin/env node
// Adversarial tests of the independent full-row Court, using an analytical UTF-8
// fixture. This proves verifier logic, not source-pinned CPython world evidence.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import {spawnSync} from "node:child_process";
const temp=fs.mkdtempSync(path.join(os.tmpdir(),"p30-sweep-court-"));
const filename=path.join(temp,"fixture.json");
const court="tools/law-r1-p30-cpython-sweep-court.mjs";
const prefixes=Array.from({length:30},(_,i)=>0xc2+i);
const suffixes=Array.from({length:64},(_,i)=>0x80+i);
const rows=[];
for(const suffix of suffixes)for(const prefix of prefixes){
  const unicode=((prefix&31)<<6)|(suffix&63);
  rows.push({
    prefix,suffix,current:"",pending_hex:prefix.toString(16),
    pending_length:1,state_flag:0,
    coarse_W:[1,"cpython-codecs-utf8-incremental",[1,1,1,1],1],
    future:{ok:true,utf8:Buffer.from(String.fromCodePoint(unicode)).toString("hex")}
  });
}
const base={
 stage:"G8 LAW-R1-P30",candidate:"CPython UTF-8 predictive collision census",
 implementation:"CPython",runtime:"3.12.12 synthetic fixture",
 source_commit_expected:"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5",
 population:{prefixes:prefixes.map(x=>x.toString(16)),suffixes:suffixes.map(x=>x.toString(16))},
 rows,
 counts:{measurements:1920,collision_edges:27840,distinct_collision_pairs:435,
         per_suffix_edges:Object.fromEntries(suffixes.map(s=>[String(s),435])),
         repeated_census_identical:true},
 bit_cover:{minimum_number_of_bits:5,all_minimal_bases:[[0,1,2,3,4]],
            deletion_necessary:{"0":true,"1":true,"2":true,"3":true,"4":true}},
 claims:{external_mechanism_replications:0,law_r2_authorized:false}
};
function run(obj){
 fs.writeFileSync(filename,JSON.stringify(obj));
 return spawnSync(process.execPath,[court,filename],{encoding:"utf8"});
}
try{
 const good=run(base);
 assert.equal(good.status,0,"baseline fixture failed: "+good.stderr);
 const mutations=[
  x=>x.rows[0].future.utf8="ffff",
  x=>x.rows[0].pending_hex="c3",
  x=>x.rows[0].coarse_W[3]=0,
  x=>x.rows[0].current="x",
  x=>x.rows[0].state_flag=1,
  x=>x.rows[1].prefix=0xc2,
  x=>x.rows.pop(),
  x=>x.rows.push(structuredClone(x.rows[0])),
  x=>x.counts.collision_edges=27839,
  x=>x.counts.per_suffix_edges["128"]=434,
  x=>x.bit_cover.minimum_number_of_bits=4,
  x=>x.bit_cover.all_minimal_bases=[[0,1,2,3,5]],
  x=>x.bit_cover.deletion_necessary["0"]=false,
  x=>x.runtime="3.13.5",
  x=>x.claims.law_r2_authorized=true,
  x=>x.counts.repeated_census_identical=false
 ];
 let caught=0;
 for(const modify of mutations){
  const bad=structuredClone(base);modify(bad);
  const test=run(bad);
  assert.notEqual(test.status,0,"mutation escaped: "+caught);
  caught++;
 }
 console.log("P30_SWEEP_COURT_SYNTHETIC_BASELINE=PASS");
 console.log("P30_SWEEP_COURT_TAMPER_REJECTIONS="+caught+"/"+caught);
 console.log("P30_SWEEP_COURT_EXTERNAL_SOURCE_EVIDENCE=NOT_CLAIMED");
} finally {fs.rmSync(temp,{recursive:true,force:true});}
