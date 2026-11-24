// R100-A: fixed mandatory repair path, public deterministic additive gains.
// Strict participation, outside option stop with no future gains; sunk gains ignored.
import assert from 'node:assert/strict';
export function assess(path) {
  const n=path.length, m=path[0].length;
  const v=Array(m).fill(0);
  let suffix=true;
  for(let j=n-1;j>=0;j--){
    for(let i=0;i<m;i++)v[i]+=path[j][i];
    suffix &&= v.every(x=>x>0);
  }
  return {local:path.every(e=>e.every(x=>x>0)),bundle:v.every(x=>x>0),sequential:suffix};
}
export function backward(path,j=0){
  if(j===path.length)return {complete:true,gain:Array(path[0].length).fill(0)};
  const next=backward(path,j+1);
  const gain=path[j].map((x,i)=>x+next.gain[i]);
  return gain.every(x=>x>0)?{complete:next.complete,gain}:{complete:false,gain:gain.map(()=>0)};
}
function main(){
 const counts={cases:0,local:0,sequential:0,bundle:0,bundleOnly:0,sequentialNotLocal:0};
 for(let k=0;k<15625;k++){
  let x=k;const p=Array.from({length:3},()=>Array.from({length:2},()=>{let v=x%5-2;x=Math.floor(x/5);return v}));
  const a=assess(p);
  assert.equal(a.sequential,backward(p).complete);
  assert(!a.local||a.sequential);assert(!a.sequential||a.bundle);
  counts.cases++;for(const key of ['local','sequential','bundle'])counts[key]+=Number(a[key]);
  counts.bundleOnly+=Number(a.bundle&&!a.sequential);
  counts.sequentialNotLocal+=Number(a.sequential&&!a.local);
 }
 assert.deepEqual(assess([[-3,1],[5,2]]),{local:false,bundle:true,sequential:true});
 assert.deepEqual(assess([[5,2],[-3,1]]),{local:false,bundle:true,sequential:false});
 console.log(JSON.stringify(counts));
}
main();
