import {threshold} from './threshold.mjs';
export function fluidStep(y,alpha,q,repair){return q+(1-q)*(y-(repair?Math.min(y,alpha):0))}

export function fluidValue(y,alpha,q,r,g,tol=1e-10){const repair=r<threshold(q,g);let v=0,d=1,steps=0;for(;d*(1+r)/(1-g)>tol;steps++){v+=d*(y+r*(repair?Math.min(y,alpha):0));y=fluidStep(y,alpha,q,repair);d*=g}return {v,tail:d*(1+r)/(1-g),steps}}

export function fluidBound(n,q,r,g){return (1+r)*g/(2*Math.sqrt(n)*(1-g)*(1-g*(1-q)))}

export function fluidEquilibrium(alpha,q,repair){if(q<=0)throw Error("q>0 required");return repair?(alpha>=q?q:1-(1-q)*alpha/q):1}
