#!/usr/bin/env node
// Synthetic fixtures only; not a substitute for source-pinned Node hosted execution.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import {spawnSync} from "node:child_process";
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),"p30-node-transport-test-"));
const file=path.join(tmp,"raw.json");
const pre=Array.from({length:30},(_,i)=>0xc2+i),suf=Array.from({length:64},(_,i)=>0x80+i);
const rows=[];
for(const suffix of suf)for(const prefix of pre){
 const cp=((prefix&31)<<6)|(suffix&63);
 rows.push({prefix,suffix,current:"",future:{ok:true,utf8:Buffer.from(String.fromCodePoint(cp)).toString("hex")},prefix_history_hex:prefix.toString(16),coarse_W:[1,"node-textdecoder-utf8",["fatal",true,"prefix-stream",true,"suffix-stream",false],1]});
}
const base={
 stage:"G8 LAW-R1-P30",candidate:"Node.js WHATWG TextDecoder transport",
 source_commit_expected:"9774069718d9f80578079d252dddf37ae6fd550d",
 node_version:"22.16.0",icu_version:"fixture",
 prefixes:pre.map(x=>x.toString(16)),suffixes:suf.map(x=>x.toString(16)),
 rows,pair:rows.filter(r=>r.suffix===0xa9&&(r.prefix===0xc2||r.prefix===0xc3)),repeat_exact:true,
 claims:{same_UTF8_specification:true,cross_runtime_implementation:true,independent_mechanism_law:false,law_r2_authorized:false}
};
const court="tools/law-r1-p30-node-transport-court.mjs";
function run(x){
 fs.writeFileSync(file,JSON.stringify(x));
 return spawnSync(process.execPath,[court,file],{encoding:"utf8"});
}
try{
 const good=run(base);
 assert.equal(good.status,0,"positive fixture: "+good.stderr);
 const changes=[
 x=>x.rows[0].future.utf8="ffff",
 x=>x.rows[0].current="!",
 x=>x.rows[0].coarse_W[3]=0,
 x=>x.rows[0].prefix_history_hex="c3",
 x=>x.rows[0].prefix=0xc3,
 x=>x.rows.pop(),
 x=>x.rows.push(structuredClone(x.rows[0])),
 x=>x.pair.pop(),
 x=>x.repeat_exact=false,
 x=>x.node_version="22.17.0",
 x=>x.icu_version="",
 x=>x.claims.law_r2_authorized=true,
 x=>x.claims.independent_mechanism_law=true,
 x=>x.prefixes[0]="c3",
 x=>x.suffixes[0]="81",
 x=>x.source_commit_expected="wrong"
 ];
 let caught=0;
 for(const mutate of changes){
 const altered=structuredClone(base);mutate(altered);
 const test=run(altered);
 assert.notEqual(test.status,0,"adversarial mutation escaped: "+caught);
 caught++;
 }
 console.log("P30_NODE_TRANSPORT_COURT_POSITIVE_SYNTHETIC=PASS");
 console.log("P30_NODE_TRANSPORT_COURT_MUTATIONS_REJECTED="+caught+"/"+caught);
 console.log("P30_NODE_TRANSPORT_WORLD_EVIDENCE=NOT_CLAIMED");
} finally{fs.rmSync(tmp,{recursive:true,force:true});}
