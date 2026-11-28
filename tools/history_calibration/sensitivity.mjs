// Posthoc audit sensitivity; not confirmatory.
export function sensitivity(sel,features,train,test,audit,original){
 const nonancestor=new Set(audit.filter(x=>x.ahead>0&&x.status==="diverged").map(x=>x.sha));
 const filtered=train.filter(x=>!nonancestor.has(x.sha));
 const paths=sel.source.map(x=>x.path), valid=new Set(paths);
 const touched=c=>[...new Set(c.files.flatMap(f=>[f.path,f.previous_path]).filter(p=>valid.has(p)))];
 const n=new Map(paths.map(p=>[p,0])), pair=new Map(), exposure=new Map();
 const key=(a,b)=>a+"\t"+b;
 for(const c of filtered){const p=touched(c);for(const a of p){n.set(a,n.get(a)+1);for(const b of p)if(a!==b)pair.set(key(a,b),(pair.get(key(a,b))||0)+1)}}
 for(const r of features.rows)exposure.set(key(r.from,r.to),r.exposure);
 const cmp=(x,y)=>{for(let i=0;i<x.length;i++)if(x[i]!==y[i])return Math.sign(x[i]-y[i]);return 0};
 const rank=a=>a.map(x=>a.reduce((s,y)=>s+(cmp(x,y)>0?1:cmp(x,y)===0?.5:0),0)/a.length);
 const mean=a=>a.reduce((s,x)=>s+x,0)/a.length;
 // Independent exact combinatorial distribution of rank of first relevant item.
 function choose(n,k){if(k<0||k>n)return 0;let x=1;for(let i=1;i<=k;i++)x=x*(n-i+1)/i;return x}
 function mrr(score,label){let best=score.filter((_,i)=>label[i]).reduce((a,b)=>cmp(a,b)>0?a:b),g=0,t=0,h=0;score.forEach((s,i)=>{const c=cmp(s,best);if(c>0)g++;if(!c){t++;h+=+label[i]}});let sum=0;for(let j=1;j<=t-h+1;j++)sum+=choose(t-j,h-1)/choose(t,h)/(g+j);return sum}
 const methods=["marginal","historical_pair","lexical_exposure","fusion"];
 const rows=[];
 for(const c of test){let p=touched(c);if(p.length<2)continue;
  const all=p.map(a=>{let candidates=paths.filter(b=>b!==a),labels=candidates.map(b=>p.includes(b));let marginal=candidates.map(b=>[n.get(b)+1]),hist=candidates.map(b=>{let joint=pair.get(key(a,b))||0,den=n.get(a)+n.get(b)-joint;return[den?joint/den:0,n.get(b)+1]}),exp=candidates.map(b=>[(exposure.get(key(a,b))||0)+(exposure.get(key(b,a))||0)]),h=rank(hist),e=rank(exp),fusion=h.map((v,i)=>[(v+e[i])/2]);return [marginal,hist,exp,fusion].map(s=>mrr(s,labels))});
  rows.push({sha:c.sha,mrr:Object.fromEntries(methods.map((m,i)=>[m,mean(all.map(r=>r[i]))]))})
 }
 const scores=Object.fromEntries(methods.map(m=>[m,mean(rows.map(r=>r.mrr[m]))]));
 const allMethods=Object.keys(original.scores);
 const loo=Object.fromEntries(allMethods.map(m=>{let x=original.per_commit.map((_,i)=>mean(original.per_commit.filter((_,j)=>j!==i).map(r=>r[m].mrr)));return[m,{min:Math.min(...x),max:Math.max(...x)}]}));
 return {nonancestor_candidates:nonancestor.size,nonancestor_nonmerge:train.length-filtered.length,remaining_training_commits:filtered.length,remaining_training_multi:filtered.filter(c=>touched(c).length>=2).length,unchanged_test_commits:rows.length,posthoc_ancestor_subset_mrr:scores,original_lexical_mrr:original.scores.lexical_exposure.mrr,original_mrr_leave_one_commit_out:loo,rows,scope:"Posthoc exclusion, no refill; sensitivity diagnostic only. Four original held-out commits; not a repaired confirmatory test. Does not validate holdout ancestry or branch observability."}
}
