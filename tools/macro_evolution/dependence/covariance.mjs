export function blockVariance(n,b,q){if(n%b)throw Error("nondivisible blocks");return b*q*(1-q)/n}

export function dependentBound(n,D,q,r,g){return (1+r)*g*Math.sqrt((D+1)/n)/(2*(1-g)*(1-g*(1-q)))}
