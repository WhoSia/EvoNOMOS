from pathlib import Path
from itertools import product
import json,subprocess,difflib,hashlib
R=Path(__file__).resolve().parent
variants=[]
for architecture,swap,mode in product(('direct','port','direct_refactored'),(False,True),(False,True)):
    name=f'{architecture}_{"replacement" if swap else "base"}_{"mode" if mode else "nomode"}'
    p=R/'snapshots'/name;p.mkdir(parents=True,exist_ok=True)
    (p/'go.mod').write_text('module evonomos/pilot\n\ngo 1.23\n')
    ver='v2' if swap else 'v1'
    if architecture=='direct':
        methods='''package pilot
func Legacy() string { return "old" }
func Lookup(id string) string { return "VERSION:" + id }
func Label(id string) string { return "label[VERSION:" + id + "]" }
func Describe(id string) string { return "desc(VERSION:" + id + ")" }
'''.replace('VERSION',ver)
        if mode:methods+=f'func Mode() string {{ return "{ver}" }}\n'
        (p/'service.go').write_text(methods)
    elif architecture=='direct_refactored':
        code=f'''package pilot
func Legacy() string {{ return "old" }}
func lookupInternal(id string) string {{ return "{ver}:" + id }}
func Lookup(id string) string {{ return lookupInternal(id) }}
func Label(id string) string {{ return "label[" + lookupInternal(id) + "]" }}
func Describe(id string) string {{ return "desc(" + lookupInternal(id) + ")" }}
'''
        if mode:code+=f'func Mode() string {{ return "{ver}" }}\n'
        (p/'service.go').write_text(code)
    else:
        (p/'service.go').write_text('''package pilot
func Legacy() string { return "old" }
func Lookup(id string) string { return active.Lookup(id) }
func Label(id string) string { return "label[" + active.Lookup(id) + "]" }
func Describe(id string) string { return "desc(" + active.Lookup(id) + ")" }
'''+('func Mode() string { return active.Mode() }\n' if mode else ''))
        (p/'contract.go').write_text('''package pilot
type Backend interface {
  Lookup(string) string
'''+('  Mode() string\n' if mode else '')+'}\nvar active Backend = backend{}\n')
        (p/'backend.go').write_text(f'''package pilot
type backend struct{{}}
func (backend) Lookup(id string) string {{ return "{ver}:" + id }}
'''+(f'func (backend) Mode() string {{ return "{ver}" }}\n' if mode else ''))
    tests=f'''package pilot
import "testing"
func TestLegacyContract(t *testing.T) {{ if x:=Legacy(); x!="old" {{ t.Fatalf("old client changed: %q",x) }} }}
func TestFeature(t *testing.T) {{
  if x:=Lookup("x");x!="{ver}:x" {{t.Errorf("lookup %q",x)}}
  if x:=Label("x");x!="label[{ver}:x]" {{t.Errorf("label %q",x)}}
  if x:=Describe("x");x!="desc({ver}:x)" {{t.Errorf("describe %q",x)}}
}}
'''
    if mode:tests+=f'func TestModeRequirement(t *testing.T) {{if x:=Mode();x!="{ver}" {{t.Fatal(x)}}}}\n'
    (p/'service_test.go').write_text(tests)
    variants.append({'name':name,'architecture':architecture,'replacement':swap,'mode':mode})
(R/'preseal.json').write_text(json.dumps({'date':'2026-11-09','class':'researcher-generated controlled source fixture (not independent upstream)','scope':'initial 8 snapshots; four direct_refactored snapshots added POST-HOC as a stronger rival after first results','prediction':'replacement: direct changes three repeated provider literals vs port one; adding backend-derived Mode: direct adds one service method vs port changes service, interface, and backend; legacy client always passes','limitations':'no independent rights, human effort, prospective demand, semantic equivalence for all clients, or new theorem; direct_refactored rival was introduced after observing original 8 results; original preseal must be separately preserved'},indent=2))
(R/'variants.json').write_text(json.dumps(variants,indent=2))
