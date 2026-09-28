#!/usr/bin/env node
import fs from 'node:fs';
const [input,out]=process.argv.slice(2);
if(!input||!out){console.error('usage: verify <candidates.json> <prolog-output.json>');process.exit(1);}
const src=JSON.parse(fs.readFileSync(input,'utf8'));
const x=JSON.parse(fs.readFileSync(out,'utf8'));
const fail=m=>{console.error('DISCOVERY_VERIFY_FAIL '+m);process.exit(1);};
if(x.protocol!=='0.5'||x.authority!=='DISCOVERY_ONLY') fail('protocol/authority');
if(x.promoted!==null) fail('premature promotion');
const byId=new Map(x.candidates.map(c=>[c.id,c]));
for(const c of src.candidates){
  if(!byId.has(c.id)) fail('missing '+c.id);
}
const contaminated=byId.get('DUPLICATI_MOVISTAR');
if(contaminated?.admission!=='HOLD') fail('contaminated Duplicati candidate admitted');
const restic=byId.get('RESTIC_OCI_ONEDRIVE');
if(restic?.admission!=='ADMITTABLE') fail('Restic adversarial pair not admitted');
if(restic?.capability_corequirement!=='HIGH') fail('Restic corequirement lost');
if(restic?.pair_quality!=='STRONG') fail('Restic real followup pair lost');
console.log('LAWKIT_P12_DISCOVERY=PASS');
console.log('LAWKIT_P12_PROMOTED=NONE');
