// R90: OCP option premium and minimax regret under uncertain demand; illustrative known decision theory.
function verify(x,m){if(!x)throw Error(m)}

function trial(){
 // Rational scaled units: q in [3/10,6/10]; p = probability of selecting M.
 const M=q=>4-2*q,S=q=>1+5*q;
 const lo=.3,hi=.6;
 const regret=(p,q)=>p*M(q)+(1-p)*S(q)-Math.min(M(q),S(q));
 const risk=p=>Math.max(regret(p,lo),regret(p,hi));
 const p=4/7, val=18/35;
 verify(Math.abs(risk(p)-val)<1e-12,"regret intersection");
 for(let i=0;i<=1000;i++)verify(risk(i/1000)>=val-1e-12,"grid contradicts optimum");
 // OCP seam with upfront premium h and per-demand savings delta.
 // E[benefit] >= 0 precisely when sum p_d delta_d >= h.
 const premium=3, savings=[0,7];
 const threshold=premium/savings[1];
 verify(Math.abs(threshold-3/7)<1e-12,"break-even");
 // Two demand worlds forbid universal recommendation when each has a different strict winner.
 verify(M(0)>S(0)&&M(1)<S(1),"preference reversal");
 return {pure_M_max_regret:risk(1),pure_S_max_regret:risk(0),randomized_M_probability:p,randomized_max_regret:val,grid_checks:1001,break_even:threshold,scope:"illustrative costs; randomizing over designs is a mathematical relaxation, not a recommendation for a single codebase"};
}
console.log(JSON.stringify(trial(),null,2));
