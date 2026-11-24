// R90: demand-cost interaction graph; known separability principle applied to a complete finite cost table.
function assert(b,msg){if(!b)throw Error(msg)}

function analyze(n,values){
 const max=1<<n;
 if(values.length!==max||!values.every(Number.isFinite))throw Error("finite complete cost table required");
 const parent=Array.from({length:n},(_,i)=>i);
 function root(i){while(parent[i]!==i){i=parent[i]}return i}
 const witness=[];let maxAbs=0;
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
 const a=1<<i,b=1<<j;
 for(let s=0;s<max;s++)if(!(s&(a|b))){
 const delta=values[s|a|b]-values[s|a]-values[s|b]+values[s];maxAbs=Math.max(maxAbs,Math.abs(delta));
 if(delta!==0){parent[root(i)]=root(j);witness.push({i,j,background:s,delta})}
 }}
 const groups={};for(let i=0;i<n;i++)(groups[root(i)]??=[]).push(i);
 const blocks=Object.values(groups).map(g=>g.reduce((m,i)=>m|(1<<i),0));
 for(let s=0;s<max;s++){
 const reconstructed=values[0]+blocks.reduce((t,b)=>t+values[s&b]-values[0],0);
 assert(reconstructed===values[s],"reconstruction failed");
 }
 return {blocks:Object.values(groups),witness,maxAbs};
}

function trial(){
 let triple=Array.from({length:8},(_,s)=>[0,1,2].filter(i=>s&(1<<i)).length+(s===7?6:0));
 const t=analyze(3,triple);assert(t.blocks.length===1,"triple interaction");
 assert(t.witness.every(w=>w.background!==0),"empty background failed to hide interaction");
 let additive=Array.from({length:16},(_,s)=>3+((s&1)?2:0)+((s&2)?3:0)+((s&3)===3?5:0)+((s&4)?4:0)+((s&8)?6:0));
 const a=analyze(4,additive);assert(a.blocks.length===3,"expected three blocks");
 // All binary-valued 3-demand cost tables; exhaustive reconstruction.
 let tables=0;
 for(let x=0;x<256;x++){analyze(3,Array.from({length:8},(_,s)=>(x>>s)&1));tables++}
 return {tables,triple_interaction:t,additive_blocks:a.blocks,scope:"finite exact cost functions; not software architecture discovery"};
}
console.log(JSON.stringify(trial(),null,2));
