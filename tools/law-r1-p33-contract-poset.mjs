#!/usr/bin/env node
// P33 bounded classical contravariant assume/guarantee contract poset.
// NOT a complete alternating-simulation interface automata implementation.
import assert from "node:assert/strict";
import fs from "node:fs";
const inNames=["read","configure"],outNames=["ok","error"];
const subset=(a,b)=>a.every(v=>b.includes(v));
const mask=(n,items)=>items.filter((_,i)=>(n&(1<<i))!==0);
const contracts=[];
for(let a=0;a<4;a++)for(let g=0;g<4;g++)
 contracts.push({assumptions:mask(a,inNames),guarantees:mask(g,outNames),a,g});
const refines=(i,s)=>subset(s.assumptions,i.assumptions)&&subset(i.guarantees,s.guarantees);
let reflexive=0,antisymmetric=0,transitive=0;
for(const a of contracts) {
 assert.ok(refines(a,a));reflexive++;
 for(const b of contracts) {
  if(refines(a,b)&&refines(b,a)) {
   assert.equal(a.a,b.a);assert.equal(a.g,b.g);antisymmetric++;
  }
  for(const c of contracts)if(refines(a,b)&&refines(b,c)) {
   assert.ok(refines(a,c));transitive++;
  }
 }
}
const get=(a,g)=>contracts.find(x=>x.a===a&&x.g===g);
const original=get(1,3),good=get(3,1),badPre=get(0,1),wide=get(3,3),narrow=get(1,1);
assert.ok(refines(good,original));
assert.ok(!refines(badPre,original));
assert.ok(!refines(wide,narrow)&&!refines(narrow,wide));
const clientSafe=(inputs,outputs,c)=>subset(inputs,c.assumptions)&&subset(c.guarantees,outputs);
assert.equal(clientSafe(["read"],["ok","error"],original),true);
assert.equal(clientSafe(["read"],["ok","error"],good),true);
assert.equal(clientSafe(["read"],["ok","error"],badPre),false);
const graph={policy_to_port:true,provider_to_port:true,policy_to_provider:false,port_to_provider:false,client_owns_port:true};
const inverted=x=>x.policy_to_port&&x.provider_to_port&&!x.policy_to_provider&&!x.port_to_provider&&x.client_owns_port;
assert.ok(inverted(graph));assert.ok(!inverted({...graph,policy_to_provider:true}));
const report={
 schema:"P33_FINAL_CLASSICAL_ASSUME_GUARANTEE_POSET_V1",
 interpretation:"state-independent two-input two-output contract order, not temporal alternating simulation",
 contracts_enumerated:contracts.length,triple_cases:contracts.length**3,
 reflexive_checks:reflexive,antisymmetric_checks:antisymmetric,transitive_premise_cases:transitive,
 refinements:{
  implementation_accepts:["read","configure"],contract_accepts:["read"],
  implementation_guarantees:["ok"],contract_guarantees:["ok","error"],
  pass:true
 },
 counterexamples:{stronger_precondition_fails:true,incomparable_wide_narrow_contracts:true,LSP_and_DIP_are_independent:true},
 citations_drive_ids:{
  LiskovWing:"1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl",
  Martin:"1fZQi6039W58RcQxTKFHiJZw22mU9kw7g",
  deAlfaroHenzinger:"1NUV-6p3ANXDT6ftnURRb8LpwbSp1xTSV",
  Ye:"15Y8_nyBQsxfx8SmzFHK_pL2V96J92wiU",
  Huang:"1RmEcUSQUqyzYfdWcK5m5DPu4W1vDVKIt"
 },
 interface_automata_correct_DOI:"10.1145/503271.503226",
 limitations:["No complete stateful input/output game or concurrency semantics","No real-source dependency graph extracted","Only finite sanity test of cited classical algebra"],
 verdict:"P33_CLASSICAL_CONTRACT_POSET_VERIFIED__CONCEPTUAL_SOLID_THEORY_BOUNDED_CLOSE_CANDIDATE__LAW_R2_NOT_AUTHORIZED"
};
const path=process.argv[2]||"out/p33-contract-poset.json";
fs.mkdirSync(path.substring(0,path.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(path,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",contracts:contracts.length,triples:contracts.length**3,transitive_premise_cases:transitive}));
