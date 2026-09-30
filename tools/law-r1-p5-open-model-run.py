#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, os, re, tempfile, urllib.request
from pathlib import Path

def fetch(url:str)->bytes:
    req=urllib.request.Request(url,headers={"User-Agent":"EvoNOMOS-LAW-R1-P5"})
    with urllib.request.urlopen(req,timeout=60) as r:
        return r.read()

def load_renderer(repo_sha:str):
    url=f"https://raw.githubusercontent.com/WhoSia/EvoNOMOS/{repo_sha}/tools/law-r1-p5-render.py"
    data=fetch(url)
    p=Path(tempfile.gettempdir())/"law_r1_p5_render.py"
    p.write_bytes(data)
    spec=importlib.util.spec_from_file_location("p5render",p)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def extract_json(s:str):
    s=s.strip()
    s=re.sub(r"^\s*<think>.*?</think>\s*","",s,flags=re.S)
    try:
        return json.loads(s)
    except Exception:
        pass
    m=re.search(r'\{\s*"choice"\s*:\s*"Option [123]".*?\}',s,re.S)
    if not m:
        raise ValueError("no choice JSON object")
    return json.loads(m.group(0))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model",required=True)
    ap.add_argument("--repo-sha",required=True)
    ap.add_argument("--replicates",type=int,default=3)
    ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args()

    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch

    renderer=load_renderer(a.repo_sha)
    corpus=json.loads(fetch(f"https://raw.githubusercontent.com/WhoSia/EvoNOMOS/{a.repo_sha}/lawkit/fixtures/law-r1-p5-blinded-design-contexts.json"))
    tokenizer=AutoTokenizer.from_pretrained(a.model,trust_remote_code=True)
    model=AutoModelForCausalLM.from_pretrained(
        a.model,device_map="auto",torch_dtype="auto",trust_remote_code=True
    )
    model.eval()
    rows=[]
    for case in corpus["cases"]:
        for arm in renderer.ARMS:
            for rep in range(a.replicates):
                prompt,mapping=renderer.render(case,arm,rep)
                messages=[{"role":"user","content":prompt}]
                kwargs={"tokenize":False,"add_generation_prompt":True}
                try:
                    text=tokenizer.apply_chat_template(messages,enable_thinking=False,**kwargs)
                except TypeError:
                    text=tokenizer.apply_chat_template(messages,**kwargs)
                inputs=tokenizer(text,return_tensors="pt").to(model.device)
                with torch.inference_mode():
                    out=model.generate(
                        **inputs,max_new_tokens=96,do_sample=False,
                        pad_token_id=tokenizer.eos_token_id
                    )
                generated=tokenizer.decode(out[0][inputs["input_ids"].shape[1]:],skip_special_tokens=True)
                retry=False
                try:
                    obj=extract_json(generated)
                except Exception:
                    retry=True
                    repair=prompt+"\nYour previous response was not parseable. Return only the requested JSON object."
                    messages=[{"role":"user","content":repair}]
                    try:
                        text=tokenizer.apply_chat_template(messages,enable_thinking=False,**kwargs)
                    except TypeError:
                        text=tokenizer.apply_chat_template(messages,**kwargs)
                    inputs=tokenizer(text,return_tensors="pt").to(model.device)
                    with torch.inference_mode():
                        out=model.generate(**inputs,max_new_tokens=64,do_sample=False,pad_token_id=tokenizer.eos_token_id)
                    generated=tokenizer.decode(out[0][inputs["input_ids"].shape[1]:],skip_special_tokens=True)
                    obj=extract_json(generated)
                rows.append({
                    "case_id":case["id"],"arm":arm,"replicate":rep,
                    "response":obj,"format_retry":retry
                })
                print(json.dumps({"progress":len(rows),"case":case["id"],"arm":arm,"rep":rep,"choice":obj.get("choice")}),flush=True)
    payload={
      "schema_version":"law-r1-p5-model-responses-v1",
      "model":a.model,
      "run_metadata":{"repo_sha":a.repo_sha,"replicates":a.replicates,"decode":"greedy","max_new_tokens":96,"format_retry_max":1},
      "rows":rows
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(payload,sort_keys=True)+"\n")
    print("LAW_R1_P5_RESPONSES_B64="+__import__("base64").b64encode(a.out.read_bytes()).decode(),flush=True)

if __name__=="__main__":
    main()
