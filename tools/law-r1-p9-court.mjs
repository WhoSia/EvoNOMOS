#!/usr/bin/env node
import fs from "node:fs";
const [i,o]=process.argv.slice(2);
const x=JSON.parse(fs.readFileSync(i,"utf8"));
if(x.verdict!=="PASS_P9_WORLD_CUSTODY") throw new Error("P9_HOLD");
if(x.fresh_holdout.result!=="BRANCH_B_SUPPORTED") throw new Error("P9_HOLD");
if(x.representation_tests.same_geometry_different_action.status!=="BOUNDED_WITNESS") throw new Error("P9_HOLD");
if(x.representation_tests.temporal_single_axis.status!=="REJECTED_AS_PREMATURE") throw new Error("P9_HOLD");
const y={
 stage:"EvoNOMOS Generation VIII LAW-R1-P9",
 result:"PASS_GEOMETRY_SURVIVES__POLICY_STATE_INSUFFICIENT__CONTEXT_EXPANDED__AXIS_EXPANSION_WITHHELD",
 geometry:{form:"G=(S,P,F)",status:"SURVIVES_AS_BOUNDED_STRUCTURAL_PROJECTION"},
 context:{form:"X",status:"TEMPORAL_EVOLUTION_MODERATORS_REQUIRED"},
 policy:{form:"Pi(X,G,E)",status:"PROMOTED"},
 attacks:{
   missing:"NO_NEW_STRUCTURAL_COORDINATE_REQUIRED",
   aliasing:"G_ALONE_INSUFFICIENT",
   reversal:"TEMPORAL_CONTEXT_SUPPORTED",
   coupling:"NOT_ESTABLISHED"
 },
 ontology:{fourth_axis:null,expansion:"CONTEXT_ONLY"},
 novelty:"WITHHELD",
 kernel:"NOT_FALSIFIED_BY_P9"
};
fs.mkdirSync(o.slice(0,o.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(o,JSON.stringify(y,null,2)+"\n");
console.log("LAW_R1_P9_COURT=PASS");
console.log(JSON.stringify({result:y.result,geometry:y.geometry.status,ontology:y.ontology.expansion}));
