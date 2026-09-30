#!/usr/bin/env node
const fs=require("fs");
const http=require("http");
const path=require("path");

const [worldDir,outPath]=process.argv.slice(2);
if(!worldDir||!outPath) throw new Error("usage: indigo-oracle <worldDir> <out>");

const providerPath=path.resolve(worldDir,"indigo.js");
const parentPath=path.resolve(worldDir,"notification-provider.js");

fs.writeFileSync(parentPath,`
class NotificationProvider {
  getAxiosConfigWithProxy(config){ return config; }
  throwGeneralAxiosError(error){ throw error; }
}
module.exports = NotificationProvider;
`);

const axiosDir=path.resolve(worldDir,"node_modules","axios");
fs.mkdirSync(axiosDir,{recursive:true});
fs.writeFileSync(path.join(axiosDir,"index.js"),`
const http=require("http");
const https=require("https");
async function post(url,data,config={}){
  return new Promise((resolve,reject)=>{
    const u=new URL(url);
    const lib=u.protocol==="https:"?https:http;
    const body=JSON.stringify(data);
    const headers={...(config.headers||{}),"Content-Length":Buffer.byteLength(body)};
    const req=lib.request({hostname:u.hostname,port:u.port,path:u.pathname+u.search,method:"POST",headers,agent:config.httpsAgent},res=>{
      let chunks="";
      res.on("data",d=>chunks+=d);
      res.on("end",()=>{
        let parsed={}; try{parsed=chunks?JSON.parse(chunks):{};}catch{}
        if(res.statusCode>=400){ const e=new Error("HTTP "+res.statusCode); e.response={status:res.statusCode,data:parsed}; reject(e); }
        else resolve({status:res.statusCode,data:parsed});
      });
    });
    req.on("error",reject); req.write(body); req.end();
  });
}
module.exports={post};
`);

const Indigo=require(providerPath);

function assert(x,m){if(!x) throw new Error(m);}

async function main(){
  const requests=[];
  let reply={success:true};
  let status=200;
  const server=http.createServer((req,res)=>{
    let body="";
    req.on("data",d=>body+=d);
    req.on("end",()=>{
      requests.push({auth:req.headers.authorization,body:JSON.parse(body||"{}")});
      res.statusCode=status;
      res.setHeader("Content-Type","application/json");
      res.end(JSON.stringify(reply));
    });
  });
  await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));
  const port=server.address().port;
  const baseUrl=`http://127.0.0.1:${port}`;
  const notification={indigoUrl:baseUrl,indigoApiKey:"key",indigoVariableId:"111",indigoActionGroupId:"222"};

  const result=await new Indigo().send(notification,"transport-check");
  assert(result==="Sent Successfully.","unexpected success result");
  assert(requests.length===2,"expected two commands");
  assert(requests[0].auth==="Bearer key","auth header");
  assert(requests[0].body.message==="indigo.variable.updateValue","variable command");
  assert(requests[0].body.objectId===111,"variable id");
  assert(requests[0].body.parameters.value==="transport-check","message propagation");
  assert(requests[1].body.message==="indigo.actionGroup.execute","action-group command");
  assert(requests[1].body.objectId===222,"action group id");

  let missingRejected=false;
  try{ await new Indigo().send({indigoUrl:baseUrl,indigoApiKey:"key"},"x"); }catch(e){ missingRejected=/variable ID, an action group ID/.test(String(e.message)); }
  assert(missingRejected,"missing target should reject");

  status=200; reply={error:"object not found"};
  let bodyError=false;
  try{ await new Indigo().send({indigoUrl:baseUrl,indigoApiKey:"key",indigoActionGroupId:"999"},"x"); }catch(e){ bodyError=/object not found/.test(String(e.message)); }
  assert(bodyError,"response-body error should reject");

  server.close();

  const out={
    schema_version:"law-r1-p4-indigo-real-implementation-v1",
    provider_source:"louislam/uptime-kuma@e62702d868a0b072c6e1870e5278762319637f04/server/notification-providers/indigo.js",
    provider_bytes:"REAL_MERGED_UPSTREAM",
    oracle:"LOCAL_HTTP_SERVER__INDEPENDENT_REIMPLEMENTATION_OF_UPSTREAM_TEST_INTENT",
    verified:[
      "bearer-auth-header",
      "variable-command-before-action-group",
      "message-payload-transport",
      "requires-variable-or-action-group",
      "provider-response-body-error-propagation"
    ],
    production_indigo_service_contact:false,
    verdict:"PASS_REAL_IMPLEMENTATION_LOCAL_HTTP_ORACLE"
  };
  fs.mkdirSync(path.dirname(outPath),{recursive:true});
  fs.writeFileSync(outPath,JSON.stringify(out,null,2)+"\n");
  console.log("LAW_R1_P4_INDIGO_REAL_IMPLEMENTATION=PASS");
}
main().catch(e=>{console.error(e);process.exit(1);});
