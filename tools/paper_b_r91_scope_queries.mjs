// R91: downward-closed promised interaction scopes; exact query reconstruction.
function check(b,m){if(!b)throw Error(m)}

function subsets(s){const a=[];for(let t=s;;t=(t-1)&s){a.push(t);if(t===0)return a}}

function supported(scopes){return [...new Set(scopes.flatMap(subsets))].sort((a,b)=>a-b)}

function reconstruct(n,scopes,query){
 const keys=supported(scopes),mu=new Map([[0,0]]);let calls=0;
 for(const a of keys){if(a===0)continue;let v=query(a);calls++;
  for(const b of subsets(a))if(b!==a)v-=mu.get(b)||0;
  mu.set(a,v)
 }
 return {calls,evaluate:s=>subsets(s).reduce((x,a)=>x+(mu.get(a)||0),0)}
}

function trial(){
 const n=6,scopes=[7,12,48],keys=supported(scopes);
 const coeff=new Map(keys.map(s=>[s,s===0?0:((s*17)%11)-5]));
 const f=s=>subsets(s).reduce((v,a)=>v+(coeff.get(a)||0),0);
 const r=reconstruct(n,scopes,f);
 for(let s=0;s<2**n;s++)check(r.evaluate(s)===f(s),"scope recovery");
 check(r.calls===12,"query count");
 // A missing promised coordinate can carry a hidden coefficient; no empirical sparsity claim.
 const outside=33;
 check(!keys.includes(outside),"outside scope");
 const g=s=>f(s)+((s&outside)===outside?1:0);
 for(const s of keys)check(f(s)===g(s),"known queries differ");
 check(g(outside)!==r.evaluate(outside),"promise violation undetected");
 return {n,scopes,queries:r.calls,full_nonempty_queries:63,verified_states:64,unpromised_interaction_hidden:true,scope:"finite exact structural-promise model"}
}
console.log(JSON.stringify(trial(),null,2));
