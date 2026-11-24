// R93: irreversible common-prefix action menus; finite witness, not an empirical claim.
function assert(b,m){if(!b)throw Error(m)}

function masksCover(sets,n){
 const full=(1n<<BigInt(n))-1n;
 let reachable=new Map([[0n,0]]);
 for(const s of sets){const next=new Map(reachable);for(const [a,k] of reachable){const b=a|s;if(k+1<(next.get(b)??Infinity))next.set(b,k+1)}reachable=next}
 return reachable.get(full)??Infinity
}

function trial(){
 const rows=[];
 for(let m=1;m<=8;m++){
  const lo=(1n<<BigInt(m))-1n,hi=lo<<BigInt(m);
  const p=[lo,...Array.from({length:m},(_,i)=>1n<<BigInt(m+i))];
  const q=[hi,...Array.from({length:m},(_,i)=>1n<<BigInt(i))];
  const late=masksCover([...p,...q],2*m),early=Math.min(masksCover(p,2*m),masksCover(q,2*m));
  assert(late===2&&early===m+1,"prefix obstruction");
  assert(p.reduce((a,b)=>a|b,0n)===(lo|hi)&&q.reduce((a,b)=>a|b,0n)===(lo|hi),"each prefix must remain feasible in every world");
  rows.push({m,worlds:2*m,early,late});
 }
 return {result:"PASS_PREFIX_MENU_GAP",rows,scope:"deterministic zero-error action menu, equal unit path cost, no world-dependent first-stage decision before disclosure"}
}
console.log(JSON.stringify(trial(),null,2));
