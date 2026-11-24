// R101-B: bounded two-stage repair game; compare credible vs committed goal.
import assert from 'node:assert/strict';
let cases=0,blocked=0,recovered=0,diverted=0;
for(let k=0;k<15625;k++){
 let n=k;const [x,y,z]=Array.from({length:3},()=>Array.from({length:2},()=>{let v=n%5-2;n=Math.floor(n/5);return v}));
 const pos=v=>v.every(a=>a>0),sum=(a,b)=>a.map((v,i)=>v+b[i]);
 const fixed=pos(y)&&pos(sum(x,y));
 const alt=pos(z)&&z[0]>Math.max(0,pos(y)?y[0]:0);
 const tail=alt?z:pos(y)?y:[0,0];
 const original= !alt&&pos(y)&&pos(sum(x,tail));
 // Binding exclusion of alternative; neither owner pays extra for commitment.
 const committed=pos(y)&&pos(sum(x,y));
 assert.equal(committed,fixed);
 if(fixed&&!original){recovered++;if(!pos(sum(x,tail)))blocked++;else diverted++;}
 cases++;
}
assert.equal(recovered,42);assert.equal(blocked,3);assert.equal(diverted,39);
console.log(JSON.stringify({cases,recovered,blocked,diverted}));
