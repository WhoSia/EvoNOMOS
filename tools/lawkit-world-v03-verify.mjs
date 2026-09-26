#!/usr/bin/env node
import fs from 'node:fs';
const p=process.argv[2];
if(!p){console.error('usage: lawkit-world-v03-verify.mjs <json>');process.exit(1);}
const x=JSON.parse(fs.readFileSync(p,'utf8'));
const fail=(m)=>{console.error(m);process.exit(1);};
if(x.protocol_version!=='0.3')fail('wrong protocol');
if(!['ADMIT','HOLD'].includes(x.admission))fail('bad admission');
if(x.decision_authority!=='NO_DESIGN_RECOMMENDATION')fail('design authority leaked');
if(x.winner!==null)fail('winner leaked');
if(x.admission==='ADMIT'&&x.authorized_next!=='PRETREATMENT_RIVAL_CONSTITUTION')fail('bad next authority');
if(x.law_pressures?.['CBL-C1']?.capability_bundle_mismatch!=='PRESENT')fail('P11 fixture must expose capability mismatch');
for(const gate of Object.values(x.gates??{})){if(gate!=='PASS'&&gate!=='FAIL')fail('invalid gate token');}
console.log('EVONOMOS_LAWKIT_V03_WORLD_ADMISSION=PASS');
console.log('EVONOMOS_LAWKIT_V03_DECISION_AUTHORITY=NONE');
