// R90: optimal repair selection creates hidden high-order demand interaction.
function assert(b,m){if(!b)throw Error(m)}

function pop(s){let k=0;while(s){s&=s-1;k++}return k}

function mobius(f,n){
 const c=Array.from({length:2**n},(_,s)=>f(s));
 for(let i=0;i<n;i++)for(let s=0;s<2**n;s++)if(s&(1<<i))c[s]-=c[s^(1<<i)];
 return c;
}

function trial(){
 const outputs=[];
 for(let n=2;n<=10;n++){
  // Each individual strategy is additive up to a constant, yet
  // taking the cheaper feasible strategy creates an n-way term.
  const direct=s=>pop(s);
  const bundle=s=>n-1;
  const optimal=s=>Math.min(direct(s),bundle(s));
  const c=mobius(optimal,n);
  assert(c[2**n-1]===-1,"missing high-order term");
  for(let s=0;s<2**n;s++)if(pop(s)>=2&&s!==2**n-1)assert(c[s]===0,"unexpected lower-order term");
  for(let s=0;s<2**n-1;s++)assert(optimal(s)===direct(s),"unexpected non-full discrepancy");
  outputs.push({n,states:2**n,highest_order_interaction:c[2**n-1]})
 }
 return {outputs,meaning:"minimization over affine repair strategies need not preserve low interaction order",scope:"finite mathematical counterexample; not real software measurements"};
}
console.log(JSON.stringify(trial(),null,2));
