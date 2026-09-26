#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const [directPath,invertPath,outPath]=process.argv.slice(2);
if(!directPath||!invertPath||!outPath){
  console.error('usage: p10-p3-adjudicate.mjs <direct-json> <invert-json> <out-json>');
  process.exit(1);
}
const D=JSON.parse(fs.readFileSync(directPath,'utf8'));
const I=JSON.parse(fs.readFileSync(invertPath,'utf8'));
const die=(m)=>{console.error(m);process.exit(1);};
if(D.arm!=='DIRECT_DEDICATED'||I.arm!=='INVERT_CHANNEL_ADAPTER')die('arm identity mismatch');
if(D.authority!=='EXPLORATORY_ONLY'||I.authority!=='EXPLORATORY_ONLY')die('authority mismatch');
for(const x of [D,I]){
  if(x.vector.Q0!==1||x.vector.Q1!==1)die(x.arm+': validity gate failed');
  if(x.winner!==null)die(x.arm+': winner leaked');
}
const dir=(d,i)=>d===i?'EQUAL':(d>i?'DIRECT_HIGHER':'INVERT_HIGHER');
const phase={
  surface:{phase0:dir(D.vector.S0,I.vector.S0),phase1:dir(D.vector.S1,I.vector.S1)},
  churn:{phase0:dir(D.vector.L0,I.vector.L0),phase1:dir(D.vector.L1,I.vector.L1)},
};
const reversed=(x)=>x.phase0!=='EQUAL'&&x.phase1!=='EQUAL'&&x.phase0!==x.phase1;
const pattern=(x)=>{
  if(x.phase0==='INVERT_HIGHER'&&x.phase1==='DIRECT_HIGHER')return 'INITIAL_INVERSION_TAX_THEN_PROPAGATION_SAVING';
  if(x.phase0==='DIRECT_HIGHER'&&x.phase1==='INVERT_HIGHER')return 'INITIAL_DIRECT_TAX_THEN_INVERSION_FOLLOWUP_TAX';
  if(x.phase0===x.phase1)return 'NO_SIGN_REVERSAL';
  return 'MIXED_OR_EQUAL';
};
const out={
  stage:'EvoNOMOS Generation VIII ORIGIN-R1-P10-P3',
  authority:'EXPLORATORY_ONLY',
  confirmatory_authority:'HOLD_SELECTION_BLINDNESS',
  followup:'PUSHOVER_PROTOCOL_REAL_SYNTHETIC_FOLLOWUP_v1',
  vectors:{DIRECT_DEDICATED:D.vector,INVERT_CHANNEL_ADAPTER:I.vector},
  phasewise_direction:phase,
  reversal:{surface:reversed(phase.surface),churn:reversed(phase.churn)},
  lifecycle_pattern:{surface:pattern(phase.surface),churn:pattern(phase.churn)},
  cil_c1_update:'FORBIDDEN_CONFIRMATORY_UPDATE',
  interpretation:[
    'Lifecycle signs are descriptive exploratory evidence only.',
    'The Pushover follow-up is protocol-real but not an independently observed project demand.',
    'A pre-followup one-arm change-volume proxy leak blocks confirmatory CIL-C1 updating.',
    'No overall design winner is authorized.'
  ],
  winner:null,
};
fs.mkdirSync(path.dirname(outPath),{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('P10_P3_LIFECYCLE_REVEAL=PASS');
console.log('P10_P3_CONFIRMATORY_AUTHORITY=HOLD_SELECTION_BLINDNESS');
console.log('P10_P3_WINNER=NONE');
