// R94: reuses the bounded historical P42 graph. No new source execution.
function check(b,m){if(!b)throw Error(m)}

function pop(n){let k=0;while(n){n&=n-1;k++}return k}

function states(){return Array.from({length:96},(_,i)=>({t:i%32,z:Math.floor(i/32)}))}

function reach(x,y){return (x.t&y.t)===x.t&&(x.z===0||x.z===y.z)}

function cost(x,y){return pop(y.t^x.t)+(x.z!==y.z?1:0)}

function goals(y){const C=!!(y.t&4),D=!!(y.t&8);return (C&&D?1:0)|(C&&y.z===1?2:0)|(D&&y.z===2?4:0)}

function coverCounts(x,b,worlds){
 const dp=Array(8).fill(Infinity);dp[0]=0;
 for(const y of worlds)if(reach(x,y)&&cost(x,y)<=b){
  const old=dp.slice(),g=goals(y);
  for(let s=0;s<8;s++)dp[s|g]=Math.min(dp[s|g],old[s]+1)
 }
 return Array.from({length:8},(_,target)=>Math.min(...dp.filter((_,s)=>(s&target)===target)));
}

function predicted(x,b,target){
 if(target===0)return 0;
 const c=(x.t&4)?0:1,d=(x.t&8)?0:1,e=x.z===0?1:0;
 if((target&2)&&x.z===2||(target&4)&&x.z===1)return Infinity;
 const ec=e+c,fd=e+d,cd=c+d;
 if((target&6)===6){
  if(b<Math.max(ec,fd))return Infinity;
  if(!(target&1)||b>=e+c+d)return 2;
  return b>=cd?3:Infinity;
 }
 if((target&3)===3||(target&5)===5){
  const branch=target&2?ec:fd;
  if(b>=e+c+d)return 1;
  return b>=Math.max(cd,branch)?2:Infinity;
 }
 return b>=(target&1?cd:target&2?ec:fd)?1:Infinity;
}

function trial(){
 const w=states();let pairs=0,checks=0,strict=0,infeasible=0;
 const histogram={};for(const x of w)for(const y of w)if(reach(x,y))pairs++;
 check(pairs===1215,"old graph count");
 for(const x of w)for(let b=0;b<=6;b++){
  const dp=coverCounts(x,b,w);
  for(let t=0;t<8;t++){
    const p=predicted(x,b,t);check(dp[t]===p,`frontier mismatch ${JSON.stringify({x,b,t,got:dp[t],p})}`);
    checks++;if(!Number.isFinite(p))infeasible++;else if(p>1)strict++;
    if(t===7){const key=Number.isFinite(p)?String(p):"INF";histogram[key]=(histogram[key]||0)+1}
  }
 }
 // At x=(empty,none), each goal attainable for b=2;
 // CD, EC and FD each need distinct endpoints. b=3 permits 2 endpoints.
 const base={t:0,z:0};check(coverCounts(base,2,w)[7]===3,"three menu");check(coverCounts(base,3,w)[7]===2,"two menu");
 // Mandatory E/F commitment destroys the opposite goal, even without a suffix budget.
 for(let t=0;t<32;t++){check(coverCounts({t,z:1},6,w)[7]===Infinity,"E commitment");check(coverCounts({t,z:2},6,w)[7]===Infinity,"F commitment")}
 return {result:"PASS_P42_MODEL_MENU_FRONTIER",states:w.length,reachablePairs:pairs,formulaChecks:checks,finiteMultiActionCells:strict,infeasibleCells:infeasible,allThreeGoalHistogram:histogram,emptyNoneBudget2:3,emptyNoneBudget3:2,scope:"P42 recorded finite graph only; no new native Go or original source execution"};
}
console.log(JSON.stringify(trial(),null,2));
