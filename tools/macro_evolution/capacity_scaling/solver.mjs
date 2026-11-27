import {expectation} from './kernel.mjs';
export function backup(model,v,g,policy=null){return model.map((acts,k)=>{const cand=policy?acts.filter(a=>a.b===policy[k]):acts;if(!cand.length)throw Error("invalid policy");return Math.min(...cand.map(a=>a.c+g*expectation(a.row,v)))})}

export function maxdiff(a,b){return Math.max(...a.map((x,i)=>Math.abs(x-b[i])))}

export function iterate(model,g,policy=null,tol=1e-9){let v=model.map(()=>0),steps=0;for(;steps<10000;steps++){let w=backup(model,v,g,policy);v=w;const residual=maxdiff(backup(model,v,g,policy),v);if(residual<tol*(1-g))return {v,steps:steps+1,residual,errorBound:residual/(1-g)}}throw Error("no convergence")}
