import {threshold,baseCost,optimalRepairs} from './threshold.mjs';
import {countModel} from './model.mjs';
import {backup,iterate,maxdiff} from './solver.mjs';
import {dualBound} from './dual.mjs';
import {repairFlow,invariantCheck} from './flow.mjs';
import {labeledModel,labeledSolve} from './labeled_oracle.mjs';
import {fluidValue,fluidBound,fluidEquilibrium} from './fluid.mjs';
import {writeFileSync} from 'node:fs';
const rows=[];let maxResidual=0,maxLabeledError=0,maxFlowError=0,dualViolations=0,fluidViolations=0,labeledCases=0,checks=0,maxFluidRatio=0;
for(const n of [1,2,3,4,8,16,32,64])for(const h of [...new Set([0,1,Math.floor(n/2),n])])for(const q of [0,.25,.75,1])for(const r of [0,.25,1,4]){
 const m=countModel(n,h,q,r);
 for(const g of [.5,.9]){
  const pi=m.map((_,k)=>optimalRepairs(k,h,q,r,g));
  const v=iterate(m,g,pi),res=maxdiff(backup(m,v.v,g),v.v),e=res/(1-g);
  if(e>1e-7)throw Error('greedy Bellman failure');
  maxResidual=Math.max(maxResidual,res);
  const repairModel=m.map(acts=>acts.map(a=>({...a,c:a.b})));
  const b=iterate(repairModel,g,pi);
  let maxDualGap=0,fluidRatio=0;
  for(let k=0;k<=n;k++){
   const gap=v.v[k]-dualBound(n,k,h,q,r,g).lower;
   if(gap < -1e-7)dualViolations++;
   maxDualGap=Math.max(maxDualGap,gap);
   const flowError=Math.abs(v.v[k]-repairFlow(n,k,q,r,g,b.v[k]));
   maxFlowError=Math.max(maxFlowError,flowError);
   const f=fluidValue(k/n,h/n,q,r,g),bound=fluidBound(n,q,r,g);
   const err=Math.abs(v.v[k]/n-f.v);
   if(err>bound+e/n+f.tail+1e-8)fluidViolations++;
   fluidRatio=Math.max(fluidRatio,err/bound);
   if(q>0){const z=fluidEquilibrium(h/n,q,r<threshold(q,g));const zp=q+(1-q)*(z-(r<threshold(q,g)?Math.min(z,h/n):0));if(Math.abs(z-zp)>1e-10)throw Error('fluid fixed point')}
  }
  maxFluidRatio=Math.max(maxFluidRatio,fluidRatio);
  if(n<=4){const lm=labeledModel(n,h,q,r),lv=labeledSolve(lm,g);const z=Math.max(...lm.states.map((x,i)=>Math.abs(lv.v[i]-v.v[lm.count(x)])));maxLabeledError=Math.max(maxLabeledError,z);if(z>1e-7)throw Error('labeled mismatch');labeledCases++}
  rows.push({n,h,q,r,g,maxDualGap,fluidRatio,residual:res,initial0:v.v[0],dual0:dualBound(n,0,h,q,r,g).lower});
 }
 for(let k1=0;k1<=n;k1++)for(let k2=k1;k2<=n;k2++)for(let b2=0;b2<=Math.min(k2,h);b2++){if(!invariantCheck(n,h,k1,k2,b2))throw Error('coupling');checks++}
}
if(dualViolations||fluidViolations||maxFlowError>1e-7)throw Error('bound failed');
const out={models:rows.length,labeledCases,checks,maxResidual,maxLabeledError,maxFlowError,dualViolations,fluidViolations,maxFluidRatio,rows};
writeFileSync(new URL('./result.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({...out,rows:undefined},null,2));
