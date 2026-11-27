import {threshold} from './threshold.mjs';
export function localRelaxed(q,r,g,lambda){const d=r+lambda;const never1=1/(1-g),never0=g*q*never1/(1-g*(1-q));const repair0=g*q*(1+d)/(1-g),repair1=repair0+1+d;return [Math.min(never0,repair0),Math.min(never1,repair1)]}

export function dualBound(n,k,h,q,r,g){const candidates=[0,Math.max(0,threshold(q,g)-r)];const vals=candidates.map(lambda=>{const v=localRelaxed(q,r,g,lambda);return {lambda,lower:(n-k)*v[0]+k*v[1]-lambda*h/(1-g)}});return vals.reduce((a,b)=>a.lower>=b.lower?a:b)}
