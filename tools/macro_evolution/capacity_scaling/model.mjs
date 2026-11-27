import {kernel} from './kernel.mjs';
export function countModel(n,h,q,r){if(!Number.isInteger(n)||!Number.isInteger(h)||n<1||h<0||h>n||q<0||q>1||r<0)throw Error("invalid model");return Array.from({length:n+1},(_,k)=>Array.from({length:Math.min(k,h)+1},(_,b)=>({b,c:k+r*b,row:kernel(n,k,b,q)})))}
