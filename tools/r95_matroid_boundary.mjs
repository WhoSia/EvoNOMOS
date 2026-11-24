// R95: the recorded P42 admission family is a partition matroid, but the
// customer-goal and delayed-information constraints are not matroid exchange.
import assert from 'node:assert/strict';
const pc=n=>{let c=0;for(;n;n&=n-1)c++;return c};
const I=Array.from({length:128},(_,s)=>s).filter(s=>(s&96)!==96);
const admissible=s=>(s&96)!==96;
let hereditary=0,exchange=0;
for(const s of I){for(let t=s;;t=(t-1)&s){assert(admissible(t));hereditary++;if(!t)break;}}
for(const s of I)for(const t of I)if(pc(s)<pc(t)){
 assert(Array.from({length:7},(_,i)=>1<<i).some(e=>(t&e)&&!(s&e)&&admissible(s|e)));exchange++;
}
const bases=I.filter(s=>pc(s)===6);assert.deepEqual(bases,[63,95]);
const G=[1,2,4];
function goals(s){return ((s&12)===12?1:0)|((s&36)===36?2:0)|((s&72)===72?4:0);}
function feasible(s,g,b){return I.some(t=>(s&t)===s&&pc(t^s)<=b&&(goals(t)&g));}
// EC and FD each require two edits from empty. The prefix must preserve both.
assert(G.slice(1).every(g=>feasible(0,g,2)));
const shared=Array.from({length:7},(_,i)=>1<<i).filter(s=>G.slice(1).every(g=>feasible(s,g,1)));
const shared3=Array.from({length:7},(_,i)=>1<<i).filter(s=>G.slice(1).every(g=>feasible(s,g,2)));
assert.deepEqual(shared,[]);assert.deepEqual(shared3,[1,2,4,8,16]);
// Goal satisfaction itself is not hereditary: EC is satisfied, E alone is not.
assert(goals(36)&2);assert.equal(goals(32)&2,0);
console.log(JSON.stringify({result:'PASS_R95_MATROID_BOUNDARY',admissionSets:I.length,rank:6,bases,hereditaryChecks:hereditary,exchangeChecks:exchange,sharedFirstEditBudget2:shared,sharedFirstEditBudget3:shared3,scope:'partition matroid of recorded add-only installed sets, not arbitrary software contracts or a contradiction of recoverable robust optimization'},null,2));
