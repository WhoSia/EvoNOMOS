export function parity(x){let p=0;while(x){p^=1;x&=x-1}return p}

export function xorProduct(cols,mask){let s=0;for(let j=0;j<cols.length;j++)if(mask&(1<<j))s^=cols[j];return s}

export function rank(cols){const basis=new Map();for(let v of cols){while(v){const bit=31-Math.clz32(v);if(basis.has(bit))v^=basis.get(bit);else{basis.set(bit,v);break}}}return basis.size}
