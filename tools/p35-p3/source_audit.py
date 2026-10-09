#!/usr/bin/env python3
"""P35-P3: Go AST normalized method edit supports; bounded strongest alternatives.
All rival sets are task-informed; B2 is RETROSPECTIVE/CONDITIONAL, never a prospective win.
"""
import hashlib, json, difflib, pathlib, subprocess, sys
root=pathlib.Path(__file__).resolve().parents[2]
ast=pathlib.Path(sys.argv[1]).resolve()
targets={'U2':root/'tools/p35-p1/worlds/u-encoded',
         'C5':root/'tools/p35-p1/worlds/c-encoded-tagged',
         'C4_frozen':root/'tools/p35-p3/c-encoded-four-decoder'}
base=root/'tools/p35-p1/worlds/baseline'
def fp(path):
 return json.loads(subprocess.check_output([str(ast),str(path/'backend.go')],text=True))
b=fp(base)
out={'provenance':{'original_restic_commit':'495982232cf1af184eac0a97871ef8161e8708ee',
 'baseline_p0_git_blob':'d15f47c3511c0a1dad1d8cb6793db59a19860066'},
 'method_hash':'gofmt normalized Go AST declarations, not raw text whitespace',
 'source_worlds':{},'rivals':{},
 'B1_history':'NO FAIR TRAINING SAMPLE: synthetic P35 methods have only P0 creation commit before demand; upstream Restic cochange is not same treatment population.',
 'B2_note':'Conditional marker ownership and information hiding/lifecycle explanation, retrospectively specified after observing outcome; this is not prospective generalization.'}
for name,path in targets.items():
 f=fp(path)
 change=sorted(k.removeprefix('func:') for k in b if k.startswith('func:') and f.get(k)!=b[k])
 kinds=sorted(k.removeprefix('type:') for k in b if k.startswith('type:') and f.get(k)!=b[k])
 orig=(base/'backend.go').read_text().splitlines(True)
 new=(path/'backend.go').read_text().splitlines(True)
 dif=list(difflib.unified_diff(orig,new))
 add=sum(x.startswith('+') and not x.startswith('+++') for x in dif)
 rem=sum(x.startswith('-') and not x.startswith('---') for x in dif)
 codec=len((path/'codec.go').read_text().splitlines())
 out['source_worlds'][name]={'modified_existing_methods':change,'method_count':len(change),'modified_types':kinds,
 'source_added_lines_including_new_codec':add+codec,'source_removed_lines':rem,
 'go_source_sha256':hashlib.sha256((path/'backend.go').read_bytes()).hexdigest()}
assert out['source_worlds']['U2']['method_count']==2
assert out['source_worlds']['C5']['method_count']==5
a=set(out['source_worlds']['C4_frozen']['modified_existing_methods'])
assert a=={'payloadStore.put','payloadStore.erase','payloadStore.clear','readEngine.decode'},a
b0=set('composed.Delete composed.Load composed.Remove composed.Save newPayloadStore payloadStore.clear payloadStore.erase payloadStore.get payloadStore.put readEngine.decode removalCoordinator.clear removalCoordinator.erase'.split())
b0plus=set('newPayloadStore payloadStore.clear payloadStore.erase payloadStore.get payloadStore.put readEngine.decode'.split())
b2=set('payloadStore.put payloadStore.erase payloadStore.clear readEngine.decode'.split())
for name,sel in [('B0_task_aware_syntactic',b0),('B0plus_field_owner',b0plus),('B2_conditional_information_hiding',b2)]:
 out['rivals'][name]={'candidates':sorted(sel),'observed':sorted(a),
 'precision':len(sel&a)/len(sel),'recall':len(sel&a)/len(a),
 'exact':sel==a,'prediction_status':'POST_HOC_EXPLANATORY' if name.startswith('B2') else 'CONSERVATIVE_CANDIDATE_SET'}
out['verdict']='C4_FIXED_READER_EXECUTABLE_CANDIDATE__U2_VS_C5_NOT_STABLE__NO_GLOBAL_MINIMUM__NO_STRONG_RIVAL_DEFEAT'
print(json.dumps(out,indent=2,ensure_ascii=False))
