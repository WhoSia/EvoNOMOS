#!/usr/bin/env node
import fs from "node:fs";
const [inp,outp]=process.argv.slice(2);
const x=JSON.parse(fs.readFileSync(inp,"utf8"));
if(x.verdict!=="PASS_MULTI_MOTIF_WORLD_CUSTODY") throw new Error("P8_HOLD");

if(x.motif_A.axis===x.motif_B.axis || x.motif_A.axis===x.motif_C.axis || x.motif_B.axis===x.motif_C.axis){
  throw new Error("P8_HOLD_AXIS_COLLAPSE");
}
if(x.motif_B.stacks_discriminator.discriminator!=="SUPPORTED_SUBSTRATE_SPLIT") throw new Error("P8_HOLD_B");
if(x.motif_C.hermes.role!=="UNRESOLVED_COMPOSITION_WORLD") throw new Error("P8_HOLD_C");

const out={
  stage:"EvoNOMOS Generation VIII LAW-R1-P8",
  result:"PASS_MULTI_MOTIF_ECOLOGY__ORTHOGONAL_AXIS_COMPOSITION_SUPPORTED__COMPONENT_NOVELTY_KILLED",
  motifs:{
    A:{
      name:"SEMANTIC_AUTHORITY_CONVERGENCE",
      axis:"S_SEMANTIC_AUTHORITY_CARDINALITY",
      status:"ABSORB_EXISTING_FAMILY__CONDITIONAL_SCOPE_REFINED",
      intervention:"reduce independently editable owners only when paths encode the same semantic authority and drift/reconciliation is observed"
    },
    B:{
      name:"INVARIANT_CLOSURE_BY_SUBSTRATE",
      axis:"F_FAILURE_CLOSURE_BOUNDARY",
      status:"ABSORB_EXISTING_FAMILY__SUBSTRATE_MODERATOR_EXPLICIT",
      intervention:"close invariant-coupled durable effects using one transaction when a shared substrate exists; otherwise use retry-safe/idempotent/compensating/reconciliation mechanisms; leave non-invariant effects outside"
    },
    C:{
      name:"OPERATIONAL_AUTHORITY_SCOPE_PARTITIONING",
      axis:"P_OPERATIONAL_AUTHORITY_SCOPE",
      status:"ABSORB_EXISTING_FAMILY__FAILURE_DOMAIN_MODERATOR_EXPLICIT",
      intervention:"narrow capability/credential authority to the principal or failure domain that needs it while retaining genuinely shared authorities when semantics require sharing"
    }
  },
  competition:{
    scalar_winner:null,
    ruling:"NOT_TRUE_RIVALS_WHEN_AXES_ARE_SEPARATED",
    false_conflict:"centralize-versus-partition is ill-posed unless semantic ownership and operational access are distinguished",
    unresolved_world:"Hermes #108671 remains open; composition implementation is not claimed"
  },
  composition:{
    representation:"THREE_AXIS_AUTHORITY_GEOMETRY",
    axes:{
      S:"semantic-authority cardinality",
      P:"operational-authority scope",
      F:"invariant/failure closure"
    },
    supported_relations:[
      "low S + narrow P is coherent: one canonical truth with scoped access",
      "F is substrate-moderated and can use atomic commit or retry/compensation without changing S or P",
      "the same system may centralize truth, partition capability, and close only invariant-coupled effects"
    ],
    status:"SUPPORTED_AS_BOUNDED_COMPOSITION_REPRESENTATION__NOT_A_NEW_UNIVERSAL_PRINCIPLE"
  },
  novelty:{
    A:"RETIRED_GENERIC_SSOT",
    B:"RETIRED_ACID_OUTBOX_SAGA_IDEMPOTENCY_FAMILY",
    C:"RETIRED_LEAST_PRIVILEGE_BULKHEAD_FAMILY",
    composition:"NOVELTY_WITHHELD"
  },
  generalized_kernel:{
    status:"NOT_FALSIFIED_BY_P8",
    update:"kernel now requires motif-axis typing before generator competition or composition",
    llm_role:"LOCAL_PROBE_ONLY",
    world_contact:"PRIMARY"
  }
};
fs.mkdirSync(outp.includes("/")?outp.slice(0,outp.lastIndexOf("/")):".",{recursive:true});
fs.writeFileSync(outp,JSON.stringify(out,null,2)+"\n");
console.log("LAW_R1_P8_COURT=PASS");
console.log(JSON.stringify({result:out.result,composition:out.composition.status,kernel:out.generalized_kernel.status}));
