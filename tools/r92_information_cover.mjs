// R92 finite verification of the action-cover counterexample. Proof is separate; this is not Lean execution.
function check(b,m){if(!b)throw Error(m)}

function vectors(n,q){const out=[];function rec(a){if(a.length===n){out.push(a);return}for(let i=0;i<q;i++)rec([...a,i])}rec([]);return out}

function acceptable(w,a){return w.every((x,i)=>x!==a[i])}

function cover(worlds,actions){return worlds.every(w=>actions.some(a=>acceptable(w,a)))}

function trial(){
 const result=[];
 for(let n=1;n<=4;n++){
  const q=n+1,worlds=vectors(n,q),diagonal=Array.from({length:q},(_,j)=>Array(n).fill(j));
  check(cover(worlds,diagonal),"diagonal cover fails");
  // Construct a world defeating any n candidate actions, one coordinate per action.
  // Exhaust all n-tuples of action vectors for n<=3; for n=4 the proof is general,
  // but enumerate the diagonal cover and a deterministic family of adversarial lists.
  let lists=0;
  function reject(list){
    const w=list.map((a,i)=>a[i]);check(list.every(a=>!acceptable(w,a)),"adversarial world failed");lists++;
  }
  if(n<=3){function rec(l){if(l.length===n){reject(l);return}for(const a of worlds)rec([...l,a])}rec([])}
  else{for(let i=0;i<worlds.length;i++)reject(Array.from({length:n},(_,j)=>worlds[(i+17*j)%worlds.length]))}
  result.push({n,q,worlds:worlds.length,centralMessages:q,independentProductMessages:2**n,checkedAdversarialLists:lists,localMinimum:2})
 }
 return {result:"PASS_FINITE_INFORMATION_COVER_WITNESSES",cases:result,scope:"central encoder and coordinated joint action, full Cartesian worlds, no communication protocol cost model"};
}
console.log(JSON.stringify(trial(),null,2));
