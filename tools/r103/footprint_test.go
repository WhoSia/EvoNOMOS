package footprint
import("testing";"strings")
// Extracted Pattern semantics from both historical arms. Not full router.
type Pattern struct {prefix,suffix string; wildcard bool}
func NewPattern(value string) Pattern {p:=Pattern{};if i:=strings.IndexByte(value,'*');i>=0 {p.wildcard=true;p.prefix=value[:i];p.suffix=value[i+1:]}else{p.prefix=value};return p}
func(p Pattern) Match(v string)bool{if !p.wildcard{return p.prefix==v};return len(v)>=len(p.prefix+p.suffix)&&strings.HasPrefix(v,p.prefix)&&strings.HasSuffix(v,p.suffix)}
func run(op int, route bool,p,v string)bool{if route{v=strings.ToLower(v)};if op==1||op==2&&route{p=strings.ToLower(p)};x:=NewPattern(p);if op==3{x.prefix=strings.ToLower(x.prefix);x.suffix=strings.ToLower(x.suffix)};return x.Match(v)}
func TestFootprint(t *testing.T){patterns:=[]string{"Gold","Go*","*OlD","A*B","*","","İ","K*"};inputs:=[]string{"Gold","gold","GOLD","xxOlD","xxold","AxxB","axxB","","i","kilo","KILO"};for op:=1;op<=3;op++{direct,route:=0,0;for _,p:=range patterns{for _,v:=range inputs{if run(op,false,p,v)!=run(0,false,p,v){direct++};if run(op,true,p,v)!=run(0,true,p,v){route++}}};t.Logf("op=%d direct=%d route=%d pairs=%d",op,direct,route,len(patterns)*len(inputs));if op==2&&direct!=0{t.Fatal("local changed direct")};if op!=2&&direct==0{t.Fatal("missing shared witness")}}}
