export function binomial(n,q){let p=[1];for(let i=0;i<n;i++){let z=Array(i+2).fill(0);for(let j=0;j<p.length;j++){z[j]+=p[j]*(1-q);z[j+1]+=p[j]*q}p=z}return p}

export function kernel(n,k,b,q){if(!Number.isInteger(b)||b<0||b>k||k>n||k<0)throw Error("invalid counts");const stuck=k-b;return {offset:stuck,p:binomial(n-stuck,q)}}

export function expectation(row,v){return row.p.reduce((s,p,j)=>s+p*v[row.offset+j],0)}
