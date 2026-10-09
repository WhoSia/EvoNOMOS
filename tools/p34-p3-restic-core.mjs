#!/usr/bin/env node
import fs from "node:fs";
import assert from "node:assert/strict";
const [root,out]=process.argv.slice(2);
assert.ok(root&&out,"usage: root output");
const terminal=JSON.parse(fs.readFileSync("lawkit/fixtures/p12-terminal-closure.json"));
const archive=JSON.parse(fs.readFileSync("lawkit/discovery/p12_candidates.json"));
const world=archive.candidates.find(x=>x.id==="RESTIC_OCI_ONEDRIVE");
const six=["save","load","stat","list","remove","delete"];
assert.equal(terminal.terminal_status,"TERMINAL_NONRESULT");
assert.equal(terminal.scientific_firewall.lifecycle_coordinates_opened,false);
assert.equal(terminal.scientific_firewall.onedrive_phase1_opened,false);
assert.deepEqual(world.bundled_capabilities.slice().sort(),six.slice().sort());
assert.deepEqual(world.demand_capabilities.slice().sort(),six.slice().sort());
const source=fs.readFileSync(root+"/internal/restic/backend.go","utf8");
const suite=fs.readFileSync(root+"/internal/backend/test/tests.go","utf8");
const counts={};
for(const c of six){
 const m=c[0].toUpperCase()+c.slice(1);
 assert.ok(source.includes(m+"("),"missing public Backend method "+m);
 counts[m]=suite.split("."+m+"(").length-1;
 assert.ok(counts[m]>0,"missing conformance call "+m);
}
const result={
 schema:"P34_P3_RESTIC_SOURCE_CAPABILITY_CONTRAST_V1",
 source_revision:world.exact_pre_demand_commit,
 real_demand_issues:[world.issue,world.followup_issue],
 required_methods:six,source_conformance_selector_counts:counts,
 P11_extra_capability_mismatch:1,P12_extra_capability_mismatch:0,
 P12_scientific_outcome:"TERMINAL_NONRESULT",OneDrive_phase1:"UNOPENED",
 evidence_ceiling:"Lexical source-method/conformance evidence, not experimental treatment execution",
 conditional_finding:"Mismatch-derived excess conformance disappears in full six-of-six demand; composed-backend costs remain unidentified",
 winner:null,verdict:"P34_P3_RESTIC_SOURCE_CO_REQUIREMENT_PASS__P12_OUTCOME_HOLD"
};
fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n");
console.log("P34_RESTIC_SOURCE_CO_REQUIREMENT=PASS");
