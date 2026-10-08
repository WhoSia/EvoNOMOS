#!/usr/bin/env node
/**
 * EvoNOMOS P31: finite demand-trace quotient checker.
 * Typed MAINTENANCE interventions, not ordinary runtime steps.
 * Synthesized algebraic witness only; NOT evidence for SOLID's utility.
 */
import assert from "node:assert/strict";

export function validate(machine) {
  const {states, demands, output, next} = machine;
  assert.ok(Array.isArray(states) && states.length > 0);
  assert.ok(Array.isArray(demands) && demands.length > 0);
  assert.equal(new Set(states).size, states.length);
  assert.equal(new Set(demands).size, demands.length);
  const all = new Set(states);
  for (const s of states) {
    assert.ok(Object.hasOwn(output,s), "missing output "+s);
    assert.ok(Object.hasOwn(next,s), "missing transitions "+s);
    for (const d of demands) assert.ok(all.has(next[s][d]), "non-total transition "+s+" "+d);
  }
}
const signature = x => JSON.stringify(x);
function classify(states, signatureOf) {
  const keys = new Map(), classOf={};let id=0;
  for(const state of states) {
    const k=signature(signatureOf(state));
    if(!keys.has(k))keys.set(k,id++);
    classOf[state]=keys.get(k);
  }
  return {classOf,classCount:id};
}
function samePartition(states,a,b) {
  return states.every(s=>states.every(t=>
    (a[s]===a[t])===(b[s]===b[t])));
}
export function refine(machine) {
  validate(machine);
  const {states,demands,output,next}=machine;
  const history=[];
  let p=classify(states,s=>output[s]);history.push(p);
  // Every strict refinement raises class count.
  for(let i=0;i<states.length;i++) {
    const q=classify(states,s=>[output[s],...demands.map(d=>p.classOf[next[s][d]])]);
    if(samePartition(states,p.classOf,q.classOf))
      return {blocks:group(states,p.classOf),classOf:p.classOf,
        iterations:i,stabilized:true,blockCounts:history.map(x=>x.classCount)};
    assert.ok(q.classCount>p.classCount,"not a strict refinement");
    history.push(q);p=q;
  }
  throw Error("Finite refinement did not stabilize");
}
function group(states,classOf){
  const m=new Map();
  for(const s of states){const k=classOf[s];if(!m.has(k))m.set(k,[]);m.get(k).push(s);}
  return [...m.values()];
}
// Breadth-first search of state pairs: shortest distinguishing demand word.
export function shortestSeparatingTrace(machine,startA,startB) {
  validate(machine);
  const {output,next,demands,states}=machine;
  assert.ok(states.includes(startA)&&states.includes(startB));
  const todo=[[startA,startB,[]]],seen=new Set();
  for(let head=0;head<todo.length;head++) {
    const [a,b,path]=todo[head],id=JSON.stringify([a,b]);
    if(seen.has(id))continue;
    seen.add(id);
    if(signature(output[a])!==signature(output[b]))
      return {demands:path,after:[a,b],observed:[output[a],output[b]]};
    for(const d of demands)todo.push([next[a][d],next[b][d],[...path,d]]);
  }
  return null;
}
export function quotient(machine){
  const p=refine(machine);
  for(const block of p.blocks)
    for(const d of machine.demands){
      const targets=block.map(s=>p.classOf[machine.next[s][d]]);
      assert.equal(new Set(targets).size,1,"not a congruence: "+d);
    }
  return {blocks:p.blocks,blockCounts:p.blockCounts,
    classes:p.blocks.length,transitionWellDefined:true};
}
export const toy={
  states:["isolated","entangled","isolated_ext","entangled_ext","regression"],
  demands:["add_provider","revise_contract"],
  output:{
    isolated:{Q:"PASS"},entangled:{Q:"PASS"},
    isolated_ext:{Q:"PASS"},entangled_ext:{Q:"PASS"},
    regression:{Q:"FAIL"}
  },
  next:{
    isolated:      {add_provider:"isolated_ext",revise_contract:"isolated"},
    entangled:      {add_provider:"entangled_ext",revise_contract:"entangled"},
    isolated_ext:   {add_provider:"isolated_ext",revise_contract:"isolated_ext"},
    entangled_ext:  {add_provider:"entangled_ext",revise_contract:"regression"},
    regression:     {add_provider:"regression",revise_contract:"regression"}
  }
};
export function selfTest() {
  const q=quotient(toy);
  const witness=shortestSeparatingTrace(toy,"isolated","entangled");
  assert.deepEqual(witness.demands,["add_provider","revise_contract"]);
  assert.deepEqual(witness.observed,[{Q:"PASS"},{Q:"FAIL"}]);
  assert.equal(q.classes,4);
  assert.deepEqual(q.blockCounts,[2,3,4]);
  assert.ok(q.blocks.some(b=>b.length===2&&b.includes("isolated")&&b.includes("isolated_ext")));
  assert.equal(shortestSeparatingTrace(toy,"isolated","isolated_ext"),null);
  const bad=structuredClone(toy);delete bad.next.isolated.add_provider;
  assert.throws(()=>validate(bad));
  return {selfTest:"PASS",fixture:"SYNTHETIC_ALGEBRAIC_ONLY",
    observation:"Q_ONLY_NOT_S_L_C_A_Q",initialPair:["isolated","entangled"],
    initialObservationEqual:true,shortestWitness:witness,
    naiveCurrentObservationClasses:2,traceStableClasses:q.classes,
    refinementBlockCounts:q.blockCounts,quotientTransitionsWellDefined:true,
    sourceWorldEquivalence:"NOT_TESTED",oop_law:"NOT_DISCOVERED",
    SOLID:"NO_SOLID_RULE_ESTABLISHED",lawR2:"NOT_AUTHORIZED"};
}
if(process.argv[1] && process.argv[1].endsWith("law-r1-p31-demand-trace-quotient.mjs")) {
  console.log(JSON.stringify(selfTest(),null,2));
}
