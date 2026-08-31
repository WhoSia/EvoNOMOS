#!/usr/bin/env python3
# Final pre-outcome evaluator wrapper. The core harness was already sealed; this
# overrides only P1 to compare phase-0 vs phase-1 pre-existing consumer loci,
# exactly as preregistered in issue #11.
import sys, shutil, tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import run_wc5 as m

def trajectory(base_dir,anchor,rep,policy,regime):
    tid=f"{anchor}-r{rep}-{policy}-{regime}"
    work=Path(tempfile.mkdtemp(prefix="wc5_")); shutil.copytree(base_dir,work/"repo",dirs_exist_ok=True); root=work/"repo"
    rec={"id":tid,"anchor":anchor,"replicate":rep,"policy":policy,"regime":regime,"status":"HOLD"}
    try:
        p0=m.build_prompt(anchor,policy,0,m.extract_packet(root,anchor)); msgs0=m.messages_for(regime,p0)
        t0,u0,_=m.groq(msgs0); b0,a0,c0=m.parse_and_apply(root,t0,anchor,policy); m.validate(root,anchor,0)
        phase0_cons=[m.norm(x) for x in m.consumer_blocks(root,anchor)]
        p1=m.build_prompt(anchor,policy,1,m.extract_packet(root,anchor)); prior=[{"role":"user","content":p0},{"role":"assistant","content":t0}]
        t1,u1,_=m.groq(m.messages_for(regime,p1,prior)); b1,a1,c1=m.parse_and_apply(root,t1,anchor,policy); m.validate(root,anchor,1)
        final_cons=[m.norm(x) for x in m.consumer_blocks(root,anchor)]
        P1=sum(1 for x,y in zip(phase0_cons,final_cons) if x!=y)
        V=[len(c0),sum(m.churn(b0[f],a0[f]) for f in c0),len(c1),sum(m.churn(b1[f],a1[f]) for f in c1),P1]
        rec.update(status="PASS",V=V,phase0_files=c0,phase1_files=c1,usage0=u0,usage1=u1,output0=t0,output1=t1)
    except Exception as e:
        rec["error"]=str(e)[:1500]
    finally:
        shutil.rmtree(work,ignore_errors=True)
    return rec

m.trajectory=trajectory
m.main()
