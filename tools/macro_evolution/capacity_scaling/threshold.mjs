export function threshold(q,g){return g*(1-q)/(1-g*(1-q))}

export function baseCost(n,k,q,g){return (k+g*q*n/(1-g))/(1-g*(1-q))}

export function optimalRepairs(k,h,q,r,g){return r<threshold(q,g)?Math.min(k,h):0}
