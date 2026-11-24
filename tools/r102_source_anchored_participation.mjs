// R102: historical P44 acceptance labels, NOT a fresh Go run.
// Rights, private costs and participation are deliberately hypothetical.
import assert from 'node:assert/strict';
const repairs=['constructor','route_both','match_lower'];
const allowed=(hard,mask)=>repairs.filter((r,i)=>(mask&(1<<i))&&(!hard||r==='route_both'));
function choose(hard,mask,gains){
 const f=allowed(hard,mask);
 const feasible=f.filter(r=>gains[r].every(x=>x>0));
 return {technical:f,strategic:feasible};
}
let cases=0,technicalOnly=0,strictLoss=0;
for(let k=0;k<729;k++){
 let n=k;const gains=Object.fromEntries(repairs.map(r=>[r,[0,1].map(()=>{const v=n%3-1;n=Math.floor(n/3);return v})]));
 for(let mask=0;mask<8;mask++){
  const soft=choose(false,mask,gains),hard=choose(true,mask,gains);
  assert(hard.technical.every(r=>soft.technical.includes(r)));
  assert(hard.strategic.every(r=>soft.strategic.includes(r)));
  for(const a of [soft,hard]){
   cases++;technicalOnly+=Number(a.technical.length>0&&a.strategic.length===0);
   strictLoss+=Number(a.strategic.length<a.technical.length);
  }
 }
}
assert.deepEqual(allowed(true,7),['route_both']);
assert.deepEqual(allowed(false,7),repairs);
console.log({cases,technicalOnly,strictLoss});
