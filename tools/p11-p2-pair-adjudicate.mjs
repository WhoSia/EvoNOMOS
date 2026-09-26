#!/usr/bin/env node
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const [directDir,segDir,outPath]=process.argv.slice(2);
if(!directDir||!segDir||!outPath){
  console.error('usage: p11-p2-pair-adjudicate.mjs <wide-dir> <seg-dir> <out.json>');
  process.exit(1);
}
const read=(d,n)=>JSON.parse(fs.readFileSync(path.join(d,n),'utf8'));
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const fail=m=>{console.error('PAIR_HOLD '+m);process.exit(1);};

const W=read(directDir,'arm-receipt.json');
const S=read(segDir,'arm-receipt.json');
if(W.arm!=='WIDE_BOUNDARY_REUSE'||S.arm!=='CAPABILITY_SEGREGATED') fail('arm identity');
for(const r of [W,S]){
  if(r.status!=='PASS'||r.source!=='dd421b79216c9b42eefd7b0191e546919f8be3f1') fail(r.arm+' source/status');
  for(const k of ['materialization','treatment_fidelity','build','shared_oracle','settings_contract','custody','reconstruction']){
    if(r[k]!=='PASS') fail(r.arm+' '+k);
  }
  if(r.phase0_provider!=='exa'||r.phase1_state!=='SEALED') fail(r.arm+' phase state');
  if(r.q0!==1) fail(r.arm+' Q0');
  if(r.measurement_firewall_released!==false||r.coordinates_opened!==false) fail(r.arm+' firewall');
  if(r.winner!==null) fail(r.arm+' winner');
  const bundle=path.join(r.arm==='WIDE_BOUNDARY_REUSE'?directDir:segDir,'arm.bundle');
  if(sha(bundle)!==r.arm_bundle_sha256) fail(r.arm+' bundle hash');
}
if(W.oracle_id!==S.oracle_id||W.oracle_id!=='SEARCH_FETCH_EXPOSURE_V01') fail('oracle mismatch');
if(W.demand_contract_sha256!==S.demand_contract_sha256) fail('demand contract mismatch');
if(W.rival_contract_sha256!==S.rival_contract_sha256) fail('rival contract mismatch');

const out={
  stage:'EvoNOMOS Generation VIII ORIGIN-R1-P11-P2',
  status:'PAIR_COMPARABLE__PHASE0_Q_PASS__EXACT_CUSTODY_PASS__MEASUREMENT_FIREWALL_CLOSED',
  source:W.source,
  arms:['WIDE_BOUNDARY_REUSE','CAPABILITY_SEGREGATED'],
  phase0:{provider:'exa',q:{WIDE_BOUNDARY_REUSE:1,CAPABILITY_SEGREGATED:1}},
  phase1:{provider:'tavily',state:'SEALED'},
  exact_bundle_custody:'PASS',
  pair_comparability:'PASS',
  measurement_firewall_released:false,
  coordinates_opened:false,
  coordinate_names:['S','L','C','A'],
  coordinate_values:'SEALED',
  authorized_next:'PHASE1_TAVILY_DUAL_ARM_MATERIALIZATION',
  winner:null
};
fs.mkdirSync(path.dirname(outPath),{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('COMPARABLE');
