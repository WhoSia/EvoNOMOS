#!/usr/bin/env node
// P34-P2: source-pinned P11 original receipt and finite client contracts.
// Finite abstract checks are NOT a replay of original TypeScript experiments.
import fs from "node:fs";
import assert from "node:assert/strict";
import path from "node:path";
const [history="historical",donor="trueforge",out="out/p34-p11.json"]=process.argv.slice(2);
const base=history+"/active/g8-origin-r1-p11-p3/";
const read=s=>JSON.parse(fs.readFileSync(base+s,"utf8"));
const seal=read("receipts/P3_TERMINAL.json");
const contract=read("inherited/DUAL_REAL_DEMAND_CONTRACT.json");
const rival=read("inherited/RIVAL_CONSTITUTION.json");
const oracle=read("inherited/SEARCH_FETCH_EXPOSURE_ORACLE.json");
assert.equal(seal.source,contract.world.exact_source);
assert.equal(seal.actions.canonical_run.id,36382197510);
assert.equal(seal.p11_closed,true);
assert.equal(seal.winner,null);
assert.deepEqual(seal.vectors.coordinate_order,["S","L","C","A","Q"]);
assert.deepEqual(contract.phase0.required_capabilities,["search"]);
assert.deepEqual(contract.phase1.required_capabilities,["search"]);
assert.ok(rival.treatments.WIDE_BOUNDARY_REUSE);
assert.ok(oracle.forbidden_successes.some(v=>v.includes("unsupported")));
const iface=fs.readFileSync(donor+"/packages/trueforge-core/src/core/web-search/WebSearchProvider.ts","utf8");
assert.ok(iface.includes("interface IWebSearchProvider"));
assert.ok(iface.includes("search(input:")&&iface.includes("fetch(input:"));
const owners=fs.readFileSync(donor+"/.github/CODEOWNERS","utf8");
const contributing=fs.readFileSync(donor+"/CONTRIBUTING.md","utf8");
const wildcard=owners.split("\n").find(x=>x.startsWith("* @"));
assert.ok(wildcard.includes("@heerambavi1998"));
assert.ok(contributing.includes("approval from a maintainer"));
const arms=["WIDE_BOUNDARY_REUSE","CAPABILITY_SEGREGATED"];
const phases=[["phase0",["parallel","exa"]],["phase1",["parallel","exa","tavily"]]];
const cases=[];
for(const [phase,providers] of phases)for(const provider of providers)for(const arm of arms){
 const advertised=provider==="parallel"||arm===arms[0]?["search","fetch"]:["search"];
 for(const client of ["search","search_fetch"]){
  const required=client==="search"?["search"]:["search","fetch"];
  const admissible=required.every(x=>advertised.includes(x));
  cases.push({phase,provider,arm,client,advertised,admissible,
   trace:["configure:"+provider,...advertised.flatMap(t=>["advertise:"+t,"invoke:"+t,"success:"+t])]});
  assert.equal(admissible,client==="search"||arm===arms[0]||provider==="parallel");
 }
}
assert.equal(cases.length,20);
const v=seal.vectors;
const delta=p=>v[arms[1]][p].map((n,i)=>n-v[arms[0]][p][i]);
assert.deepEqual(delta("phase0"),[0,27,-1,0,0]);
assert.deepEqual(delta("phase1"),[0,-31,-1,0,0]);
for(const arm of arms)for(const [phase] of phases){
 assert.equal(v[arm][phase][4],1);
 assert.equal(v[arm][phase][2],arm===arms[0]?1:0);
}
assert.equal(seal.pareto.phase0,"TRADEOFF");
assert.equal(seal.pareto.phase1,"CAPABILITY_SEGREGATED_PARETO_DOMINATES_PHASE");
const result={
 schema:"P34_P11_TEMPORAL_RECONSTITUTION_V1",
 historical_sha:"e2e5a2e43c899e9e3574b615ba2375b32d0895fb",
 donor_sha:seal.source,
 original_run:seal.actions.canonical_run.id,
 vectors:v,delta:{phase0:delta("phase0"),phase1:delta("phase1")},
 pareto:seal.pareto,cases,
 codeowners_core_wildcard:wildcard,
 governance_claim:"Code owners named and maintainer-approval policy present; pre-demand PR reviews independently checked; branch-protection enforcement NOT verified",
 interpretation:"Both arms meet demand search and own truthful advertised-capability contracts; SEG is not substitutable under a stronger all-provider fetch client for Exa/Tavily; this does not mean SEG breaks the actual search-only requirement.",
 restriction:"Abstract trace model from frozen receipts, NOT treatment re-execution or full temporal interface automata",
 ruling:"P34_ORIGIN_P11_RECONSTITUTED__CLIENT_RELATIVE_LSP_ISP_PASS__GOVERNANCE_PARTIAL__LAW_R2_HOLD"
};
fs.mkdirSync(path.dirname(out),{recursive:true});
fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n");
console.log(JSON.stringify({PASS:true,cases:cases.length,p0:delta("phase0"),p1:delta("phase1")}));
