// R93: same clairvoyant cost, arbitrarily large commitment penalty under a bounded action menu.
function check(b,m){if(!b)throw Error(m)}

function cover(sets,n){
 const full=(1<<n)-1,dp=Array(1<<n).fill(Infinity);dp[0]=0;
 for(const x of sets){const old=dp.slice();for(let s=0;s<dp.length;s++)dp[s|x]=Math.min(dp[s|x],old[s]+1)}
 return dp[full];
}

function frontier(m,H){
 const n=2*m,all=(1<<n)-1,half=(1<<m)-1;
 // A common prefix costs 1; low-cost action edges cost 1, fallback H-1.
 // World-dependent goal membership is the only source of uncertainty.
 const prefix=(mask,offset)=>[
  {mask,cost:2},...Array.from({length:m},(_,i)=>({mask:1<<(offset+i),cost:2})),{mask:all,cost:H}];
 const P=prefix(half,m),Q=prefix(half<<m,0);
 const pointwise=(menu,w)=>Math.min(...menu.filter(a=>a.mask&(1<<w)).map(a=>a.cost));
 for(let w=0;w<n;w++)check(pointwise(P,w)===2&&pointwise(Q,w)===2,"identical clairvoyant optimum");
 const budgetCost=(menus,k)=>[2,H].find(t=>menus.some(menu=>cover(menu.filter(a=>a.cost<=t).map(a=>a.mask),n)<=k))??Infinity;
 const rows=[];
 for(let k=1;k<=m+1;k++){
 const early=budgetCost([P,Q],k),late=budgetCost([[...P,...Q]],k);
 check(early===(k<=m?H:2),"early frontier");
 check(late===(k===1?H:2),"late frontier");
 rows.push({k,early,late});
 }
 return rows
}

function trial(){
 let cases=0;for(let m=2;m<=6;m++)for(const H of [3,10,100]){cases+=frontier(m,H).length}
 return {result:"PASS_COMMITMENT_COST_FRONTIER",cases,example:frontier(4,20),scope:"finite constructed menu costs; exact dynamic programming, not actual source edit measurements"}
}
console.log(JSON.stringify(trial(),null,2));
