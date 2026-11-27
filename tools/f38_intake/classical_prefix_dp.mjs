/* Generic bounded reachability with real pre-disclosure edits. Classical DP; no inferred source or ownership. */
export function boundedPrefixDP(edges, goalMask, maxBudget, maxGoalMask) {
  if (!Array.isArray(edges) || edges.length !== goalMask.length) throw Error("graph shape");
  const n=edges.length;
  for (const adj of edges) if (!Array.isArray(adj)||adj.some(j=>!Number.isInteger(j)||j<0||j>=n)) throw Error("edge");
  if (!Number.isInteger(maxBudget)||maxBudget<0||!Number.isInteger(maxGoalMask)||maxGoalMask<1||maxGoalMask>255) throw Error("bounds");
  const possible=[Uint8Array.from(goalMask)];
  for(let b=1;b<=maxBudget;b++){
    const prev=possible[b-1];
    possible.push(Uint8Array.from(prev,(v,i)=>edges[i].reduce((m,j)=>m|prev[j],v)));
  }
  const table=[];
  for(let b=0;b<=maxBudget;b++){
    const row=[];
    for(let r=0;r<=b;r++){
      const masks=[];
      for(let U=1;U<=maxGoalMask;U++){
        if(r===0) masks[U]=Uint8Array.from(possible[b],m=>Number((m&U)===U));
        else {const prev=table[b-1][r-1][U];masks[U]=Uint8Array.from(edges,adj=>Number(adj.some(j=>prev[j])));}
      }
      row.push(masks);
    }
    table.push(row);
  }
  return table;
}
export function replayR95(){
  const pop=n=>{let c=0;for(;n;n&=n-1)c++;return c};
  const W=Array.from({length:96},(_,i)=>({t:i%32,z:Math.floor(i/32)}));
  const reach=(x,y)=>(x.t&y.t)===x.t&&(x.z===0||x.z===y.z);
  const cost=(x,y)=>pop(x.t^y.t)+Number(x.z!==y.z);
  const goals=x=>((x.t&12)===12?1:0)|((x.t&4)&&x.z===1?2:0)|((x.t&8)&&x.z===2?4:0);
  const G=[1,2,4];
  const edges=W.map(x=>W.map((y,i)=>({y,i})).filter(({y})=>reach(x,y)&&cost(x,y)===1).map(({i})=>i));
  const table=boundedPrefixDP(edges,W.map(goals),6,7);
  const formula=(x,b,r,U)=>W.some(y=>reach(x,y)&&cost(x,y)===r&&G.every(g=>!(U&g)||W.some(z=>reach(y,z)&&cost(y,z)<=b-r&&(goals(z)&g))));
  let checks=0,mismatches=0;
  const hist=[];
  for(let b=0;b<=6;b++){const row=[];for(let r=0;r<=b;r++){let yes=0;for(let U=1;U<8;U++)for(let i=0;i<W.length;i++){const a=Boolean(table[b][r][U][i]),f=formula(W[i],b,r,U);checks++;if(a!==f)mismatches++;if(a)yes++;}row.push(yes);}hist.push(row);}
  if(checks!==18816||mismatches!==0)throw Error("R95 differential check failed");
  const a=boundedPrefixDP([[1],[2,3],[],[]],[0,0,1,2],2,3),b=boundedPrefixDP([[1,2],[3],[4],[],[]],[0,0,0,1,2],2,3);
  if(!a[2][1][3][0]||b[2][1][3][0])throw Error("prefix counterexample failed");
  return {scope:"historical graph replay; exact supplied unit-cost edges, not new source or future prediction",states:W.length,edges:edges.reduce((n,e)=>n+e.length,0),checks,mismatches,feasibleCounts:hist,terminalCounterexample:{commonPrefixA:Boolean(a[2][1][3][0]),commonPrefixB:Boolean(b[2][1][3][0])},verdict:"CLASSICAL_TIE"};
}
