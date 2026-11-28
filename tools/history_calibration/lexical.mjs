// Restricted source lexer; not Python AST or dynamic call graph.
export function lexical(sources){
 const modules=new Map(sources.map(x=>[x.path.split("/").at(-1).slice(0,-3),x.path]));
 const rows=[],coverage=[];
 for(const {path,content} of sources){
  const lines=content.split(/\r?\n/), bindings=new Map(), skipped=[], kept=[];
  let recognized=0;
  const names=/^([A-Za-z_]\w*)(?:\s+as\s+([A-Za-z_]\w*))?$/;
  for(let i=0;i<lines.length;i++){
   const line=lines[i]; if(!/^\s*from\s+\./.test(line)){if(!/^\s*(?:from|import)\s+/.test(line))kept.push(line);continue}
   const match=line.match(/^\s*from\s+\.(\w*)\s+import\s+([^#]+?)(?:\s*#.*)?$/);
   if(!match){skipped.push(i+1);continue}
   const parts=match[2].trim().split(",").map(p=>p.trim()).filter(Boolean);
   if(!parts.length||parts.some(p=>!names.test(p))){skipped.push(i+1);continue}
   const pairs=parts.map(p=>p.match(names)).map(m=>[modules.get(match[1]||m[1]),m[2]||m[1]]).filter(([target])=>target&&target!==path);
   if(!pairs.length){skipped.push(i+1);continue}
   recognized++;
   for(const [target,name] of pairs){if(!bindings.has(target))bindings.set(target,new Set());bindings.get(target).add(name)}
  }
  const counts=new Map();
  for(const tok of kept.join("\n").match(/[A-Za-z_]\w*/g)||[])counts.set(tok,(counts.get(tok)||0)+1);
  for(const [target,names] of bindings){const ids=[...names].sort();rows.push({from:path,to:target,identifiers:ids,exposure:ids.reduce((n,k)=>n+(counts.get(k)||0),0)})}
  coverage.push({path,recognized,skipped});
 }
 return {rows,coverage};
}
