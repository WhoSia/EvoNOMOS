#!/usr/bin/env node
// P31 observational sieve: execute elementary factorization / partition-refinement
// checks against the EXACT previous P3 terminal seal. No empirical law promotion.
import { readFileSync } from "node:fs";
import assert from "node:assert/strict";

const p3 = JSON.parse(readFileSync(new URL("../active/g8-law-r1-p3/P3_TERMINAL_SEAL.json",import.meta.url),"utf8"));
const actions=["DISPERSED_MEMBERSHIP_EXTENSION","DUAL_RUNTIME_MEMBERSHIP_REGISTRY"];
const phases=["phase0","phase1"];
const outputs=["S","L","C","A"];
function cost(a,phase) {
 const v=p3.vectors[a][phase];
 assert.equal(v.length,5);
 return {feasible:v[4]===1,values:v.slice(0,4)};
}
function dominates(b,a) {
 return b.values.every((x,i)=>x<=a.values[i]) && b.values.some((x,i)=>x<a.values[i]);
}
function pareto(phase) {
 const eligible=actions.filter(a=>cost(a,phase).feasible);
 return eligible.filter(a=>!eligible.some(b=>b!==a&&dominates(cost(b,phase),cost(a,phase))));
}
function groups(contexts,alpha) {
 const g=new Map();
 for(const x of contexts) {
  const z=alpha(x);
  if(!g.has(z))g.set(z,[]);
  g.get(z).push(x);
 }
 return g;
}
function eq(a,b) {return JSON.stringify([...a].sort())===JSON.stringify([...b].sort());}
function factorization(contexts,alpha,frontier) {
 for(const [key,fiber] of groups(contexts,alpha)) {
  for(let i=1;i<fiber.length;i++) {
   if(!eq(frontier(fiber[0]),frontier(fiber[i]))) {
    return {lossless:false,witness:{key,left:fiber[0],right:fiber[i],leftPareto:frontier(fiber[0]),rightPareto:frontier(fiber[i])}};
   }
  }
 }
 return {lossless:true,witness:null};
}
function minimalObservedRepair(contexts,alpha,frontier) {
 return (x)=>JSON.stringify([alpha(x),[...frontier(x)].sort()]);
}
function safeSelectors(contexts,alpha,frontier) {
 const ret={};
 for(const [key,fiber] of groups(contexts,alpha)) {
  let cand=[...frontier(fiber[0])];
  for(const x of fiber.slice(1))cand=cand.filter(a=>frontier(x).includes(a));
  ret[key]=cand;
 }
 return ret;
}
function run() {
 const coarse=()=>"membership-structure"; // deliberately ignores demand/lifecycle
 const front=x=>pareto(x);
 const repair=minimalObservedRepair(phases,coarse,front);
 const coarseCheck=factorization(phases,coarse,front);
 const repairedCheck=factorization(phases,repair,front);
 const selectors=safeSelectors(phases,coarse,front);
 const ans={
  authority:"P31_PROOF_INSTANCE_ONLY__NOT_GENERATIVE_LAW",
  source:p3.stage,provenance:{run:p3.canonical_run,sha:p3.canonical_head},
  observation_scope:p3.oracle_strength.established,
  measured:phases.map(x=>({context:x,alternatives:actions.map(a=>({name:a,...cost(a,x)})),pareto:front(x)})),
  coarse_projection:{label:"membership-structure",exact_factorization:coarseCheck.lossless,obstruction:coarseCheck.witness},
  observed_coarsest_repair:{classes:groups(phases,repair).size,exact_factorization:repairedCheck.lossless,uses_outcome_to_refine:true,is_prospective_predictor:false},
  safe_but_not_lossless_constant_actions:selectors["membership-structure"],
  scientific_boundary:"Existing phase0/phase1 cost vectors; not an outcome-blind OO law, not global SOLID, not a full world replication.",
  P31_open:true,LAW_R2_authorized:false
 };
 return ans;
}
function selfTest() {
 const r=run();
 assert.equal(r.observation_scope,"BOUNDED_NO_NETWORK");
 assert.deepEqual(r.measured[0].pareto,actions);
 assert.deepEqual(r.measured[1].pareto,[actions[1]]);
 assert.equal(r.coarse_projection.exact_factorization,false);
 assert.equal(r.coarse_projection.obstruction.left,"phase0");
 assert.equal(r.coarse_projection.obstruction.right,"phase1");
 assert.equal(r.observed_coarsest_repair.classes,2);
 assert.equal(r.observed_coarsest_repair.exact_factorization,true);
 assert.deepEqual(r.safe_but_not_lossless_constant_actions,[actions[1]]);
 // Synthetic *logical* counterexample for selector existence, NEVER real-world data.
 const fake={left:["A"],right:["B"]};
 assert.deepEqual(safeSelectors(["left","right"],()=> "same", x=>fake[x]).same,[]);
 assert.equal(factorization(["left","right"],()=> "same",x=>fake[x]).lossless,false);
 assert.equal(factorization(["left","right"],x=>x,x=>fake[x]).lossless,true);
 // A no-information alpha cannot be an exact projection if frontiers conflict.
 assert.equal(factorization(["left","right"],()=> "same", x=>["A","B"]).lossless,true);
 return {tests:"PASS",claims:"Mathematical definitions tested on finite witnesses only; proofs in P31_OBSERVATIONAL_SIEVE_SOLID_PROJECTION_THEOREMS.md",real_world_new_law:false};
}
console.log(JSON.stringify(process.argv.includes("--self-test")?selfTest():run(),null,2));
