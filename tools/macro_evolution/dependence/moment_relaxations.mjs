export function cantelliOverflow(mu,v,a){if(a<=mu)throw Error("upper-tail threshold required");return (1-a)*v/(v+(a-mu)**2)}

export function stopLossBound(mu,v,a){return (Math.sqrt(v+(mu-a)**2)+mu-a)/2}
