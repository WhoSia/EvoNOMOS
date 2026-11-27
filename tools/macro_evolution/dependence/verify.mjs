import {frac,cmp,fmt,num} from './fraction.mjs';
import {mixture} from './mixture.mjs';
import {moments} from './moments.mjs';
import {momentBounds} from './moment_bounds.mjs';
import {blockVariance} from './covariance.mjs';
import {readFileSync} from 'node:fs';
const recorded=JSON.parse(readFileSync(new URL('./results.json',import.meta.url)));
const rows=[];
for(const n of [5,10,20,40,80,160]){
 const A=moments(mixture(n,[[1,4],[3,4]]),n),B=moments(mixture(n,[[0,1],[2,6],[4,1]]),n);
 if(cmp(A.mean,B.mean)||cmp(A.variance,B.variance)||cmp(A.mean,frac(1,2))||cmp(A.variance,frac(n+3,16*n)))throw Error('moment mismatch');
 const row={n,variance:fmt(A.variance),overflow_A:fmt(A.overflow),overflow_B:fmt(B.overflow),A:num(A.overflow),B:num(B.overflow),sign_A:cmp(A.overflow,frac(1,16)),sign_B:cmp(B.overflow,frac(1,16))};
 if(n<=80){
  const z=momentBounds(n);
  for(const x of [A,B])if(cmp(x.overflow,z.lo.value)<0||cmp(x.overflow,z.hi.value)>0)throw Error('outside bounds');
  row.bounds=[num(z.lo.value),num(z.hi.value)];row.extremizers=[z.lo,z.hi].map(v=>({support:v.xs,weight:v.w.map(fmt),value:fmt(v.value)}));row.feasible=z.feasible;
 }
 rows.push(row);
}
const block=[];for(const n of [16,64,256,1024])for(const b of [1,Math.sqrt(n),n])block.push({n,b,variance:blockVariance(n,b,.5)});
if(JSON.stringify(rows)!==JSON.stringify(recorded.rows)||JSON.stringify(block)!==JSON.stringify(recorded.block))throw Error('recorded results differ');
console.log('PASS exact mixtures, finite sharp bounds, and block variance');
