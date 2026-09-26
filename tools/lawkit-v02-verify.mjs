#!/usr/bin/env node
import fs from 'node:fs';
const p=process.argv[2];
if(!p){console.error('usage: lawkit-v02-verify.mjs <json>');process.exit(1);}
const x=JSON.parse(fs.readFileSync(p,'utf8'));
const fail=(m)=>{console.error(m);process.exit(1);};
if(x.law_candidate!=='CIL-C1')fail('wrong law');
if(x.authority!=='HOLD_SELECTION_BLINDNESS')fail('authority ceiling violated');
if(x.evidence_class!=='EXPLORATORY_ONLY')fail('evidence class promoted');
if(x.cil_c1_update!=='FORBIDDEN_CONFIRMATORY_UPDATE')fail('confirmatory update leaked');
if(x.decision_authority!=='ABSTAIN')fail('decision authority must abstain');
for(const forbidden of ['winner','recommended_design','score']){
  if(forbidden in x)fail(forbidden+' leaked');
}
console.log('EVONOMOS_LAWKIT_V02_AUTHORITY=HOLD_SELECTION_BLINDNESS');
console.log('EVONOMOS_LAWKIT_V02_DECISION=ABSTAIN');
