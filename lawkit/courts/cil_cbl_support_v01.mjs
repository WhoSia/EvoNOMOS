#!/usr/bin/env node
import fs from 'node:fs';
const [measurementPath,outPath]=process.argv.slice(2);
if(!measurementPath||!outPath){console.error('usage: cil_cbl_support_v01.mjs <measurement.json> <out.json>');process.exit(1);}
const m=JSON.parse(fs.readFileSync(measurementPath,'utf8'));
const W=m.arms.WIDE_BOUNDARY_REUSE,S=m.arms.CAPABILITY_SEGREGATED;
const fail=x=>{console.error('LAW_COURT_HOLD '+x);process.exit(1);};
for(const a of [W,S]) if(a.phase0.Q!==1||a.phase1.Q!==1) fail('Q gate');
const keys=['S','L','C','A'],delta=(p,k)=>S[p][k]-W[p][k];
const pareto=p=>{const d=keys.map(k=>delta(p,k));if(d.every(x=>x===0))return'EQUAL';if(d.every(x=>x<=0)&&d.some(x=>x<0))return'CAPABILITY_SEGREGATED_PARETO_DOMINATES_PHASE';if(d.every(x=>x>=0)&&d.some(x=>x>0))return'WIDE_BOUNDARY_REUSE_PARETO_DOMINATES_PHASE';return'TRADEOFF';};
const dS0=delta('phase0','S'),dS1=delta('phase1','S');
let cil;if(dS0>0&&dS1<0)cil='BIRTH_TAX_THEN_LATER_SURFACE_SAVING';else if(dS0<=0&&dS1<0)cil='LATER_SURFACE_SAVING_WITHOUT_BIRTH_TAX';else if(dS1===0)cil='NO_LATER_MEMBERSHIP_SURFACE_DISCRIMINATION';else cil='LATER_SURFACE_COST';
const cilAuthority=cil==='BIRTH_TAX_THEN_LATER_SURFACE_SAVING'?'SUPPORT_DOMAIN_EXTENDED__BOUNDARY_PRESENT__REAL_FOLLOWUP':cil==='LATER_SURFACE_SAVING_WITHOUT_BIRTH_TAX'?'MECHANISM_MODIFIED__LATER_SAVING_WITHOUT_PREDECLARED_BIRTH_TAX':'BOUNDARY_EVIDENCE__NO_CIL_SUPPORT_EXTENSION';
const cbl=W.phase0.C>S.phase0.C&&W.phase1.C>S.phase1.C;
const dL0=delta('phase0','L'),dL1=delta('phase1','L');
let churn='NO_SIGN_REVERSAL';if(dL0>0&&dL1<0)churn='BIRTH_TAX_THEN_LATER_CHURN_SAVING';else if(dL0<0&&dL1>0)churn='EARLY_CHURN_SAVING_THEN_LATER_COST';else if(dL0===0&&dL1===0)churn='NO_CHURN_DIFFERENCE';
const out={stage:m.stage,status:'LAW_SUPPORT_DOMAIN_COURT_COMPLETE',deltas:{phase0:Object.fromEntries(keys.map(k=>[k,delta('phase0',k)])),phase1:Object.fromEntries(keys.map(k=>[k,delta('phase1',k)]))},pareto:{phase0:pareto('phase0'),phase1:pareto('phase1')},'CIL-C1':{classification:cil,authority:cilAuthority,universal_law_validation:'WITHHELD'},'CBL-C1':{mechanism_support:cbl,authority:cbl?'MECHANISTIC_SUPPORT_EXTENDED__TWO_REAL_SEARCH_ONLY_DEMANDS__NO_DESIGN_RECOMMENDATION':'CBL_MECHANISM_NOT_SUPPORTED_IN_THIS_WORLD',design_recommendation:'WITHHELD'},churn_relation:churn,scalarization:false,winner:null};
fs.mkdirSync(outPath.includes('/')?outPath.slice(0,outPath.lastIndexOf('/')):'.',{recursive:true});fs.writeFileSync(outPath,JSON.stringify(out,null,2)+'\n');
console.log('CIL_CBL_COURT=PASS');console.log(JSON.stringify({cil:out['CIL-C1'],cbl:out['CBL-C1'],pareto:out.pareto,churn_relation:out.churn_relation,winner:null}));
