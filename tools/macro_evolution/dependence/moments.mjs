import {frac,add,mul} from './fraction.mjs';
export function moments(p,n){let m=0n,s=0n,o=0n;for(let k=0;k<=n;k++){m+=BigInt(k)*p.w[k];s+=BigInt(k*k)*p.w[k];o+=BigInt(Math.max(0,5*k-3*n))*p.w[k]}const mean=frac(m,p.d*BigInt(n)),second=frac(s,p.d*BigInt(n*n)),variance=add(second,mul(frac(-1),mul(mean,mean))),overflow=frac(o,p.d*BigInt(5*n));return {mean,variance,overflow}}
