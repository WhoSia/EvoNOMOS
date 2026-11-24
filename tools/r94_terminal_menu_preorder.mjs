// R94: terminal menu preorder from downset of budget-admissible goal signatures.
function assert(b,m){if(!b)throw Error(m)}

function down(family,n){return Array.from({length:2**n},(_,s)=>s===0||family.some(a=>(s&a)===s))}

function profile(family,n){const dp=Array(2**n).fill(Infinity);dp[0]=0;for(const a of family){const old=dp.slice();for(let s=0;s<dp.length;s++)dp[s|a]=Math.min(dp[s|a],old[s]+1)}return dp.map((_,s)=>Math.min(...dp.filter((v,t)=>(t&s)===s)))}

function trial(){
 const n=3, families=Array.from({length:128},(_,mask)=>Array.from({length:7},(_,i)=>i+1).filter((_,i)=>mask&(1<<i)));
 const data=families.map(f=>({f,down:down(f,n),profile:profile(f,n)}));let checks=0;
 for(const a of data)for(const b of data){
  const inclusion=a.down.every((x,i)=>!x||b.down[i]);
  const order=a.profile.every((v,i)=>b.profile[i]<=v);
  assert(inclusion===order,"dominance equivalence");
  checks++;
 }
 // Equal one-goal distances do not determine conjunction/menus.
 const a=profile([1,2,4],3),b=profile([7],3);
 assert([1,2,4].every(g=>a[g]===b[g]),"singleton equality");
 assert(a[7]===3&&b[7]===1,"joint gap");
 // Fixed threshold profile cannot preserve an additional history-sensitive contract.
 const before=profile([3],2),after=profile([1,2],2);
 assert(before[3]===1&&after[3]===2,"history-sensitive split");
 return {result:"PASS_MENU_PREORDER",familyPairs:checks,singletonEqual:true,jointMenu:[3,1],scope:"finite terminal coverage with per-action common budget; no multistage strategy preservation"};
}
console.log(JSON.stringify(trial(),null,2));
