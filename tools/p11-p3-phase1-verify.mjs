#!/usr/bin/env node
import fs from 'node:fs';
const [arm,p]=process.argv.slice(2);if(!arm||!p)process.exit(2);
const x=JSON.parse(fs.readFileSync(p,'utf8'));const fail=m=>{console.error('PHASE1_VERIFY_FAIL '+m);process.exit(1)};const has=(p,t)=>Array.isArray(p.tools)&&p.tools.includes(t);
if(x.treatment!==arm||x.network!=='MOCK_ONLY'||x.secret_leak!==false)fail('identity/network');
if(x.parallel?.search!=='PASS'||x.parallel?.fetch!=='PASS'||!has(x.parallel,'web_search')||!has(x.parallel,'web_fetch'))fail('parallel');
if(x.phase1?.provider!=='tavily'||x.phase1.search!=='PASS'||x.phase1.keyed!=='PASS'||x.phase1.keyless!=='PASS'||!has(x.phase1,'web_search'))fail('tavily search/auth');
if(arm==='WIDE_BOUNDARY_REUSE'){if(x.phase1.fetch!=='PASS'||!has(x.phase1,'web_fetch'))fail('wide fetch');}
else if(arm==='CAPABILITY_SEGREGATED'){if(x.phase1.fetch!=='HIDDEN'||has(x.phase1,'web_fetch'))fail('seg fetch');}
else fail('unknown arm');
console.log('ORACLE_OK');
