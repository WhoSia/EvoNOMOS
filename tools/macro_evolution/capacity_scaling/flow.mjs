import {baseCost,threshold} from './threshold.mjs';
export function repairFlow(n,k,q,r,g,discountedRepairs){return baseCost(n,k,q,g)+(r-threshold(q,g))*discountedRepairs}

export function invariantCheck(n,h,k1,k2,b2){const b1=Math.min(k1,h);return k1<=k2&&b2<=Math.min(k2,h)&&b2>=0&&k1-b1<=k2-b2}
