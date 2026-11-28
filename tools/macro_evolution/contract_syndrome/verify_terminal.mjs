// Replay the frozen small terminal grid; rightsChecks counts retained-feasible triples.
import assert from 'node:assert/strict';
import {parity,xorProduct} from './gf2.mjs';
import {syndromeDP} from './syndrome_dp.mjs';
import {brute} from './brute_oracle.mjs';
import {gaussianWitness} from './gaussian_certificate.mjs';
const count={matrices:0,syndromes:0,feasible:0,impossible:0,gaussianWitnessChecks:0,allDeletionTriples:0,previouslyFeasible:0,rightsChecks:0,deletionMakesImpossible:0,sameCost:0,higherCost:0,lowerCost:0};
for(let r=1;r<=3;r++)for(let m=0;m<=3;m++)for(let k=0;k<2**(r*m);k++){
  const cols=Array.from({length:m},(_,j)=>(k>>(j*r))&((1<<r)-1));
  const weights=cols.map((_,j)=>j+1);
  const d=syndromeDP(cols,weights),b=brute(cols,weights);
  const deleted=cols.map((_,j)=>syndromeDP(cols.filter((_,i)=>i!==j),weights.filter((_,i)=>i!==j)));
  count.matrices++;
  for(let s=0;s<2**r;s++){
    count.syndromes++;const v=d.get(s),w=gaussianWitness(cols,s,r);
    assert.equal(v?.cost,b.get(s));
    count.gaussianWitnessChecks++;
    if(v){count.feasible++;assert.equal(xorProduct(cols,Number(v.mask)),s);assert.equal(weights.reduce((c,x,j)=>c+((v.mask&(1n<<BigInt(j)))?x:0),0),v.cost);assert.equal(w,null)}
    else{count.impossible++;assert.notEqual(w,null);assert.equal(parity(w&s),1);assert(cols.every(c=>parity(w&c)===0))}
    for(const d2 of deleted){
      count.allDeletionTriples++;const u=d2.get(s);
      if(!v){assert.equal(u,undefined);continue}
      count.previouslyFeasible++;
      if(!u){count.deletionMakesImpossible++;continue}
      count.rightsChecks++;
      if(u.cost===v.cost)count.sameCost++;else if(u.cost>v.cost)count.higherCost++;else count.lowerCost++;
      assert(u.cost>=v.cost);
    }
  }
}
assert.deepEqual(count,{matrices:685,syndromes:5050,feasible:3134,impossible:1916,gaussianWitnessChecks:5050,allDeletionTriples:14356,previouslyFeasible:9082,rightsChecks:5944,deletionMakesImpossible:3138,sameCost:5505,higherCost:439,lowerCost:0});
console.log(JSON.stringify(count,null,2));
