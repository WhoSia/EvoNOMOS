#!/usr/bin/env node
import fs from "node:fs";

const [measurementPath,outPath]=process.argv.slice(2);
if(!measurementPath||!outPath) throw new Error("usage: court <measurement> <out>");
const m=JSON.parse(fs.readFileSync(measurementPath,"utf8"));
const D=m.arms.DISPERSED_MEMBERSHIP_EXTENSION;
const R=m.arms.DUAL_RUNTIME_MEMBERSHIP_REGISTRY;
const fail=x=>{throw new Error("LAW_R1_P3_HOLD "+x);};

for(const a of [D,R]){
  if(a.phase0.Q!==1||a.phase1.Q!==1) fail("Q gate");
}
if(m.oracle_strength.scope!=="BOUNDED_NO_NETWORK"||m.oracle_strength.production_external_api_authority!==false) fail("oracle-strength contract");

const keys=["S","L","C","A"];
const delta=(phase,key)=>R[phase][key]-D[phase][key];
const d0=Object.fromEntries(keys.map(k=>[k,delta("phase0",k)]));
const d1=Object.fromEntries(keys.map(k=>[k,delta("phase1",k)]));

let classification,authority;
if(d1.S<0){
  if(d0.S<0 && d0.A>0){
    classification="IMMEDIATE_AND_LATER_MEMBERSHIP_SURFACE_SAVING_WITH_ARCHITECTURE_BIRTH_TAX";
  } else if(d0.S>0){
    classification="MEMBERSHIP_BIRTH_TAX_THEN_LATER_SURFACE_SAVING";
  } else if(d0.S===0){
    classification="LATER_MEMBERSHIP_SURFACE_SAVING_WITH_NEUTRAL_PHASE0_S";
  } else {
    classification="LATER_MEMBERSHIP_SURFACE_SAVING";
  }
  authority="CIL_C1_SUPPORT_EXTENDED__BOUNDARY_SCOPE_REFINED__TWO_REAL_DEMANDS__BOUNDED_NO_NETWORK";
} else if(d1.S===0){
  classification="NO_LATER_MEMBERSHIP_SURFACE_DISCRIMINATION";
  authority="CIL_C1_NOT_EXTENDED_IN_THIS_WORLD";
} else {
  classification="LATER_MEMBERSHIP_SURFACE_COST";
  authority="CIL_C1_CHALLENGED_IN_THIS_WORLD";
}

let lRelation;
if(d0.L>0&&d1.L<0) lRelation="L_BIRTH_TAX_THEN_LATER_SAVING";
else if(d0.L<0&&d1.L<0) lRelation="L_SAVING_BOTH_PHASES";
else if(d0.L<0&&d1.L>0) lRelation="L_EARLY_SAVING_THEN_LATER_COST";
else if(d0.L===0&&d1.L===0) lRelation="L_NO_DIFFERENCE";
else lRelation="L_MIXED_OR_NONREVERSING";

const out={
  stage:m.stage,
  status:"LAW_R1_P3_COURT_COMPLETE",
  deltas:{phase0:d0,phase1:d1},
  "CIL-C1":{
    classification,
    authority,
    mechanism:"membership-authority propagation only",
    l_saving_required:false,
    universal_design_law_validation:"WITHHELD"
  },
  "CBL-C1":{
    classification:"NOT_APPLICABLE_SINGLETON_MANDATORY_SEND_CONTRACT",
    authority:"UNCHANGED",
    falsifier_cell_update:"NONE"
  },
  churn_relation:lRelation,
  oracle_strength_boundary:{
    established:"BOUNDED_NO_NETWORK",
    production_external_api_equivalence:"UNESTABLISHED"
  },
  scalarization:false,
  winner:null,
  architecture_recommendation:"WITHHELD",
  solid_dip_ocp_validation:"WITHHELD"
};
fs.mkdirSync(outPath.includes("/")?outPath.slice(0,outPath.lastIndexOf("/")):".",{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+"\n");
console.log("LAW_R1_P3_COURT=PASS");
console.log(JSON.stringify({classification,authority,deltas:out.deltas,churn_relation:lRelation,winner:null}));
