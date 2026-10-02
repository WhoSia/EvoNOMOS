#!/usr/bin/env node
import fs from "node:fs";
const [i,o]=process.argv.slice(2);
const x=JSON.parse(fs.readFileSync(i,"utf8"));
if(x.verdict!=="PASS_P10_WORLD_CUSTODY") throw new Error("HOLD");
if(x.tests.matched_geometry_reversal!=="SUPPORTED_BOUNDED") throw new Error("HOLD");
if(x.tests.matched_context_discrimination!=="SUPPORTED_DEVELOPMENT") throw new Error("HOLD");
if(x.tests.interaction_nonseparability!=="SUPPORTED_BOUNDED") throw new Error("HOLD");
if(x.tests.same_X_G_E_distinct_action!=="NOT_OBSERVED") throw new Error("R2_GATE");
const y={
 stage:"EvoNOMOS Generation VIII LAW-R1-P10",
 result:"PASS_INTERACTION_REQUIRED__STATE_FACTORIZATION_SURVIVES__POLICY_SEPARABILITY_REJECTED__R2_NOT_AUTHORIZED",
 state:"X_G_E_SUFFICIENT",
 policy:"INTERACTION_BEARING",
 r2:"NOT_AUTHORIZED",
 kernel:"NOT_FALSIFIED"
};
fs.mkdirSync(o.slice(0,o.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(o,JSON.stringify(y,null,2)+"\n");
console.log("LAW_R1_P10_COURT=PASS");
console.log(JSON.stringify(y));
