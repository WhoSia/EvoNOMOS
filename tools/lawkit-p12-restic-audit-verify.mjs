#!/usr/bin/env node
import fs from 'node:fs';

const [worldPath,auditPath,outPath]=process.argv.slice(2);
if(!worldPath||!auditPath||!outPath){
  console.error('usage: verify <world.json> <audit.json> <out.json>');
  process.exit(1);
}
const world=JSON.parse(fs.readFileSync(worldPath,'utf8'));
const audit=JSON.parse(fs.readFileSync(auditPath,'utf8'));
const fail=m=>{console.error('RESTIC_WORLD_HOLD '+m);process.exit(1);};

if(world.world_id!=='RESTIC_OCI_ONEDRIVE') fail('world identity');
if(audit.world_id!==world.world_id) fail('audit identity');
if(audit.status!=='PASS') fail('source audit');
if(audit.exact_source_commit!==world.source.exact_pre_demand_commit) fail('source commit');

const core=['Save','Load','Stat','List','Remove','Delete'];
for(const m of core){
  if(audit.core_method_coverage?.[m]!=='MANDATORY') fail(m+' not mandatory');
  if(audit.conformance_exercised?.[m]!=='EXERCISED') fail(m+' not exercised');
}
for(const [pattern,paths] of Object.entries(audit.forbidden_provider_evidence??{})){
  if(paths.length) fail('pre-demand provider evidence '+pattern);
}
if(world.demands.initial.natural!==true||world.demands.followup.natural!==true) fail('non-natural demand');
if(world.demands.pair_frozen_before_evonomos_treatment!==true) fail('pair not frozen');
if(world.demands.initial.implementation_exposure!=='POST_DEMAND_IMPLEMENTATION_EXISTS_BUT_UNREAD') fail('OCI exposure class');
if(world.demands.followup.implementation_exposure!=='NONE_OBSERVED') fail('OneDrive exposure class');

const out={
  stage:'EvoNOMOS Generation VIII ORIGIN-R1-P12',
  world_id:world.world_id,
  source_audit:'PASS',
  backend_core_bundle:core,
  corequirement_geometry:'HIGH',
  capability_bundle_mismatch_at_admission:'LOW_OR_ABSENT',
  real_pair:{initial:4517,followup:5301},
  cbl_c1_falsification_pressure:'HIGH',
  authority:'WORLD_ADMISSION_ELIGIBLE',
  design_recommendation:'NONE',
  treatment_bytes:0,
  winner:null
};
fs.mkdirSync(new URL('.', 'file://'+process.cwd()+'/'+outPath).pathname,{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('P12_RESTIC_WORLD_AUDIT=PASS');
console.log('P12_CBL_FALSIFICATION_PRESSURE=HIGH');
