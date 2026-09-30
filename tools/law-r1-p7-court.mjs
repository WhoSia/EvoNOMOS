#!/usr/bin/env node
import fs from "node:fs";
const [inp,outp]=process.argv.slice(2);
const x=JSON.parse(fs.readFileSync(inp,"utf8"));
if(x.verdict!=="PASS_WORLD_CUSTODY_AND_OUT_OF_STREAM_CHALLENGE") throw new Error("P7_HOLD");
if(x.holdout_result.prediction!=="SUPPORTED") throw new Error("P7_HOLDOUT_FAIL");
const out={
 stage:"EvoNOMOS Generation VIII LAW-R1-P7",
 result:"PASS_DISCOVERY_LOOP__GENERIC_SSOT_NOVELTY_KILLED__CONDITIONAL_GENERATOR_ABSORBED",
 generalized_kernel:"NOT_FALSIFIED_BY_P7",
 discovered_generator:{
   name:"SEMANTIC_AUTHORITY_CONVERGENCE",
   status:"ABSORB_EXISTING_FAMILY__CONDITIONAL_SCOPE_REFINED",
   rule:"IF multiple independently editable paths encode or mutate the same semantic authority AND observed burden is drift/reconciliation, THEN test convergence onto one behavioral authority; UNLESS paths encode intentionally distinct semantics, independent evolution is intended, or secondary representations are mechanically derived/read-only.",
   authority:"THREE_DISCOVERY_WORLDS_PLUS_ONE_FRESH_HOLDOUT__NO_UNIVERSAL_LAW"
 },
 novelty:{
   generic_ssot:"RETIRED",
   deduplicate_everything:"REJECTED",
   evonomos_claim:"DISCOVERY_AUTHORITY_LOOP_ONLY__NOVELTY_WITHHELD"
 },
 epistemic_update:{
   success_means:"the kernel may rediscover, absorb, narrow or kill candidate generators; invention is not required",
   llm_role:"LOCAL_PROBE_ONLY",
   world_contact:"PRIMARY"
 }
};
fs.mkdirSync(outp.includes("/")?outp.slice(0,outp.lastIndexOf("/")):".",{recursive:true});
fs.writeFileSync(outp,JSON.stringify(out,null,2)+"\n");
console.log("LAW_R1_P7_COURT=PASS");
console.log(JSON.stringify({result:out.result,generator:out.discovered_generator.status,kernel:out.generalized_kernel}));
