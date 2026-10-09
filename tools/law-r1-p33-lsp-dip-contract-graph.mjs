#!/usr/bin/env node
/**
 * P33 bounded five-principle contract-graph model.
 * Mathematical interpretation of established behavioral subtyping,
 * client-contract dependency inversion and demand-relative quotients.
 * Finite exhaustive checks are regression tests, not universal proof.
 */
import assert from "node:assert/strict";
import fs from "node:fs";

const alphabet=["00","01","10","11"];
const traceFamily = mask => alphabet.filter((_,i) => mask & (1<<i));
const subset=(left,right)=>left.every(x=>right.includes(x));
const predicate=(left,right)=>subset(left,right);
const contract= ["00","01","11"]; // a two-read client forbids 1 followed by 0
const providerGood=["00","01"];
const providerUnsafe=["10"]; // individually returns only 0/1 but breaks history
const providerSilent=[]; // trace inclusion alone is vacuous for deadlock
const allowableInputs=["read","configure"];
const guardedInputs=["read"];
const fullInputs=["read","configure"];

function lspSafety(provider, port){
 return subset(port.accepts, provider.accepts) &&
        subset(provider.traces,port.traces);
}
const port={
  name:"ReadPort",
  accepts:allowableInputs,
  traces:contract,
  label:"nondecreasing two-read outcomes"
};
const good={name:"GoodProvider",accepts:fullInputs,traces:providerGood};
const badTrace={name:"BadHistoryProvider",accepts:fullInputs,traces:providerUnsafe};
const badPre={name:"BadPreconditionProvider",accepts:guardedInputs,traces:providerGood};
const silent={name:"SilentProvider",accepts:fullInputs,traces:providerSilent};
assert.equal(lspSafety(good,port),true);
assert.equal(lspSafety(badTrace,port),false);
assert.equal(lspSafety(badPre,port),false);
assert.equal(lspSafety(silent,port),true); // shows trace-safety vacuity
const progress=provider=>provider.traces.length>0;
assert.equal(progress(silent),false);

let exhaustive=0;
for(let k=0;k<16;k++)for(let i=0;i<16;i++)for(let s=0;s<16;s++){
 const K=traceFamily(k), I=traceFamily(i), Safe=traceFamily(s);
 if(subset(I,K)&&subset(K,Safe)) assert.ok(subset(I,Safe));
 exhaustive++;
}
assert.equal(exhaustive,4096);

function dependencyGraph({direct=false,portImportsImplementation=false,clientOwned=true}={}){
 const edges=[
  ["Client","ReadPort"],["GoodProvider","ReadPort"],
  ["Bootstrap","Client"],["Bootstrap","GoodProvider"]
 ];
 if(direct)edges.push(["Client","GoodProvider"]);
 if(portImportsImplementation)edges.push(["ReadPort","GoodProvider"]);
 return {edges,portOwner:clientOwned?"ClientPolicy":"GoodProvider",
  bindings:[["ReadPort","GoodProvider"]]};
}
function dependencyInversion(g, client="Client", iface="ReadPort", impl="GoodProvider"){
 const edge=(from,to)=>g.edges.some(x=>x[0]===from&&x[1]===to);
 const bindings=g.bindings.some(x=>x[0]===iface&&x[1]===impl);
 return edge(client,iface) && edge(impl,iface) && !edge(client,impl) &&
        !edge(iface,impl) && g.portOwner==="ClientPolicy" && bindings;
}
const graphGood=dependencyGraph();
const graphDirect=dependencyGraph({direct:true});
const graphPortLeaks=dependencyGraph({portImportsImplementation:true});
const graphOwnerBad=dependencyGraph({clientOwned:false});
assert.equal(dependencyInversion(graphGood),true);
assert.equal(dependencyInversion(graphDirect),false);
assert.equal(dependencyInversion(graphPortLeaks),false);
assert.equal(dependencyInversion(graphOwnerBad),false);
// Runtime behavior and compile-time dependency direction are independent:
assert.equal(lspSafety(good,port),true);
assert.equal(dependencyInversion(graphDirect),false);
assert.equal(dependencyInversion(graphGood),true);
assert.equal(lspSafety(badTrace,port),false);

const states=[0,1,2,3],oA=states.map(x=>Math.floor(x/2)),
  gA=oA,gB=states.map(x=>x%2),oBoth=states.map(x=>x);
function kernelRefines(o,g){
 return states.every(x=>states.every(y=>o[x]!==o[y]||g[x]===g[y]));
}
assert.equal(kernelRefines(oA,gA),true);
assert.equal(kernelRefines(oA,gB),false);
assert.equal(kernelRefines(oBoth,gB),true);
// A stable port can be well-typed, LSP-safe and DIP-directed but unable
// to support a new demand whose distinctions its observation erases.
function jointCertificate(graph,impl,contract,observation,demand){
 return {inversion:dependencyInversion(graph),
         precondition:subset(contract.accepts,impl.accepts),
         traceRefinement:subset(impl.traces,contract.traces),
         progress:progress(impl),
         demandAdequacy:kernelRefines(observation,demand)};
}
const certified=jointCertificate(graphGood,good,port,oA,gA);
const insufficient=jointCertificate(graphGood,good,port,oA,gB);
const direct=jointCertificate(graphDirect,good,port,oA,gA);
const unsound=jointCertificate(graphGood,badTrace,port,oA,gA);
assert.ok(Object.values(certified).every(Boolean));
assert.deepEqual(Object.entries(insufficient).filter(([,v])=>!v).map(([k])=>k),["demandAdequacy"]);
assert.deepEqual(Object.entries(direct).filter(([,v])=>!v).map(([k])=>k),["inversion"]);
assert.deepEqual(Object.entries(unsound).filter(([,v])=>!v).map(([k])=>k),["traceRefinement"]);

// Cost/projection and behavioral contracts live in distinct logical layers.
// A source-inverted graph does not imply lower total lifecycle cost.
const params={pA:.2,pB:.2,pAB:.04,k:.03,costPerTouch:1};
const grouped=lambda=>.36+.32*lambda, split=.43;
assert.ok(grouped(.1)<split && grouped(.3)>split);

const report={
 schema:"P33_CONDITIONAL_SOLID_TRACE_REFINEMENT_PORT_GRAPH_V1",
 theory_status:"INTEGRATIVE_CLASSICAL_RESULTS_WITH_EXPLICIT_ASSUMPTIONS",
 trace_alphabet:alphabet,
 examined_trace_contract_triplets:exhaustive,
 trace_contract:port,
 provider_cases:{
  good_lsp_safety:lspSafety(good,port),
  violating_history_lsp_safety:lspSafety(badTrace,port),
  excessive_precondition_lsp_safety:lspSafety(badPre,port),
  silent_lsp_safety_vacuous:lspSafety(silent,port),
  silent_progress:progress(silent)
 },
 dependency_cases:{
  inverted_and_client_owned:dependencyInversion(graphGood),
  concrete_direct_import:dependencyInversion(graphDirect),
  port_imports_implementation:dependencyInversion(graphPortLeaks),
  provider_owns_port:dependencyInversion(graphOwnerBad),
  source_graph:graphGood
 },
 cross_principle_cases:{
  all_bounded_conditions:certified,
  LSP_and_DIP_but_new_demand_unobservable:insufficient,
  LSP_but_DIP_not_satisfied:direct,
  DIP_but_LSP_not_satisfied:unsound
 },
 identity_of_claims:{
  LSP:"Provider traces subset of accepted client port traces under input preconditions; progress and liveness must be separately specified",
  DIP:"Source compile/import edges plus client-policy owned port and injected provider binding, not just runtime call arrows",
  ISP:"Port observation preserves every distinction demanded by D; coarsest sufficient quotient relative to D",
  OCP:"A new demand can be implemented downstream of an unchanged observation only when kernel refinement holds",
  SRP:"Expected interference and change-frequency conditional cost; does not follow from substitution"
 },
 prior_genealogy:[
  "Liskov-Wing 1994 behavioral subtyping invariants/history",
  "Martin 1996 OCP-LSP-DIP structural implications",
  "de Alfaro-Henzinger 2001 interface automata",
  "Parnas 1972 change-oriented information hiding",
  "Sullivan et al. 2001 change options",
  "EvoNOMOS P18 Principle-as-Projection hypothesis",
  "EvoNOMOS ORIGIN-R1-P11 WIDE versus SEGREGATED capabilities",
  "EvoNOMOS P31 LSP contract versus conditional cost maxim distinction"
 ],
 model_limits:[
  "Four finite two-response traces and 4096 finite safety-condition combinations only",
  "Trace inclusion gives safety only; silent provider demonstrates divergence/progress hole",
  "No full asynchronous concurrent client trace semantics or actual OO runtime subtyping",
  "Source graph is an explicit logical example, not an extracted production import graph",
  "DIP policy ownership is a modeled governance/port criterion rather than intrinsic graph property",
  "Mathematical joint certificate proves neither a cost advantage nor a new universal law"
 ],
 verdict:"P33_LSP_DIP_FORMAL_SYNTHESIS_FINITE_METHOD_PASS__INTEGRATIVE_THEORY_OPEN__LAW_R2_NOT_AUTHORIZED"
};
const output=process.argv[2]||"out/p33-lsp-dip-finite.json";
fs.mkdirSync(output.slice(0,output.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",cases:exhaustive,examples:Object.keys(report.cross_principle_cases),
  safeProvider:report.provider_cases.good_lsp_safety,unsafeHistory:report.provider_cases.violating_history_lsp_safety,
  negativeCases:3}));
