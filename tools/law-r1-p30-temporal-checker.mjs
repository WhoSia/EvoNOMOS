#!/usr/bin/env node
// Phase II-C theorem regression only; a constructed Moore machine is not a fresh world witness.
import assert from "node:assert/strict";

const states = ["a","b","c","d"];
const out = {a:0,b:0,c:0,d:1};
const W = {a:"ready",b:"ready",c:"post",d:"post"};
const action = {
  a:{step:"c",idle:"a"},
  b:{step:"d",idle:"b"},
  c:{step:"c",idle:"c"},
  d:{step:"d",idle:"d"}
};
const advance=(s,word)=>word.reduce((q,x)=>action[q][x],s);
const trace=(s,word)=>[out[s],...word.map((_,i)=>out[advance(s,word.slice(0,i+1))])];
assert.equal(W.a,W.b);
assert.equal(out.a,out.b);
assert.deepEqual(trace("a",[]),trace("b",[]));
assert.notDeepEqual(trace("a",["step"]),trace("b",["step"]));
assert.deepEqual([W.a,W.b],["ready","ready"]);
assert.equal(trace("a",["step"])[1],0);
assert.equal(trace("b",["step"])[1],1);

function observationalPartition(){
  let p=Object.fromEntries(states.map(s=>[s,String(out[s])]));
  const history=[JSON.stringify(states.map(s=>p[s]))];
  for(let iteration=0;iteration<states.length;iteration++){
    const sig=states.map(s=>JSON.stringify([out[s],...["step","idle"].map(a=>p[action[s][a]])]));
    const code=new Map();
    const next=Object.fromEntries(states.map((s,i)=>{
      if(!code.has(sig[i]))code.set(sig[i],String(code.size));
      return [s,code.get(sig[i])];
    }));
    const equivalent=(x,y)=>states.every(i=>states.every(j=>(x[i]===x[j])===(y[i]===y[j])));
    if(equivalent(p,next))return {p:next,iterations:iteration};
    p=next;
    history.push(JSON.stringify(states.map(s=>p[s])));
  }
  throw new Error("Partition refinement did not converge within finite-state bound");
}
const pr=observationalPartition();
assert.notEqual(pr.p.a,pr.p.b);
assert.ok(pr.iterations<=states.length-1);
console.log("P30_IIC_PASSIVE_MATCH=PASS");
console.log("P30_IIC_TEMPORAL_PREDICTIVE_COLLISION=PASS");
console.log("P30_IIC_MOORE_PARTITION_REFINEMENT=PASS");
console.log("P30_IIC_FRESH_WORLD_EVIDENCE=NOT_CLAIMED");
console.log("P30_IIC_LAW_R2=NOT_AUTHORIZED");
