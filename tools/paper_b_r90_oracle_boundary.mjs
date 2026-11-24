// R90: deterministic exact additivity oracle obstruction and conditional low-order recovery.
function check(b,m){if(!b)throw Error(m)}

function pop(s){let n=0;while(s){s&=s-1;n++}return n}

function additive(v,n){
 const N=2**n;
 for(let s=0;s<N;s++){
 let expected=v[0];for(let i=0;i<n;i++)if(s&(1<<i))expected+=v[1<<i]-v[0];
 if(expected!==v[s])return false
 }return true
}

function queryObstruction(n){
 const N=2**n,base=Array.from({length:N},(_,s)=>2*pop(s));
 let witnesses=0,monotonicChecks=0;
 check(additive(base,n),"baseline");
 for(let t=1;t<N;t++){
 const rival=base.slice();rival[t]++;
 check(!additive(rival,n),"perturbation must violate singleton additivity");
 for(let s=0;s<N;s++){
 if(s!==t)check(rival[s]===base[s],"changed an observed query");
 for(let i=0;i<n;i++)if(!(s&(1<<i))){
 check(rival[s]<=rival[s|(1<<i)],"cover monotonicity");monotonicChecks++
 }
 }witnesses++;
 }
 return {n,normalized_nonempty_queries:N-1,witnesses,monotonicChecks};
}

function mobiusRecover(n,r,query){
 const N=2**n,coef=Array(N).fill(0);
 let calls=0;
 for(let s=0;s<N;s++)if(pop(s)<=r){
 let a=query(s);calls++;
 for(let t=(s-1)&s;s&&t!==s;t=(t-1)&s){
 a-=coef[t];if(t===0)break;
 }
 coef[s]=a;
 }
 const evalAt=s=>{let a=0;for(let t=s;;t=(t-1)&s){a+=coef[t];if(t===0)break}return a};
 return {calls,evalAt};
}

function trial(){
 const obstruction=[];for(let n=2;n<=8;n++)obstruction.push(queryObstruction(n));
 const n=6,N=2**n;
 const coef=Array.from({length:N},(_,s)=>pop(s)===1?3:pop(s)===2?(s%5):0);
 const val=s=>{let a=0;for(let t=s;;t=(t-1)&s){a+=coef[t];if(t===0)break}return a};
 const model=mobiusRecover(n,2,val);for(let s=0;s<N;s++)check(model.evalAt(s)===val(s),"degree-two recovery");
 const hidden=mobiusRecover(n,2,s=>val(s)+(s===7?1:0));
 check(hidden.evalAt(7)!==val(7)+1,"low degree promise must be externally justified");
 return {obstruction,degree_two:{n,queries_including_zero:model.calls,total_states:N,verified_states:N,hidden_interaction_not_detected:true},scope:"mathematical oracle model; no empirical cost or novelty claim"};
}
console.log(JSON.stringify(trial(),null,2));
