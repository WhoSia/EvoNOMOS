#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const [repoRoot,specPath,outPath]=process.argv.slice(2);
if(!repoRoot||!specPath||!outPath){
  console.error('usage: github_provider_family_v01.mjs <repo-root> <spec.json> <out.json>');
  process.exit(1);
}
const spec=JSON.parse(fs.readFileSync(specPath,'utf8'));
const fail=(m)=>{console.error(m);process.exit(1);};
const head=execFileSync('git',['-C',repoRoot,'rev-parse','HEAD'],{encoding:'utf8'}).trim();
if(head!==spec.expected_commit)fail('source commit mismatch');

const siteResults=[];
const scanned=[];
for(const site of spec.authority_sites){
  const p=path.join(repoRoot,site.path);
  if(!fs.existsSync(p))fail('missing authority site: '+site.path);
  const text=fs.readFileSync(p,'utf8');
  for(const token of site.must_contain??[]){
    if(!text.includes(token))fail(site.name+': missing token '+JSON.stringify(token));
  }
  siteResults.push({name:site.name,path:site.path,status:'PASS'});
  scanned.push({path:site.path,text});
}
const forbidden={};
for(const token of spec.forbidden_provider_tokens??[]){
  const locations=scanned.filter(x=>x.text.toLowerCase().includes(token.toLowerCase())).map(x=>x.path);
  forbidden[token]={status:locations.length===0?'ABSENT':'PRESENT',locations};
  if(locations.length)fail('forbidden pre-demand provider token present: '+token);
}
const ifacePath=path.join(repoRoot,spec.interface.path);
const ifaceText=fs.readFileSync(ifacePath,'utf8');
for(const token of spec.interface.must_contain??[]){
  if(!ifaceText.includes(token))fail('interface evidence missing '+JSON.stringify(token));
}
const out={
  adapter:'github-provider-family-v0.1',
  world_id:spec.world_id,
  exact_source_commit:head,
  membership_surface_fanout:siteResults.length,
  authority_sites:siteResults,
  existing_runtime_interface:true,
  interface_capabilities:spec.interface.capabilities,
  forbidden_provider_tokens:forbidden,
  status:'PASS',
};
fs.mkdirSync(path.dirname(outPath),{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('LAWKIT_SOURCE_ADAPTER=PASS');
console.log('LAWKIT_SOURCE_FANOUT='+siteResults.length);
