export function choose(n,k){if(k<0||k>n)return 0n;let c=1n;for(let i=1;i<=k;i++)c=c*BigInt(n-i+1)/BigInt(i);return c}

export function mixture(n,weights){const d=8n*4n**BigInt(n);if(weights.reduce((s,w)=>s+w[1],0)!==8)throw Error("weights");const w=Array.from({length:n+1},(_,k)=>choose(n,k)*weights.reduce((s,[theta,m])=>s+BigInt(m)*BigInt(theta)**BigInt(k)*BigInt(4-theta)**BigInt(n-k),0n));if(w.reduce((s,v)=>s+v,0n)!==d)throw Error("PMF");return {w,d}}
