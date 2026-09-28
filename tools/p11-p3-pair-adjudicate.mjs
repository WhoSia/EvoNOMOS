#!/usr/bin/env node
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const [wideDir,segDir,outPath]=process.argv.slice(2);
if(!wideDir||!segDir||!outPath){console.error('usage');process.exit(2);}
const read=(d,n)=>JSON.parse(fs.readFileSync(path.join(d,n),'utf8'));
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const fail=m=>{console.error('PAIR_HOLD '+m);process.exit(1);};
const W=read(wideDir,'arm-receipt.json'),S=read(segDir,'arm-receipt.json');
if(W.arm!=='WIDE_BOUNDARY_REUSE'||S.arm!=='CAPABILITY_SEGREGATED')fail('arm identity');
for(const [r,d] of [[W,wideDir],[S,segDir]]){
  if(r.status!=='PASS'||r.source!=='dd421b79216c9b42eefd7b0191e546919f8be3f1')fail(r.arm+' source/status');
  for(const k of ['parent_custody','materialization','treatment_fidelity','build','shared_oracle','settings_contract','custody','reconstruction']) if(r[k]!=='PASS')fail(r.arm+' '+k);
  if(r.q0!==1||r.q1!==1)fail(r.arm+' Q');
  if(r.phase0_provider!=='exa'||r.phase1_provider!=='tavily')fail(r.arm+' phase identity');
  if(r.measurement_firewall_released!==false||r.coordinates_opened!==false||r.winner!==null)fail(r.arm+' firewall/winner');
  if(sha(path.join(d,'arm.bundle'))!==r.arm_bundle_sha256)fail(r.arm+' bundle hash');
}
for(const k of ['measurement_constitution_sha256','law_court_constitution_sha256','demand_contract_sha256','rival_contract_sha256']){
  if(W[k]!==S[k])fail(k+' mismatch');
}
if(W.oracle_id!==S.oracle_id||W.oracle_id!=='SEARCH_FETCH_EXPOSURE_V01')fail('oracle mismatch');
const out={
  stage:'EvoNOMOS Generation VIII ORIGIN-R1-P11-P3',
  status:'PAIR_COMPARABLE__PHASE1_Q_PASS__EXACT_CUSTODY_PASS__FIREWALL_RELEASE_ELIGIBLE',
  source:W.source,
  phase0:{provider:'exa',q:{WIDE_BOUNDARY_REUSE:1,CAPABILITY_SEGREGATED:1},coordinates:'SEALED'},
  phase1:{provider:'tavily',q:{WIDE_BOUNDARY_REUSE:1,CAPABILITY_SEGREGATED:1},coordinates:'SEALED'},
  exact_bundle_custody:'PASS',
  pair_comparability:'PASS',
  measurement_firewall_released:false,
  release_eligible:true,
  coordinate_values:'SEALED_UNTIL_REVEAL_JOB',
  winner:null
};
fs.mkdirSync(path.dirname(outPath),{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('COMPARABLE');
console.log('FIREWALL_RELEASE_ELIGIBLE');
