#!/usr/bin/env node
import fs from 'node:fs';

const [treatment,path]=process.argv.slice(2);
if(!treatment||!path){
  console.error('usage: p11-p1-exposure-verify.mjs <WIDE_BOUNDARY_REUSE|CAPABILITY_SEGREGATED> <probe.json>');
  process.exit(1);
}
const x=JSON.parse(fs.readFileSync(path,'utf8'));
const fail=m=>{console.error('EXPOSURE_FAIL '+m);process.exit(1);};
const has=(phase,tool)=>Array.isArray(phase.tools)&&phase.tools.includes(tool);

if(x.network!=='MOCK_ONLY') fail('network not mocked');
if(x.secret_leak!==false) fail('secret leak');
if(x.parallel?.search!=='PASS'||x.parallel?.fetch!=='PASS') fail('parallel behavior');
if(!has(x.parallel,'web_search')||!has(x.parallel,'web_fetch')) fail('parallel tool exposure');

for(const [name,p] of [['phase0',x.phase0],['phase1',x.phase1]]){
  if(!p) fail(name+' missing');
  if(p.search!=='PASS'||!has(p,'web_search')) fail(name+' search');
  if(treatment==='WIDE_BOUNDARY_REUSE'){
    if(p.fetch!=='PASS'||!has(p,'web_fetch')) fail(name+' wide fetch must be visible and functional');
  }else if(treatment==='CAPABILITY_SEGREGATED'){
    if(p.fetch!=='HIDDEN'||has(p,'web_fetch')) fail(name+' segregated fetch must be hidden');
  }else{
    fail('unknown treatment');
  }
}
if(x.treatment!==treatment) fail('treatment identity mismatch');
console.log('SEARCH_FETCH_EXPOSURE_ORACLE=PASS');
console.log('TREATMENT_FIDELITY=PASS');
