#!/usr/bin/env node
import fs from 'node:fs';

const [arm,path]=process.argv.slice(2);
if(!arm||!path){
  console.error('usage: p11-p2-phase0-verify.mjs <arm> <probe.json>');
  process.exit(1);
}
const x=JSON.parse(fs.readFileSync(path,'utf8'));
const fail=m=>{console.error('PHASE0_VERIFY_FAIL '+m);process.exit(1);};
const has=(p,t)=>Array.isArray(p.tools)&&p.tools.includes(t);

if(x.treatment!==arm) fail('arm identity');
if(x.network!=='MOCK_ONLY'||x.secret_leak!==false) fail('network/secret');
if(x.parallel?.search!=='PASS'||x.parallel?.fetch!=='PASS') fail('parallel validity');
if(!has(x.parallel,'web_search')||!has(x.parallel,'web_fetch')) fail('parallel exposure');
if(x.phase0?.provider!=='exa'||x.phase0?.search!=='PASS'||!has(x.phase0,'web_search')) fail('Exa search');
if(x.phase1?.provider!=='tavily'||x.phase1?.search!=='SEALED'||x.phase1?.fetch!=='SEALED') fail('Tavily seal');
if((x.phase1?.tools??[]).length!==0) fail('Tavily tools opened');

if(arm==='WIDE_BOUNDARY_REUSE'){
  if(x.phase0.fetch!=='PASS'||!has(x.phase0,'web_fetch')) fail('wide fetch fidelity');
}else if(arm==='CAPABILITY_SEGREGATED'){
  if(x.phase0.fetch!=='HIDDEN'||has(x.phase0,'web_fetch')) fail('seg fetch exposure');
}else{
  fail('unknown arm');
}

console.log('ORACLE_OK');
