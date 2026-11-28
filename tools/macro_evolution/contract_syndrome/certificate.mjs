import {parity} from './gf2.mjs';
export function infeasibleWitness(cols,s,rows){for(let y=1;y<2**rows;y++)if(parity(y&s)&&cols.every(c=>!parity(y&c)))return y;return null}
