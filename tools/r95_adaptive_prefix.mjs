// R95: bounded P42 graph and a constructed terminal-equivalence counterexample.
// No native Chi execution. Costs count edits, not engineer time.
import assert from 'node:assert/strict';
const pop = n => {let c=0;for(;n;n&=n-1)c++;return c};
const W=Array.from({length:96},(_,i)=>({t:i%32,z:Math.floor(i/32)}));
const key=x=>x.t+32*x.z;
const reach=(x,y)=>(x.t&y.t)===x.t&&(x.z===0||x.z===y.z);
const cost=(x,y)=>pop(x.t^y.t)+Number(x.z!==y.z);
const goals=x=>((x.t&12)===12?1:0)|((x.t&4)&&x.z===1?2:0)|((x.t&8)&&x.z===2?4:0);
const G=[1,2,4];
const edges=W.map(x=>W.filter(y=>reach(x,y)&&cost(x,y)===1).map(key));
// Exactly r real common edits before revelation. Total per-branch budget b.
// Full revelation thereafter; zero extra edits are allowed.
function formula(x,b,r,U){
 if(r>b)return false;
 return W.some(y=>reach(x,y)&&cost(x,y)===r&&G.every(g=>!(U&g)||W.some(z=>reach(y,z)&&cost(y,z)<=b-r&&(goals(z)&g))));
}
// Independent recursive graph search with universal branching at disclosure.
function oracle(i,b,r,U,memo=new Map()){
 if(b<0||r>b)return false;
 const k=[i,b,r,U].join(':');if(memo.has(k))return memo.get(k);
 let ans;
 if(r){ans=edges[i].some(j=>oracle(j,b-1,r-1,U,memo));}
 else if(pop(U)>1){ans=G.every(g=>!(U&g)||oracle(i,b,0,g,memo));}
 else {ans=U===0||Boolean(goals(W[i])&U)||(b>0&&edges[i].some(j=>oracle(j,b-1,0,U,memo)));}
 memo.set(k,ans);return ans;
}
let checks=0,violations=0;const memo=new Map(),hist=[];
for(let b=0;b<=6;b++){
 const row=[];
 for(let r=0;r<=b;r++){
  let yes=0;
  for(const x of W)for(let U=1;U<8;U++){
   const a=formula(x,b,r,U),o=oracle(key(x),b,r,U,memo);assert.equal(a,o);checks++;if(a)yes++;
   if(r&&a&&!formula(x,b,r-1,U))violations++;
  }
  row.push(yes);
 }
 hist.push(row);
}
assert.equal(violations,0);
// Same cost-indexed terminal goal signatures at every integer budget, different
// ability to choose a shared real first edit before learning the goal.
const A={s:['p'],p:['L','R'],L:[],R:[]},B={s:['pL','pR'],pL:['L'],pR:['R'],L:[],R:[]};
function signatures(graph,b){let seen=new Set(['s']),front=['s'];for(let t=0;t<b;t++){front=front.flatMap(v=>graph[v]);front.forEach(v=>seen.add(v));}return [...new Set([...seen].map(v=>v==='L'?1:v==='R'?2:0))].sort();}
function wins(graph){return graph.s.some(p=>graph[p].includes('L')&&graph[p].includes('R'));}
for(let b=0;b<=5;b++)assert.deepEqual(signatures(A,b),signatures(B,b));assert(wins(A));assert(!wins(B));
// P42 start: both E/F goals feasible at total budget 2 when revealed immediately;
// no common first real edit fits both within that budget; at budget 3 C is common.
assert(formula(W[0],2,0,6));assert(!formula(W[0],2,1,6));assert(formula(W[0],3,1,6));
console.log(JSON.stringify({result:'PASS_R95',states:W.length,formulaOracleChecks:checks,delayMonotonicityViolations:violations,feasibleCountsByBudgetAndDisclosureDelay:hist,terminalEquivalentCounterexample:{A:wins(A),B:wins(B)},emptyNone:{budget2Immediate:true,budget2AfterOne:false,budget3AfterOne:true},scope:'historical finite P42 graph; synthetic costs; no native Go/Lean'},null,2));
