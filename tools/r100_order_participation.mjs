// R100-B: order-sensitive participation on the historical P42 edit grammar.
// Synthetic owner gains; no actual labor or native Chi claim.
import assert from 'node:assert/strict';
const steps=['C','D','E','F'];
const legal=p=>!(p.includes('E')&&p.includes('F'));
const goal=(p,g)=>g.every(x=>p.includes(x));
function paths(g){
 const out=[];
 function visit(p){if(goal(p,g)){out.push(p);return}for(const x of steps)if(!p.includes(x)&&legal([...p,x]))visit([...p,x]);}
 visit([]);return out;
}
function seq(p,u){let v=[0,0];for(let j=p.length-1;j>=0;j--){v=v.map((x,i)=>x+u[p[j]][i]);if(v.some(x=>x<=0))return false;}return true;}
function bundle(p,u){return [0,1].every(i=>p.reduce((s,x)=>s+u[x][i],0)>0);}
const gs=[['C','D'],['E','C'],['F','D']];
let count=0,orderGap=0,bundleGap=0;
for(let k=0;k<6561;k++){
 let n=k;const u=Object.fromEntries(steps.map(x=>[x,[0,1].map(()=>{const v=n%3-1;n=Math.floor(n/3);return v;})]));
 for(const g of gs){
  const p=paths(g).filter(x=>x.length===2);
  assert.equal(p.length,2);
  const a=p.map(x=>seq(x,u)),b=p.map(x=>bundle(x,u));
  assert.equal(b[0],b[1]);assert(a.every((x,i)=>!x||b[i]));
  count++;orderGap+=Number(a[0]!==a[1]);bundleGap+=Number(b[0]&&!a.some(Boolean));
 }
}
console.log({count,orderGap,bundleGap});
