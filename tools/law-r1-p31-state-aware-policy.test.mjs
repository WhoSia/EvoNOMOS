#!/usr/bin/env node
import assert from "node:assert/strict";
import {decide} from "./law-r1-p31-state-aware-policy.mjs";
const base={
 source_commit:"f3d536d37825302e31ed0eddd811c689f38f85a3",
 sqlite_version:"3.46.1",
 fixture_scope:"DISPOSABLE_TEST_DATABASE",
 schema:"events(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)",
 visible_row_count:0,
 allocator_measurement:"DIRECT_PRE_ACTION_SQLITE_SEQUENCE",
 transaction_exclusivity:"EXCLUSIVE_TEST_WINDOW"
};
let selectedReserve=0,selectedNoop=0;
for(const minimum_next_id of [5,9])for(const high_water of [0,3,7,11]){
 const d=decide({...base,minimum_next_id,high_water});
 assert.equal(d.status,"ADMISSIBLE_FROZEN_GRID");
 const bit=Number(high_water+1<minimum_next_id);
 assert.equal(d.state_feature.value,bit);
 assert.equal(d.selected_action,bit?"RESERVE":"NOOP");
 assert.equal(d.selected_extra_write_transactions,bit);
 assert.equal(d.predicted_future_id.NOOP,high_water+1);
 assert.equal(d.predicted_future_id.RESERVE,Math.max(high_water,minimum_next_id-1)+1);
 assert.equal(d.execution_performed,false);
 assert.equal(d.law_r2_authorized,false);
 if(bit)selectedReserve++;else selectedNoop++;
}
assert.deepEqual([selectedReserve,selectedNoop],[5,3]);
const invalid=[
 ["source_commit","wrong"],["sqlite_version","3.45.3"],
 ["fixture_scope","PRODUCTION"],["schema","unknown"],
 ["visible_row_count",1],["allocator_measurement","INFERRED_FROM_FUTURE_Y"],
 ["transaction_exclusivity","UNCONTROLLED"],["high_water",100],
 ["minimum_next_id",20],["high_water",null]
];
for(const [field,value] of invalid){
 const d=decide({...base,high_water:3,minimum_next_id:5,[field]:value});
 assert.equal(d.status,"ABSTAIN");
 assert.equal(d.actions_permitted,false);
 assert.ok(d.reasons.length>0);
}
assert.equal(decide(null).status,"ABSTAIN");
console.log("P31_POLICY_DECISION_GRID=8/8 PASS");
console.log("P31_POLICY_ABSTENTION_REGRESSIONS=11/11 PASS");
console.log("P31_POLICY_WORLD_EVIDENCE=NOT_CLAIMED");
