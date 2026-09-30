#!/usr/bin/env node
import fs from "node:fs";

const [atlasPath,outPath]=process.argv.slice(2);
if(!atlasPath||!outPath) throw new Error("usage: court <atlas> <out>");
const a=JSON.parse(fs.readFileSync(atlasPath,"utf8"));
if(a.verdict!=="PASS_ATLAS_WORLD_CUSTODY") throw new Error("P6_HOLD atlas custody");

const fresh=a.fresh_worlds;
const by=(p,c)=>fresh.some(x=>x.principle===p && x.cell===c);

const checks={
  SRP: by("SRP","APPLY") && by("SRP","LOCAL_ABSTAIN_ON_FURTHER_SPLIT"),
  OCP: by("OCP","APPLY") && by("OCP","REVOKE"),
  LSP: by("LSP","ADMISSIBILITY_FAILURE_REPAIR") &&
       by("LSP","ADMISSIBILITY_REJECT_INCOMPATIBLE_SHARED_BASE"),
  ISP: a.existing_authority?.ISP?.apply?.authority==="LIFECYCLE_VECTOR_WORLD_CONTACT" &&
       a.existing_authority?.ISP?.boundary?.authority==="TERMINAL_NON_RESULT",
  DIP: a.existing_authority?.DIP?.authority==="LIFECYCLE_VECTOR_WORLD_CONTACT"
};
if(Object.values(checks).some(x=>!x)) throw new Error("P6_HOLD missing principle surface");

const out={
  stage:"EvoNOMOS Generation VIII LAW-R1-P6",
  status:"CROSS_PRINCIPLE_ATLAS_COMPLETE",
  checks,
  principle_roles:{
    SRP:{
      role:"CONDITIONAL_INTERVENTION_GENERATOR",
      observed_surface:"APPLY + LOCAL_ABSTAIN_ON_FURTHER_SPLIT",
      authority:"STRUCTURAL_WORLD_WITNESS",
      interpretation:"partition when ownership/change causes are separable; do not infer that every large class should be decomposed"
    },
    OCP:{
      role:"CONDITIONAL_INTERVENTION_GENERATOR",
      observed_surface:"APPLY + REVOKE",
      authority:"STRUCTURAL_WORLD_WITNESS",
      interpretation:"extension boundaries can earn authority under recurring variation and lose it when the declared extension point is not real"
    },
    LSP:{
      role:"ADMISSIBILITY_CONSTRAINT",
      observed_surface:"SUBSTITUTABILITY_REPAIR + INCOMPATIBLE_BASE_REJECT",
      authority:"STRUCTURAL_PLUS_BEHAVIORAL_WITNESS",
      interpretation:"LSP primarily gates whether a subtype/shared-base relation is admissible; it is not itself a command to introduce inheritance"
    },
    ISP:{
      role:"CONDITIONAL_INTERVENTION_GENERATOR",
      observed_surface:"LIFECYCLE APPLY + UNRESOLVED FULL-COREQUIREMENT BOUNDARY",
      authority:"P11_LIFECYCLE_SUPPORT_PLUS_P12_NONRESULT",
      interpretation:"segregation earns authority under truthful extraneous conformance burden; full corequirement remains unresolved rather than automatically abstained"
    },
    DIP:{
      role:"CONDITIONAL_INTERVENTION_GENERATOR",
      observed_surface:"INITIAL_VS_FOLLOWUP_TRADEOFF",
      authority:"LIFECYCLE_VECTOR_WORLD_CONTACT",
      interpretation:"inversion can reduce follow-up change locality while paying initial/boundary costs; no universal dominance"
    }
  },
  generalized_kernel:{
    tuple:"L=(X,A,Y,M,F,Pi,U)",
    result:"ROLE_DIFFERENTIATED_CROSS_PRINCIPLE_ATLAS_SUPPORTED",
    llm_role:"LOCAL_PROBE_ONLY",
    scalarization:false,
    universal_solid_verdict:"WITHHELD",
    universal_replacement_claim:"WITHHELD",
    novelty_status:"JOINT_OPERATIONAL_CONJUNCTION_ONLY__NOT_YET_ESTABLISHED_AS_NOVEL"
  },
  key_update:{
    principle_authority:"REVOCABLE_AND_ROLE_DEPENDENT",
    abstain:"NO_AUTHORIZED_STRUCTURAL_INTERVENTION",
    revoke:"PREVIOUS_STRUCTURAL_EXTENSION_OR_ABSTRACTION_AUTHORITY_WITHDRAWN",
    unresolved:"A boundary cell may remain unresolved without being coerced into APPLY or ABSTAIN"
  }
};

fs.mkdirSync(outPath.includes("/")?outPath.slice(0,outPath.lastIndexOf("/")):".",{recursive:true});
fs.writeFileSync(outPath,JSON.stringify(out,null,2)+"\n");
console.log("LAW_R1_P6_COURT=PASS");
console.log(JSON.stringify({
  result:out.generalized_kernel.result,
  lsp:out.principle_roles.LSP.role,
  novelty:out.generalized_kernel.novelty_status
}));
