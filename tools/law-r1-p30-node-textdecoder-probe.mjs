#!/usr/bin/env node
// Source-pinned via workflow setup-node 22.16.0; outcome selection forbidden.
// Independent JS TextDecoder construction for each prefix/suffix pair.
import assert from "node:assert/strict";
import {TextDecoder,TextEncoder} from "node:util";
assert.equal(process.versions.node,"22.16.0","Exact Node runtime required");
const enc=new TextEncoder();
const prefixes=Array.from({length:30},(_,i)=>0xc2+i);
const suffixes=Array.from({length:64},(_,i)=>0x80+i);
function measure(prefix,suffix){
 const decoder=new TextDecoder("utf-8",{fatal:true,ignoreBOM:false});
 const current=decoder.decode(Uint8Array.of(prefix),{stream:true});
 let future;
 try{
  const decoded=decoder.decode(Uint8Array.of(suffix),{stream:false});
  future={ok:true,utf8:Buffer.from(enc.encode(decoded)).toString("hex")};
 }catch(err){future={ok:false,error:err?.name??"UnknownError"};}
 return {prefix,suffix,current,future,prefix_history_hex:prefix.toString(16),
 coarse_W:[1,"node-textdecoder-utf8",["fatal",true,"prefix-stream",true,"suffix-stream",false],1]};
}
function generate(){
 const rows=[];
 for(const suffix of suffixes)for(const prefix of prefixes)rows.push(measure(prefix,suffix));
 return rows;
}
const rows=generate();
const second=generate();
assert.deepEqual(second,rows);
const pair=rows.filter(r=>r.suffix===0xa9&&(r.prefix===0xc2||r.prefix===0xc3));
const result={
 stage:"G8 LAW-R1-P30",candidate:"Node.js WHATWG TextDecoder transport",
 source_commit_expected:"9774069718d9f80578079d252dddf37ae6fd550d",
 node_version:process.versions.node,icu_version:process.versions.icu,
 pair,
 prefixes:prefixes.map(p=>p.toString(16)),
 suffixes:suffixes.map(s=>s.toString(16)),
 rows,repeat_exact:true,
 claims:{same_UTF8_specification:true,cross_runtime_implementation:true,
 independent_mechanism_law:false,law_r2_authorized:false}
};
process.stdout.write(JSON.stringify(result)+"\n");
