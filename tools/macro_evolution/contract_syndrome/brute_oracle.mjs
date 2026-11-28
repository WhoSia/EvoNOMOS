import {xorProduct} from './gf2.mjs';
export function brute(cols,weights){const d=new Map();for(let mask=0;mask<2**cols.length;mask++){const s=xorProduct(cols,mask);let cost=0;for(let j=0;j<cols.length;j++)if(mask&(1<<j))cost+=weights[j];if(!d.has(s)||cost<d.get(s))d.set(s,cost)}return d}
