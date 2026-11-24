// R90: cross-block discrete mixed-difference bound. Integer test fixtures, not empirical evidence.
function check(b,m){if(!b)throw Error(m)}

function partitions(n){
 const result=[];
 function go(i,blocks){if(i===n){result.push(blocks.slice());return}
 for(let j=0;j<blocks.length;j++){let b=blocks[j];blocks[j]|=1<<i;go(i+1,blocks);blocks[j]=b}
 blocks.push(1<<i);go(i+1,blocks);blocks.pop()}
 go(0,[]);return result;
}

function certify(n,v,blocks){
 if(!Number.isInteger(n)||n<1||n>12||v.length!==2**n||!v.every(Number.isSafeInteger))throw Error("finite bounded integer table required");
 const N=2**n;let seen=0;
 for(const b of blocks){if(!Number.isInteger(b)||b<=0||b>=N||(seen&b))throw Error("invalid partition");seen|=b}
 if(seen!==N-1)throw Error("incomplete partition");
 const eps=[];
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
 const a=1<<i,b=1<<j;
 if(blocks.some(t=>(t&a)&&(t&b)))continue;
 let e=0;
 for(let s=0;s<N;s++)if(!(s&(a|b)))e=Math.max(e,Math.abs(v[s|a|b]-v[s|a]-v[s|b]+v[s]));
 eps.push([a,b,e])
 }
 let cases=0,maxError=0,maxBound=0;
 for(let s=0;s<N;s++){
 const predicted=v[0]+blocks.reduce((sum,b)=>sum+v[s&b]-v[0],0);
 const error=Math.abs(v[s]-predicted);
 const bound=eps.reduce((sum,[a,b,e])=>sum+((s&a)&&(s&b)?e:0),0);
 check(error<=bound,"cross-interaction bound violated");
 cases++;maxError=Math.max(maxError,error);maxBound=Math.max(maxBound,bound)
 }
 return {cases,maxError,maxBound};
}

function trial(){
 let checks=0;
 for(let f=0;f<256;f++){
 const v=Array.from({length:8},(_,s)=>(f>>s)&1);
 for(const p of partitions(3))checks+=certify(3,v,p).cases;
 }
 const v=Array.from({length:8},(_,s)=>((s&3)===3?2:0)+((s&5)===5?3:0)+((s&6)===6?4:0));
 const tight=certify(3,v,[1,2,4]);
 check(tight.maxError===9&&tight.maxBound===9,"tight witness");
 return {checks,functions:256,partitions_per_function:5,tight_witness:tight,scope:"exhaustive 3-variable binary-valued tables; analytic bound for finite real-valued tables separately proved"};
}
console.log(JSON.stringify(trial(),null,2));
