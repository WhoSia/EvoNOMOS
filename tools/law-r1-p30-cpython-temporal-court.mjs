#!/usr/bin/env node
import fs from "node:fs";
const r=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
const a=r.arm_a.before,b=r.arm_b.before;
const same=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
const w=x=>({Q:x.Q,R:x.R,G:x.G,H_pending_length:x.H_pending_length});
const matched=same(w(a),w(b));
const passive=r.current_equal && a.O_now==="" && b.O_now==="";
const split=r.future_different;
const rescued=r.prospective_pending_content_separates && a.H_pending_hex!==b.H_pending_hex;
let verdict="HOLD_NO_ADMISSIBLE_TEMPORAL_COLLISION";
if(!matched || !passive) verdict="HOLD_PRECOMMITTED_STATE_OR_PASSIVE_MISMATCH";
else if(split && rescued) verdict="PASS_TEMPORAL_PREDICTIVE_COLLISION_AT_COARSE_W__PROSPECTIVE_PENDING_CONTENT_REFINEMENT__LAW_R2_NOT_AUTHORIZED";
else if(split) verdict="PASS_TEMPORAL_PREDICTIVE_COLLISION_AT_COARSE_W__REFINEMENT_UNRESOLVED__LAW_R2_NOT_AUTHORIZED";
const out={stage:"G8 LAW-R1-P30",matched_W:matched,passive_match:passive,future_split:split,prospective_pending_content_rescue:rescued,verdict,law_r2_authorized:false,claim_ceiling:"Only the frozen CPython decoder grain. No persistent ontology failure or transport."};
console.log(JSON.stringify(out,null,2));
if(process.argv[3])fs.writeFileSync(process.argv[3],JSON.stringify(out,null,2)+"\n");
if(verdict.startsWith("HOLD"))process.exitCode=3;
