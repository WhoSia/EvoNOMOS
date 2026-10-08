#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import {execFileSync} from "node:child_process";
const [before,after,receipt]=process.argv.slice(2);
if(!before||!after)throw Error("Usage: node ... OLD_TREE NEW_TREE [JSON]");
const old="6d48e3b3aa3a21baea44e05b8b0aa8f731fe0fd6";
const fix="fb9c0e7e675de70035e556b9ba579d1e8f602da1";
const git=(dir,...args)=>execFileSync("git",["-C",dir,...args],{encoding:"utf8"}).trim();
assert.equal(git(before,"rev-parse","HEAD"),old);
assert.equal(git(after,"rev-parse","HEAD"),fix);
assert.equal(git(after,"rev-parse","HEAD^"),old);
const get=(dir,rel)=>fs.readFileSync(path.join(dir,rel),"utf8");
const o=get(before,"internal/provider/provider.go"),n=get(after,"internal/provider/provider.go");
assert.match(o,/type Interface interface \{/);
for(const sym of ["Name()","Kind()","Description()","Dependencies()","DefaultPalette()","Load("])assert.ok(o.includes(sym),sym);
assert.match(n,/type MetricDescriptor struct \{/);
assert.match(n,/type Loader interface \{/);
assert.doesNotMatch(n.slice(n.indexOf("type MetricDescriptor struct"),n.indexOf("type Loader interface")) ,/Load\(/);
assert.match(n.slice(n.indexOf("type Loader interface")) ,/Load\(root \*model\.Directory\) error/);
const or=get(before,"internal/provider/registry.go"),nr=get(after,"internal/provider/registry.go");
assert.match(or,/providers map\[metric.Name\]Interface/);
assert.match(nr,/entries map\[metric.Name\]registration/);
assert.match(nr,/descriptor MetricDescriptor/);
assert.match(nr,/loader\s+Loader/);
const changed=git(after,"diff-tree","--no-commit-id","--name-only","-r","HEAD").split("\n");
assert.ok(changed.includes("cmd/codeviz/help_metrics_cmd.go"));
assert.ok(changed.includes("internal/provider/run.go"));
assert.ok(changed.includes("internal/provider/registry_test.go"));
const out={stage:"G8 LAW-R1-P31",verdict:"PASS_INDEPENDENT_PROVIDER_CAPABILITY_TOPOLOGY_SOURCE_ONLY__LIFECYCLE_EFFECT_NOT_TESTED",
world:"theunrepentantgeek/code-visualizer#162",before:old,after:fix,
changed_paths:changed,pre:{provider_combines_metadata_and_Load:true},post:{descriptor_has_Load:false,loader_has_Load:true,registry_pairs_descriptor_and_loader:true},
source_root_equivalent:"NOT_PROVEN",new_functional_demand:"NOT_EXECUTED",cross_world_law:"NOT_AUTHORIZED",p31_closed:false,law_r2_authorized:false};
console.log(JSON.stringify(out,null,2));if(receipt)fs.writeFileSync(receipt,JSON.stringify(out,null,2)+"\n");
