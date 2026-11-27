export function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a||1n}

export function frac(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const d=gcd(a,b);return [a/d,b/d]}

export function add(x,y){return frac(x[0]*y[1]+y[0]*x[1],x[1]*y[1])}

export function mul(x,y){return frac(x[0]*y[0],x[1]*y[1])}

export function cmp(x,y){const d=x[0]*y[1]-y[0]*x[1];return d<0n?-1:d>0n?1:0}

export function fmt(x){return x[1]===1n?String(x[0]):`${x[0]}/${x[1]}`}

export function num(x){return Number(x[0])/Number(x[1])}
