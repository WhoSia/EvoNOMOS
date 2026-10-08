#!/usr/bin/env node
// Exact historical OOP structure-source audit. Not a maintenance-law trial.
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import {execFileSync} from "node:child_process";
const [baseDir, sharedDir, outFile]=process.argv.slice(2);
if(!baseDir||!sharedDir)throw Error("Usage: node law-r1-p31-swamp-structural-pair-audit.mjs base shared [receipt]");
const refs={
 direct:"a1f174e425d3c68ac0ef6c9c8307814e5d8b4227",
 shared:"775bf53ac4dcf1234121fbe4f827704f58d216ee"
};
const run=(cwd,args)=>execFileSync("git",["-C",cwd,...args],{encoding:"utf8"}).trim();
assert.equal(run(baseDir,["rev-parse","HEAD"]),refs.direct);
assert.equal(run(sharedDir,["rev-parse","HEAD"]),refs.shared);
assert.equal(run(sharedDir,["rev-parse","HEAD^"]),refs.direct);
const file=(dir,rel)=>fs.readFileSync(path.join(dir,rel),"utf8");
const bSync=file(baseDir,"sync/company.go"),sSync=file(sharedDir,"sync/company.go");
const bTui=file(baseDir,"tui/app.go"),sTui=file(sharedDir,"tui/app.go");
const bFilter=file(baseDir,"filter/filter.go"),sFilter=file(sharedDir,"filter/filter.go");
const bSelect=file(baseDir,"tui/filter_select.go"),sSelect=file(sharedDir,"tui/filter_select.go");
assert.match(bSync,/func toFilterRules\(filters \[\]store\.CompanyFilter\)/);
assert.doesNotMatch(bSync,/func FilterRules\(/);
assert.match(sSync,/func FilterRules\(filters \[\]store\.CompanyFilter\)/);
assert.match(bTui,/func narrowPostingsToFilters\(/);
assert.match(sTui,/func filterPostingsByCompanyFilters\(/);
assert.match(sTui,/sync\.FilterRules\(/);
assert.match(bTui,/filter\.Match\(fp, rules\)/);
assert.match(sFilter,/FieldDepartment\s*=\s*"department"/);
assert.match(sFilter,/FieldLocation\s*=\s*"location"/);
assert.doesNotMatch(bFilter,/FieldDepartment\s*=\s*"department"/);
assert.match(bTui,/case "department":/);
assert.match(bTui,/case "location":/);
assert.match(sTui,/case filter\.FieldDepartment:/);
assert.match(sTui,/case filter\.FieldLocation:/);
assert.match(bSelect,/"department"/);
assert.match(sSelect,/filter\.FieldDepartment/);
const changed=run(sharedDir,["diff-tree","--no-commit-id","--name-only","-r","HEAD"]).split("\n");
for(const required of ["filter/filter.go","sync/company.go","tui/app.go","tui/app_test.go","tui/filter_select.go"])assert.ok(changed.includes(required));
const postErrorBlock=sTui.slice(sTui.indexOf("func filterPostingsByCompanyFilters"),sTui.indexOf("func narrowPostingsToFilters"));
assert.match(postErrorBlock,/return nil, err/);
const output={
 stage:"G8 LAW-R1-P31",
 verdict:"PASS_HISTORICAL_DIRECT_SHARED_OOP_SOURCE_TOPOLOGY__SEMANTIC_DOMAIN_CONFOUND_PRESERVED__NO_CAUSAL_LIFECYCLE_CLAIM",
 world:"dklassen/swamp#61",
 revision_pair:refs,
 source_diff_paths:changed,
 direct_conversion:"independent ingestion/display transformation responsibilities",
 shared_conversion:"exported sync.FilterRules and delegated display filtering",
 valid_field_domain:["department","location"],
 semantics_outside_domain:"invalid/unsupported fields may follow different handling; cannot claim total equivalence",
 source_test_results:"CI owns actual Go test outcomes; this static checker does not certify tests",
 distinct_experiment_needed:"new frozen Team filter requirement, two realized architectural variants on a common source-independent requirement",
 p31_closed:false,law_r2_authorized:false
};
console.log(JSON.stringify(output,null,2));
if(outFile)fs.writeFileSync(outFile,JSON.stringify(output,null,2)+"\n");
