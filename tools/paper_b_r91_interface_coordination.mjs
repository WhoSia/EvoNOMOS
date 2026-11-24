// R91: exact finite coordination gap and a tight range bound.
function check(b,m){if(!b)throw Error(m)}

function coord(cost){
 const minima=cost.map(row=>Math.min(...row)),ranges=cost.map((row,i)=>Math.max(...row)-minima[i]);
 const z=Array.from({length:cost[0].length},(_,j)=>cost.reduce((s,row)=>s+row[j],0));
 const independent=minima.reduce((a,b)=>a+b,0),joint=Math.min(...z);
 const common=z.some(v=>v===independent);
 const upper=ranges.reduce((a,b)=>a+b,0)-Math.max(...ranges);
 check(joint-independent>=0&&joint-independent<=upper,"bound");
 check((joint===independent)===cost[0].some((_,j)=>cost.every((row,i)=>row[j]===minima[i])),"equality condition");
 return {gap:joint-independent,upper,common};
}

function trial(){
 let checks=0,tight=0;for(let mask=0;mask<3**6;mask++){
 let x=mask;const c=Array.from({length:3},()=>Array.from({length:2},()=>{let v=x%3;x=Math.floor(x/3);return v}));
 const r=coord(c);checks++;if(r.gap===r.upper)tight++;
 }
 const c=[[0,0,1],[1,0,0],[0,1,0]];
 const pairwise=[[c[0],c[1]],[c[0],c[2]],[c[1],c[2]]].map(coord);
 check(pairwise.every(r=>r.gap===0)&&coord(c).gap===1,"hidden shared-interface incompatibility");
 return {cases:checks,tight_cases:tight,pairwise_gaps:pairwise.map(r=>r.gap),global_gap:coord(c).gap,scope:"finite shared-interface cost matrix"};
}
console.log(JSON.stringify(trial(),null,2));
