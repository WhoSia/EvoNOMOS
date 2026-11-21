"""Exact shortest decision-conflict witness by finite set-cover dynamic programming.

Classical finite DP adapted to context-collapsed source-boundary decisions.
For K feasible actions and N contexts: O(N*2^K*K); no full source extraction.
"""

def shortest_conflict_witness(opt_sets, n_actions):
    if n_actions < 1 or any(not s or any(a<0 or a>=n_actions for a in s)
                             for s in opt_sets):
        raise ValueError("every context must have a valid nonempty optimal-action set")
    target=(1<<n_actions)-1
    best={0:()}
    for i,opt in enumerate(opt_sets):
        excluded=target ^ sum(1<<a for a in set(opt))
        updated=dict(best)
        for mask,path in best.items():
            newmask=mask|excluded
            candidate=path+(i,)
            if newmask not in updated or (
                    len(candidate),candidate)<(len(updated[newmask]),updated[newmask]):
                updated[newmask]=candidate
        best=updated
    return best.get(target)
