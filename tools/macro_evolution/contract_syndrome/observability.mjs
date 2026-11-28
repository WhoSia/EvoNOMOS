export function dot(x,y){let t=x&y,p=0;while(t){t&=t-1;p^=1}return p}

export function image(rows,x){return rows.reduce((s,r,i)=>s|(dot(r,x)<<i),0)}

export function rowProduct(r,M){let v=0;for(let j=0;j<M.length;j++)if(r&(1<<j))v^=M[j];return v}

export function matrixRows(code,d,n){return Array.from({length:n},(_,j)=>(code>>(d*j))&((1<<d)-1))}

export function obsClosure(B,M,d){let O=[],block=B.slice();for(let j=0;j<d;j++){O.push(...block);block=block.map(r=>rowProduct(r,M))}return O}

export function partition(rows,d){const p=new Map();for(let x=0;x<2**d;x++){const z=rows.map(r=>dot(r,x)).join("");if(!p.has(z))p.set(z,[]);p.get(z).push(x)}return [...p.values()]}
