// R96: finite synthetic owner-veto game; not an empirical software cost model.
import assert from 'node:assert/strict';
// Local fallback costs L. Shared repair costs S. Proposer pays p even on rejection.
// B receives transfer t on acceptance; A pays it. Tie breaks toward fallback/reject.
function solve(L,S,p,t=0){
 const accept=S[1]-t<L[1];
 const proposal=accept?[S[0]+p+t,S[1]-t]:[L[0]+p,L[1]];
 const propose=proposal[0]<L[0];
 return {accept,propose,outcome:propose&&accept?'shared':'local'};
}
let checked=0,transferChecked=0,blocked=0;
for(let a=0;a<=5;a++)for(let b=0;b<=5;b++)for(let c=0;c<=5;c++)for(let d=0;d<=5;d++)for(let p=1;p<=3;p++){
 const L=[a,b],S=[c,d],efficient=c+d+p<a+b;
 const g=solve(L,S,p);
 assert.equal(g.outcome==='shared',a-c>p&&b-d>0);
 if(efficient&&g.outcome==='local')blocked++;
 // Half-integer transfers of either sign suffice for integer costs and strict gains.
 let feasible=false;
 for(let j=-24;j<=24;j++)if(solve(L,S,p,j/2).outcome==='shared')feasible=true;
 assert.equal(feasible,efficient);checked++;transferChecked+=49;
}
// Equal aggregate shared cost, same local fallback and proposal cost, different incidence.
const L=[5,5],p=1,X=[2,4],Y=[0,6];
assert.equal(X[0]+X[1],Y[0]+Y[1]);
assert.equal(solve(L,X,p).outcome,'shared');assert.equal(solve(L,Y,p).outcome,'local');
assert.equal(solve(L,Y,p,2).outcome,'shared');
console.log(JSON.stringify({result:'PASS_R96',checked,transferChecked,efficientButBlocked:blocked,example:{L,p,X,Y,withoutTransfer:[solve(L,X,p),solve(L,Y,p)],withTransfer:solve(L,Y,p,2)},scope:'synthetic complete-information sequential veto; enforceable unrestricted transfers; tie-break against proposal and acceptance; no empirical claim'},null,2));
