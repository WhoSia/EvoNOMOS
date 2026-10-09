#!/usr/bin/env node
/**
 * P33 finite demand-relative interface quotient verifier.
 * Classical quotient universal property and factorization.
 * Interpretive SOLID reconstruction, not new mathematics.
 */
import assert from "node:assert/strict";
import fs from "node:fs";
const X=[0,1,2,3];
const gA=[0,0,1,1];    // first bit
const gB=[0,1,0,1];    // second bit
const gBoth=X.map(x=>gA[x]*2+gB[x]);
const countLabels=f=>new Set(f).size;
const sameKernel=(a,b)=>X.every(x=>X.every(y=>(a[x]===a[y])===(b[x]===b[y])));
const kernelRefines=(a,b)=>X.every(x=>X.every(y=>a[x]!==a[y]||b[x]===b[y]));
function factor(g,obs){
 const decoder=new Map();
 for(const x of X){
  if(decoder.has(obs[x])&&decoder.get(obs[x])!==g[x])return null;
  decoder.set(obs[x],g[x]);
 }
 return decoder;
}
function mapping(n){
 const ret=[];
 for(let i=0;i<X.length;i++){ret.push(n%4);n=Math.floor(n/4);}
 return ret;
}
const possible=Array.from({length:256},(_,i)=>mapping(i));
let checked=0,suffA=0,suffBoth=0,minA=Infinity,minBoth=Infinity;
for(const obs of possible){
 const fa=factor(gA,obs),fb=factor(gB,obs),fall=factor(gBoth,obs);
 const expectedA=kernelRefines(obs,gA);
 const expectedB=kernelRefines(obs,gB);
 const expectedBoth=expectedA&&expectedB;
 assert.equal(fa!==null,expectedA);
 assert.equal(fb!==null,expectedB);
 assert.equal(fall!==null,expectedBoth);
 if(fa!==null){suffA++;minA=Math.min(minA,countLabels(obs));}
 if(fall!==null){suffBoth++;minBoth=Math.min(minBoth,countLabels(obs));}
 // Every sufficient interface refines the minimal demanded quotient.
 if(fall!==null)assert.ok(kernelRefines(obs,gBoth));
 checked++;
}
// All deterministic output predicates on four states, and all observations.
let exhaustive=0;
for(const g of possible) for(const obs of possible){
 assert.equal(factor(g,obs)!==null,kernelRefines(obs,g));
 exhaustive++;
}
assert.equal(exhaustive,65536);
assert.equal(minA,2);
assert.equal(minBoth,4);
assert.ok(sameKernel(gBoth,X));
assert.equal(factor(gB,gA),null);  // A-only interface fails a B demand.
assert.notEqual(factor(gB,gBoth),null);

// A demand-relevant interface does not have a unique encoding, only a
// universal equivalence class up to bijective relabeling of observations.
const renamed=[3,3,2,2];
assert.ok(sameKernel(renamed,gA));
assert.notEqual(factor(gA,renamed),null);

// Source-rooted collision (already known issue, not an independent forecast).
const nameUrlStates=[
 {name:"alpha][https://x.invalid/",url:"https://y.invalid/"},
 {name:"alpha",url:"https://x.invalid/][https://y.invalid/"}
];
const msg=x=>"["+x.name+"]["+x.url+"] TLS certificate CERT will expire in 5 days";
assert.equal(msg(nameUrlStates[0]),msg(nameUrlStates[1]));
assert.notDeepEqual(nameUrlStates[0],nameUrlStates[1]);
const desired=nameUrlStates.map(x=>x.name+"|"+x.url);
assert.notEqual(desired[0],desired[1]);
let sourceReceipts="not supplied";
if(process.argv[2] && fs.existsSync(process.argv[2])){
 const s=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
 assert.equal(s.source_birth,"398482d590daaac0d44e288c9be3bc6f6667f8b8");
 assert.equal(s.parametrized_actual_source_executions.caller.passed_pairs,64);
 assert.equal(s.parametrized_actual_source_executions.dispatcher.failed_pairs,64);
 sourceReceipts="bounded source execution already verified 64/64 vs 0/64";
}
// Conditional SRP-cost illustration, not a universal decomposition law.
const pA=.2,pB=.2,pAB=.04,initialOverhead=.03;
const xor=pA+pB-2*pAB,union=pA+pB-pAB;
const grouped=lambda=>union+lambda*xor;
const split=pA+pB+initialOverhead;
const threshold=(split-union)/xor;
assert.ok(Math.abs(threshold-.21875)<1e-12);
assert.ok(grouped(.1)<split);
assert.ok(grouped(.3)>split);
const record={
 schema:"P33_DEMAND_RELATIVE_INTERFACE_QUOTIENT_V1",
 kind:"CLASSICAL_MATHEMATICS_PLUS_SOLID_INTERPRETATION",
 theorem:"Each demand g factors via interface o iff ker(o) subseteq ker(g); joint demands use intersection of equivalence kernels.",
 universal_property:"The canonical tuple observation q_D is coarsest sufficient quotient up to bijective recoding; any sufficient o factors q_D through o.",
 tested_observation_functions:checked,
 exhaustive_factorization_pairs:exhaustive,
 srp_conditional_cost_model:{pA,pB,pAB,grouped_base_touch:union,one_axis_only_probability:xor,amortized_split_overhead:initialOverhead,split_cost:split,split_preference_threshold_lambda:threshold,grouping_preferred_at_lambda_0_1:true,split_preferred_at_lambda_0_3:true,interpretation:"Illustrative stipulated coupling-risk penalty, NOT an empirically estimated design law"},
 min_interface_labels_for_A:minA,
 min_interface_labels_for_A_and_B:minBoth,
 sufficient_observations_for_A:suffA,
 sufficient_observations_for_joint:suffBoth,
 oA_extensible_to_B_without_new_channel:false,
 source_message_collision_verified:true,
 source_receipts:sourceReceipts,
 interpretation:{
  ISP:"demand-indexed coarsest sufficient capability partition; not a mandated API member count",
  OCP:"extension without modifying the existing information boundary possible exactly when new g factors through o, within the restricted decoder edit grammar",
  DIP:"replace concrete producer behind a stable sufficient contract; behavioral equivalence is relative to the same demand family",
  LSP:"requires complete behavioral refinement of stipulated client observations; equality on bounded samples is insufficient",
  SRP:"demand-change reasons partition ownership; a contextual decomposition hypothesis, not derivable from quotient theorem alone"
 },
 limitations:["finite four-state verifier does not prove theorem for arbitrary infinite X; the general proof is elementary quotient/factorization logic","not an empirical SOLID success law","no production Uptime Kuma functional proof","no H-versus-B2 prospective advantage"],
 verdict:"P33_FORMAL_REINTERPRETATION_PASS__FINITARY_CHECK_PASS__SCIENCE_APPLICATION_OPEN__LAW_R2_NOT_AUTHORIZED"
};
const out=process.argv[3]??"out/p33-solid-quotient.json";
fs.mkdirSync(out.slice(0,out.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(out,JSON.stringify(record,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",exhaustive_pairs:exhaustive,min_interface_labels_A:minA,min_joint_labels:minBoth,source:sourceReceipts}));
