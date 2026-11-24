// R90: mathematical graph semantics, not empirical software evidence.
function dist(vertices,edges){
 const n=vertices.length,a=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?0:Infinity));
 for(const [i,j,w] of edges){if(!Number.isFinite(w)||w<0)throw Error("invalid edge");a[i][j]=Math.min(a[i][j],w)}
 for(let k=0;k<n;k++)for(let i=0;i<n;i++)for(let j=0;j<n;j++)a[i][j]=Math.min(a[i][j],a[i][k]+a[k][j]);return a;
}

function check(b,msg){if(!b)throw Error(msg)}

function trial(){
 const localA=[[0,1,1],[1,0,4]],localB=[[0,1,2],[1,0,3]];
 const v=[[0,0],[0,1],[1,0],[1,1]], a=dist([0,1],localA),b=dist([0,1],localB);
 const index=(x,y)=>2*x+y;
 const edges=[];
 for(let x=0;x<2;x++)for(let y=0;y<2;y++){
 for(const [i,j,w] of localA)if(i===x)edges.push([index(x,y),index(j,y),w]);
 for(const [i,j,w] of localB)if(i===y)edges.push([index(x,y),index(x,j),w]);
 }
 const d=dist(v,edges);let count=0,tri=0;
 for(let i=0;i<4;i++)for(let j=0;j<4;j++){
 check(d[i][j]===a[v[i][0]][v[j][0]]+b[v[i][1]][v[j][1]],"product decomposition");count++;
 for(let k=0;k<4;k++){check(d[i][k]<=d[i][j]+d[j][k],"triangle");tri++}
 }
 // A coupling contract x=y, with one-coordinate changes only, blocks both endpoints.
 const blocked=dist([[0,0],[1,1]],[])[0][1];check(blocked===Infinity,"blocked contract");
 // Simultaneous operation can instead make distance smaller than projection sum.
 const shortcut=dist(v,[...edges,[0,3,1]])[0][3];check(shortcut===1&&d[0][3]===3,"atomic shortcut");
 // Penalty charged in another coordinate changes lifts (non-product).
 const penaltyEdges=edges.map(([i,j,w])=>[i,j,w+((i===2&&j===3)||(i===1&&j===3)?5:0)]);
 const p=dist(v,penaltyEdges);check(p[0][3]===8,"coupled penalty");
 return {product_pairs:count,triangle_cases:tri,forward:d[0][3],reverse:d[3][0],blocked:"Infinity",atomic_shortcut:shortcut,coupled_penalty:p[0][3],scope:"constructed finite examples"};
}
console.log(JSON.stringify(trial(),null,2));
