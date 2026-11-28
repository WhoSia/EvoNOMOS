import {parity} from './gf2.mjs';
export function chainWitness(bits){const p=[0];for(const x of bits)p.push(p.at(-1)^x);return {prefix:p,edit:p.at(-1)}}

export function validChain(bits,w){return w.prefix.length===bits.length+1&&w.prefix[0]===0&&w.prefix.at(-1)===w.edit&&bits.every((b,i)=>(w.prefix[i]^b)===w.prefix[i+1])}

export function enumerateParity(n){let even=0,odd=0;const marg=[Array.from({length:n},()=>new Map()),Array.from({length:n},()=>new Map())];for(let x=0;x<2**n;x++){const p=parity(x),bits=Array.from({length:n},(_,i)=>(x>>i)&1);const w=chainWitness(bits);if(!validChain(bits,w)||w.edit!==p)throw Error("chain mismatch");if(p)odd++;else even++;for(let j=0;j<n;j++){const z=bits.filter((_,i)=>i!==j).join("");const m=marg[p][j];m.set(z,(m.get(z)||0)+1)}}for(let j=0;j<n;j++){if(marg[0][j].size!==2**(n-1)||marg[1][j].size!==2**(n-1)||[...marg[0][j]].some(([z,v])=>marg[1][j].get(z)!==v))throw Error("marginal mismatch")}return {n,even,odd,proper_marginal_pairs:n*2**(n-1),mean_cost_even:0,mean_cost_odd:1}}
