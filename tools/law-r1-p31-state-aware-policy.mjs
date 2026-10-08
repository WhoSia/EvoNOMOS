#!/usr/bin/env node
// Research-only prospective P31 policy evaluator; NEVER mutates a database.
// Abstains outside the source-pinned disposable-fixture experiment.
import fs from "node:fs";

const SOURCE="f3d536d37825302e31ed0eddd811c689f38f85a3";
const HS=new Set([0,3,7,11]), MS=new Set([5,9]);
export function decide(input){
 const problems=[];
 if(!input || typeof input!=="object")return {status:"ABSTAIN",reasons:["INVALID_INPUT"]};
 if(input.source_commit!==SOURCE)problems.push("SOURCE_UNVERIFIED");
 if(input.sqlite_version!=="3.46.1")problems.push("RUNTIME_UNVERIFIED");
 if(input.fixture_scope!=="DISPOSABLE_TEST_DATABASE")problems.push("UNSUPPORTED_DEPLOYMENT");
 if(input.schema!=="events(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)")problems.push("SCHEMA_NOT_ADMITTED");
 if(input.visible_row_count!==0)problems.push("NONEMPTY_PUBLIC_STATE");
 if(input.allocator_measurement!=="DIRECT_PRE_ACTION_SQLITE_SEQUENCE")problems.push("H_PROVENANCE_UNVERIFIED");
 if(input.transaction_exclusivity!=="EXCLUSIVE_TEST_WINDOW")problems.push("CONCURRENT_CONTEXT_UNCONTROLLED");
 const h=input.high_water,m=input.minimum_next_id;
 if(!Number.isSafeInteger(h)||!HS.has(h))problems.push("OUT_OF_SUPPORT_HIGH_WATER");
 if(!Number.isSafeInteger(m)||!MS.has(m))problems.push("OUT_OF_SUPPORT_DEMAND");
 if(problems.length)return {status:"ABSTAIN",reasons:problems,actions_permitted:false};
 const bit=Number(h+1<m);
 return {
  status:"ADMISSIBLE_FROZEN_GRID",
  state_feature:{name:"needs_high_water_reservation",value:bit,bits:1},
  selected_action:bit?"RESERVE":"NOOP",
  predicted_future_id:{NOOP:h+1,RESERVE:Math.max(h,m-1)+1},
  expected_threshold_violations:{NOOP:Number(h+1<m),RESERVE:0},
  expected_extra_write_transactions:{NOOP:0,RESERVE:1},
  selected_extra_write_transactions:bit,
  evidence_scope:"Hypothesis and bounded policy on prospective SQLite 3.46.1 fixture grid only",
  execution_performed:false,
  law_r2_authorized:false
 };
}
if(process.argv[1] && import.meta.url.endsWith(process.argv[1].replaceAll("\\","/"))){
 if(!process.argv[2])throw Error("Usage: node law-r1-p31-state-aware-policy.mjs CONTEXT.json");
 const context=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
 process.stdout.write(JSON.stringify(decide(context),null,2)+"\n");
}
