// Exact tie-aware ranking metrics, chronological frozen fixture replay.
export function evaluate(sel,features,train,test){
 const u=sel.source.map(x=>x.path), U=new Set(u);
 const check=(rows,expected)=>{if(JSON.stringify(rows.map(x=>x.sha))!==JSON.stringify(expected.filter(x=>x.parents.length<=1).map(x=>x.sha)))throw Error("selection mismatch");if(new Set(rows.map(x=>x.sha)).size!==rows.length)throw Error("duplicate commit");for(const c of rows){if(!c.files.length||new Set(c.files.map(f=>f.path)).size!==c.files.length)throw Error("invalid paths "+c.sha);}};
 check(train,sel.train_candidates);check(test,sel.test_candidates);
 if(train.some(x=>x.date>="2025-01-01T00:00:00Z")||test.some(x=>x.date<"2025-01-01T00:00:00Z")||train.some(x=>test.some(y=>x.sha===y.sha)))throw Error("time leakage");
 if(features.snapshot!==sel.snapshot||JSON.stringify(features.source)!==JSON.stringify(sel.source))throw Error("source mismatch");
 const touched=c=>[...new Set(c.files.flatMap(x=>[x.path,x.previous_path]).filter(x=>U.has(x)))].sort();
 const attrition=rows=>({commits:rows.length,zero:rows.filter(c=>touched(c).length===0).length,one:rows.filter(c=>touched(c).length===1).length,multi:rows.filter(c=>touched(c).length>=2).length,matched_paths:rows.reduce((n,c)=>n+touched(c).length,0),all_path_records:rows.reduce((n,c)=>n+c.files.length,0)});
 const counts=new Map(u.map(a=>[a,0])), pair=new Map(), dir=new Map();
 const key=(a,b)=>JSON.stringify([a,b]);
 for(const c of train){const files=touched(c);for(const a of files){counts.set(a,counts.get(a)+1);for(const b of files)if(a!==b)pair.set(key(a,b),(pair.get(key(a,b))||0)+1)}}
 for(const r of features.rows){if(!U.has(r.from)||!U.has(r.to)||r.from===r.to||!Number.isInteger(r.exposure)||r.exposure<0||dir.has(key(r.from,r.to)))throw Error("invalid feature");dir.set(key(r.from,r.to),r.exposure)}
 const cmp=(a,b)=>{for(let i=0;i<a.length;i++)if(a[i]!==b[i])return Math.sign(a[i]-b[i]);return 0};
 const ranks=scores=>scores.map(s=>scores.reduce((n,t)=>n+(cmp(s,t)>0?1:cmp(s,t)===0?.5:0),0)/scores.length);
 const names=["uniform","marginal","historical_pair","binary_import","lexical_exposure","fusion"];
 function metrics(scores,labels){
  const positive=scores.filter((_,i)=>labels[i]), negative=scores.filter((_,i)=>!labels[i]);if(!positive.length)throw Error("no positive");
  const best=positive.reduce((a,b)=>cmp(a,b)>=0?a:b);let above=0, tied=0,hits=0;
  for(let i=0;i<scores.length;i++){const c=cmp(scores[i],best);if(c>0)above++;if(!c){tied++;hits+=+labels[i]}}
  let survival=1,mrr=0;for(let j=1;j<=tied-hits+1;j++){const p=hits/(tied-j+1);mrr+=survival*p/(above+j);survival*=1-p}
  let auc=null;if(negative.length){let sum=0;for(const p of positive)for(const n of negative){const c=cmp(p,n);sum+=c>0?1:c===0?.5:0}auc=sum/(positive.length*negative.length)}
  return {mrr,auc,top1:above?0:hits/tied};
 }
 const close=(a,b)=>Math.abs(a-b)<1e-12;
 if(!close(metrics([[0],[0],[0]],[true,false,false]).mrr,11/18)||!close(metrics([[0],[0],[0]],[true,true,false]).mrr,5/6)||!close(metrics([[0],[1]],[true,false]).mrr,.5)||metrics([[1],[0]],[true,false]).auc!==1)throw Error("metric selftest");
 const mean=xs=>xs.length?xs.reduce((a,b)=>a+b,0)/xs.length:null;
 const summarize=rows=>Object.fromEntries(names.map(n=>[n,Object.fromEntries(["mrr","auc","top1"].map(k=>[k,mean(rows.map(r=>r[n][k]).filter(x=>x!==null))]))]));
 const rows=[];
 for(const c of test){const files=touched(c);if(files.length<2)continue;const anchors=[];
  for(const a of files){const candidates=u.filter(b=>a!==b),labels=candidates.map(b=>files.includes(b));const hist=candidates.map(b=>{const p=pair.get(key(a,b))||0, den=counts.get(a)+counts.get(b)-p;return [den?p/den:0,counts.get(b)+1]});const marginal=candidates.map(b=>[counts.get(b)+1]);const binary=candidates.map(b=>[+(dir.has(key(a,b))||dir.has(key(b,a)))]);const exp=candidates.map(b=>[(dir.get(key(a,b))||0)+(dir.get(key(b,a))||0)]);const hr=ranks(hist),er=ranks(exp);const f=hr.map((h,i)=>[(h+er[i])/2]);const score=[candidates.map(()=>[0]),marginal,hist,binary,exp,f];anchors.push({anchor:a,positives:files.filter(b=>b!==a),...Object.fromEntries(names.map((n,i)=>[n,metrics(score[i],labels)]))})}
  rows.push({sha:c.sha,date:c.date,files,anchors,...summarize(anchors)});
 }
 return {source_count:u.length,train_attrition:attrition(train),test_attrition:attrition(test),anchor_count:rows.reduce((n,r)=>n+r.anchors.length,0),test_eligible:rows.length,threshold_met:rows.length>=5,scores:summarize(rows),per_commit:rows,scope:"Historical co-change proxy only; lexical exposure not contracts or dynamic calls; conditional on at least two cutoff source paths; no population or causal claim."};
}
