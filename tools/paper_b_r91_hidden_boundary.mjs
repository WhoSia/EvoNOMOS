// R91: conditional factor elimination boundary and sharp hidden-component example.
function assert(b,m){if(!b)throw Error(m)}

function pop(x){let k=0;while(x){x&=x-1;k++}return k}

function mobius(v,n){let a=v.slice();for(let i=0;i<n;i++)for(let s=0;s<a.length;s++)if(s&(1<<i))a[s]-=a[s^(1<<i)];return a}

function solve(n,h,factors){
 return Array.from({length:2**n},(_,d)=>{
  let best=Infinity;
  for(let z=0;z<2**h;z++){
   let val=factors.reduce((sum,f)=>sum+f.value(d,z),0);
   best=Math.min(best,val)
  }
  return best
 })
}

function trial(){
 // Split latent choices: boundary {0,1} and {2,3}; pure unary demand term.
 const n=5,h=2;
 const f=[
  {value:(d,z)=>z&1?1:pop(d&3)},
  {value:(d,z)=>z&2?1:pop(d&12)},
  {value:(d,z)=>d&16?3:0}
 ];
 const v=solve(n,h,f),m=mobius(v,n);
 assert(m.every((a,s)=>pop(s)<=2||a===0),"boundary order exceeded");
 assert(v.every((a,s)=>a===Math.min(pop(s&3),1)+Math.min(pop(s&12),1)+(s&16?3:0)),"component factorization");
 // A connected hidden chain (two latent binary variables); all four demands are its boundary.
 const chain=[
  {value:(d,z)=>z&1?0:pop(d&3)},
  {value:(d,z)=>z&2?0:pop(d&12)},
  {value:(d,z)=>z&1?3:0},
  {value:(d,z)=>Boolean(z&1)===Boolean(z&2)?0:5}
 ];
 const w=solve(4,2,chain),c=mobius(w,4);
 assert(w.every((a,s)=>a===Math.min(pop(s),3)),"chain witness");
 assert(c[15]===-1,"boundary order not realized");
 // Pure demand factor independent of hidden components can create its own high-order interaction.
 const pure=solve(4,0,[{value:(d,z)=>d===15?1:0}]);
 assert(mobius(pure,4)[15]===1,"pure factor witness");
 return {split_states:v.length,split_max_order:Math.max(...m.map((a,s)=>a?pop(s):0)),connected_states:w.length,connected_max_order:Math.max(...c.map((a,s)=>a?pop(s):0)),connected_top_coefficient:c[15],pure_factor_top_coefficient:1,scope:"finite mathematical factorized optimization fixtures; no source-code identification"};
}
console.log(JSON.stringify(trial(),null,2));
