// R101: deterministic repair game, A chooses an offer, B accepts or stops.
// Stop gives state-specific continuation payoff. Ties favor stopping.
// Gains are synthetic, not estimates of maintenance labor.
import assert from 'node:assert/strict';
function solve(nodes,id){
 const n=nodes[id];let best={gain:n.stop,path:[]};
 for(const e of n.edges){
  const tail=solve(nodes,e.to);
  const g=e.gain.map((x,i)=>x+tail.gain[i]);
  if(g[1]>n.stop[1]&&g[0]>best.gain[0])best={gain:g,path:[e.to,...tail.path]};
 }
 return best;
}
const make=(x,y,z)=>({s:{stop:[0,0],edges:[{to:'p',gain:x}]},p:{stop:[0,0],edges:[{to:'goal',gain:y},{to:'alt',gain:z}]},goal:{stop:[0,0],edges:[]},alt:{stop:[0,0],edges:[]}});
let cases=0,divert=0,blocked=0;
for(let k=0;k<15625;k++){
 let n=k;const [x,y,z]=Array.from({length:3},()=>Array.from({length:2},()=>{let v=n%5-2;n=Math.floor(n/5);return v}));
 const fixed=y.every(v=>v>0)&&x.every((v,i)=>v+y[i]>0);
 const g=solve(make(x,y,z),'s');
 const alt=z.every(v=>v>0)&&z[0]>y[0]&&fixed;
 if(fixed&&!g.path.includes('goal')){assert(alt);divert++;if(!g.path.length)blocked++;}
 cases++;
}
const example=make([-1,-1],[2,2],[3,1]);
assert.deepEqual(solve(example,'s').path,[]);
console.log({cases,divert,blocked});
