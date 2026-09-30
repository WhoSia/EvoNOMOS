from __future__ import annotations
import importlib.util, json, os, re, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path
from groq import Groq
from google import genai
from google.genai import types

STAGE="EVONOMOS-G8-LAW-R1-P5-HOST"
SCIENCE_SHA="378cb1cfe3a9506d2f7aefa5ea5eb2effd7a7d45"
MODELS={
 "gptoss20":{"provider":"groq","family":"gpt-oss","model":"openai/gpt-oss-20b"},
 "gptoss120":{"provider":"groq","family":"gpt-oss","model":"openai/gpt-oss-120b"},
 "gemini":{"provider":"gemini","family":"gemini","model":"gemini-3.5-flash-lite"},
}
SCHEMA={
 "type":"object",
 "properties":{
   "choice":{"type":"string","enum":["Option 1","Option 2","Option 3"]},
   "confidence":{"type":"number","minimum":0,"maximum":1},
   "reason":{"type":"string"}
 },
 "required":["choice","confidence","reason"],
 "additionalProperties":False
}
OUT=Path("receipts/evonomos_p5")
OUT.mkdir(parents=True,exist_ok=True)

def fetch(rel):
    url=f"https://raw.githubusercontent.com/WhoSia/EvoNOMOS/{SCIENCE_SHA}/{rel}"
    req=urllib.request.Request(url,headers={"User-Agent":"EvoNOMOS-P5-host"})
    with urllib.request.urlopen(req,timeout=60) as r:
        return r.read()

def load_renderer():
    p=Path(tempfile.gettempdir())/"law_r1_p5_render.py"
    p.write_bytes(fetch("tools/law-r1-p5-render.py"))
    spec=importlib.util.spec_from_file_location("p5render",p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def parse(text):
    t=(text or "").strip()
    t=re.sub(r"^\s*<think>.*?</think>\s*","",t,flags=re.S)
    try:o=json.loads(t)
    except Exception:
        i=t.find("{")
        if i<0:raise
        o,_=json.JSONDecoder().raw_decode(t[i:])
    if set(o)!={"choice","confidence","reason"}: raise ValueError("exact-schema")
    if o["choice"] not in {"Option 1","Option 2","Option 3"}: raise ValueError("choice")
    o["confidence"]=float(o["confidence"])
    if not 0<=o["confidence"]<=1:raise ValueError("confidence")
    o["reason"]=str(o["reason"])
    return o

def groq_call(client,model,prompt,contract):
    kw={"model":model,"messages":[{"role":"user","content":prompt}],"temperature":0,"top_p":1,
        "max_completion_tokens":384,"stream":False}
    if contract.get("reasoning"):
        kw["reasoning_effort"]=contract["reasoning"];kw["reasoning_format"]="hidden"
    if contract["format"]=="schema":
        kw["response_format"]={"type":"json_schema","json_schema":{"name":"evonomos_p5","strict":True,"schema":SCHEMA}}
    elif contract["format"]=="object":
        kw["response_format"]={"type":"json_object"}
    return client.chat.completions.create(**kw).choices[0].message.content or ""

def calibrate_groq(model):
    client=Groq(api_key=os.environ["GROQ_API_KEY"],max_retries=4)
    canary='Return exactly this JSON object and nothing else: {"choice":"Option 2","confidence":0.5,"reason":"canary"}'
    candidates=[
      {"name":"schema_hidden_low","format":"schema","reasoning":"low"},
      {"name":"object_hidden_low","format":"object","reasoning":"low"},
      {"name":"object_plain","format":"object","reasoning":None},
      {"name":"plain","format":"plain","reasoning":None},
    ]
    audit=[]
    for c in candidates:
        ok=0;errors=[]
        for _ in range(2):
            try:
                o=parse(groq_call(client,model,canary,c))
                good=(o["choice"]=="Option 2" and abs(o["confidence"]-0.5)<1e-9 and o["reason"]=="canary")
                ok+=int(good)
                if not good:errors.append("value-mismatch")
            except Exception as e:errors.append(type(e).__name__+":"+str(e)[:180])
        audit.append({"contract":c,"ok":ok,"errors":errors})
        if ok==2:return c,audit
    return None,audit

def gemini_call(client,model,prompt):
    cfg=types.GenerateContentConfig(
      temperature=0,top_p=1,max_output_tokens=256,seed=5517,
      response_mime_type="application/json",response_json_schema=SCHEMA
    )
    return client.models.generate_content(model=model,contents=prompt,config=cfg).text or ""

def calibrate_gemini(model):
    client=genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    canary='Return exactly this JSON object and nothing else: {"choice":"Option 2","confidence":0.5,"reason":"canary"}'
    errors=[];ok=0
    for _ in range(2):
        try:
            o=parse(gemini_call(client,model,canary))
            good=(o["choice"]=="Option 2" and abs(o["confidence"]-0.5)<1e-9 and o["reason"]=="canary")
            ok+=int(good)
            if not good:errors.append("value-mismatch")
        except Exception as e:errors.append(type(e).__name__+":"+str(e)[:180])
    return ({"name":"gemini_schema_seed5517","format":"schema","reasoning":None} if ok==2 else None),[{"contract":"gemini_schema_seed5517","ok":ok,"errors":errors}]

def main():
    renderer=load_renderer()
    corpus=json.loads(fetch("lawkit/fixtures/law-r1-p5-blinded-design-contexts.json"))
    prompts=[]
    for case in corpus["cases"]:
        for arm in renderer.ARMS:
            for rep in range(3):
                prompt,mapping=renderer.render(case,arm,rep)
                prompts.append({
                  "case_id":case["id"],"family":case["family"],"cell":case["cell"],"arm":arm,"replicate":rep,
                  "principle_prime":case["principle_prime"],"precommitted":case["precommitted"],
                  "principle_congruent":case["principle_congruent"],"option_to_semantic":mapping,"prompt":prompt
                })
    packet={"schema_version":"law-r1-p5-prompt-packet-v1","replicates":3,"rows":prompts}
    (OUT/"prompt_packet.json").write_text(json.dumps(packet,indent=2,sort_keys=True),encoding="utf-8")
    scorer=OUT/"law-r1-p5-score.py";scorer.write_bytes(fetch("tools/law-r1-p5-score.py"))

    contracts={};audits={}
    for k,cfg in MODELS.items():
        contract,audit=(calibrate_groq(cfg["model"]) if cfg["provider"]=="groq" else calibrate_gemini(cfg["model"]))
        contracts[k]=contract;audits[k]=audit
    (OUT/"contract_calibration.json").write_text(json.dumps({"contracts":contracts,"audits":audits},indent=2),encoding="utf-8")
    if any(v is None for v in contracts.values()):
        raise RuntimeError("response-contract calibration failed")

    all_scores={}
    for key,cfg in MODELS.items():
        rows=[];client=None
        if cfg["provider"]=="groq":client=Groq(api_key=os.environ["GROQ_API_KEY"],max_retries=4)
        else:client=genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        for idx,p in enumerate(prompts,1):
            retry=False;status="OK";err=None
            try:
                raw=groq_call(client,cfg["model"],p["prompt"],contracts[key]) if cfg["provider"]=="groq" else gemini_call(client,cfg["model"],p["prompt"])
                try:o=parse(raw)
                except Exception:
                    retry=True
                    repair=p["prompt"]+"\nYour previous response was not parseable. Return only the requested JSON object."
                    raw=groq_call(client,cfg["model"],repair,contracts[key]) if cfg["provider"]=="groq" else gemini_call(client,cfg["model"],repair)
                    o=parse(raw)
            except Exception as e:
                status="TECHNICAL_FAIL";err=type(e).__name__+":"+str(e)[:240];o=None
            rows.append({"case_id":p["case_id"],"arm":p["arm"],"replicate":p["replicate"],"response":o,"format_retry":retry,"status":status,"error":err})
            if idx%18==0:print(json.dumps({"model":key,"progress":idx,"total":len(prompts)}),flush=True)
            if cfg["provider"]=="groq":time.sleep(0.05)
        if any(r["status"]!="OK" for r in rows):
            raise RuntimeError(f"{key} technical failures: "+str([r for r in rows if r["status"]!="OK"][:3]))
        response={
          "schema_version":"law-r1-p5-model-responses-v1",
          "model":cfg["model"],
          "run_metadata":{"host_repo":"WhoSia/EvoNOMOS","science_sha":SCIENCE_SHA,"provider":cfg["provider"],"contract":contracts[key],"replicates":3},
          "rows":rows
        }
        rp=OUT/f"responses_{key}.json";rp.write_text(json.dumps(response,indent=2,sort_keys=True),encoding="utf-8")
        sp=OUT/f"score_{key}.json"
        subprocess.run([sys.executable,str(scorer),"--packet",str(OUT/"prompt_packet.json"),"--responses",str(rp),"--out",str(sp)],check=True)
        all_scores[key]=json.loads(sp.read_text())
    result={
      "stage":"EvoNOMOS Generation VIII LAW-R1-P5",
      "execution_host":STAGE,
      "science_sha":SCIENCE_SHA,
      "models":MODELS,
      "contracts":contracts,
      "scores":all_scores,
      "authority":"THREE_INTERFACE_DESCRIPTIVE_PILOT_ONLY",
      "population_llm_claim":False,
      "solid_verdict":"WITHHELD"
    }
    (OUT/"p5_host_result.json").write_text(json.dumps(result,indent=2,sort_keys=True),encoding="utf-8")
    print("EVONOMOS_P5_HOST=PASS")
    print(json.dumps({k:{"pilot":v["pilot_classification"],"contrasts":v["descriptive_contrasts"],"summary":v["summary"]} for k,v in all_scores.items()},sort_keys=True),flush=True)

if __name__=="__main__":
    main()
