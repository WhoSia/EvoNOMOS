package middleware

import (
  "fmt"
  "net/http"
  "net/http/httptest"
  "strings"
  "testing"
)

// MATH-2B independent, intentionally small reference semantics.
// DO NOT call the treatment's Pattern.Match, p35P7MatchStrength or
// p35Math2BestMatch. The only matching grammar here is literal, p*, *g.
type math2bRule struct {
 header string
 patterns []string
 label string
}
type math2bConfig struct {
 name string
 rules []math2bRule
}
var math2bConfigs = []math2bConfig{
 {"a-wild-b-exact",[]math2bRule{{"X-A",[]string{"p*"},"aWild"},{"X-B",[]string{"ping"},"bExact"}}},
 {"a-exact-b-wild",[]math2bRule{{"X-A",[]string{"ping"},"aExact"},{"X-B",[]string{"p*"},"bWild"}}},
 {"a-wild-then-exact",[]math2bRule{{"X-A",[]string{"p*"},"aFirst"},{"X-A",[]string{"ping"},"aLater"},{"X-B",[]string{"p*"},"bWild"}}},
 {"a-any-b-wild",[]math2bRule{{"X-A",[]string{"p*","ping"},"aAny"},{"X-B",[]string{"p*"},"bWild"}}},
 {"both-wild-tie",[]math2bRule{{"X-A",[]string{"*g"},"aSuffix"},{"X-B",[]string{"p*"},"bPrefix"}}},
}
var math2bFieldArrangements = [][]string{
 nil, {"none"}, {"ping"}, {"pong"}, {"miss","ping"},
 {"miss,ping"}, {" ping , pong "}, {"polo, miss"},
 {"","ping"}, {" , , "}, {"pong","ping"}, {"miss, pong"},
}

func math2bPatternStrength(pattern,value string) int {
 switch pattern {
 case "ping":
  if value=="ping" {return 2}
 case "p*":
  if strings.HasPrefix(value,"p") {return 1}
 case "*g":
  if strings.HasSuffix(value,"g") {return 1}
 default:
  panic("MATH2B_REFERENCE_UNEXPECTED_PATTERN")
 }
 return 0
}

func math2bRuleStrength(rule math2bRule, physical []string) int {
 best:=0
 for _,raw:=range physical {
  for _,piece:=range strings.Split(raw,",") {
   token:=strings.ToLower(strings.TrimSpace(piece))
   if len(token)==0 {continue}
   for _,pattern:=range rule.patterns {
    if s:=math2bPatternStrength(pattern,token);s>best {best=s}
   }
  }
 }
 return best
}

// Reference first selects the earliest matching registration FOR EACH KEY,
// then compares first-hit strengths across different keys; ties lexical.
func math2bExpected(config math2bConfig, a,b []string)string {
 best:=0
 winner:="fallback"
 for _,key:=range []string{"X-A","X-B"} {
  values:=a
  if key=="X-B" {values=b}
  for _,rule:=range config.rules {
   if rule.header!=key {continue}
   strength:=math2bRuleStrength(rule,values)
   if strength==0 {continue}
   if strength>best {best=strength;winner=rule.label}
   break
  }
 }
 return winner
}

func math2bHandler(config math2bConfig)http.Handler {
 r:=RouteHeaders()
 for _,rule:=range config.rules {
  label:=rule.label
  if len(rule.patterns)==1 {
   r.Route(rule.header,rule.patterns[0],p35tag(label))
  } else {
   r.RouteAny(rule.header,rule.patterns,p35tag(label))
  }
 }
 r.RouteDefault(p35tag("fallback"))
 next:=http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if w.Header().Get("X-P35-P7")=="" {w.Header().Set("X-P35-P7","next")}
 })
 return r.Handler(next)
}
func math2bActual(h http.Handler,a,b []string)string {
 r:=httptest.NewRequest("GET","/",nil)
 for _,v:=range a {r.Header.Add("X-A",v)}
 for _,v:=range b {r.Header.Add("X-B",v)}
 w:=httptest.NewRecorder()
 h.ServeHTTP(w,r)
 return w.Header().Get("X-P35-P7")
}

func TestP35Math2BIndependentReferenceGrid(t *testing.T){
 cases:=0
 for _,config:=range math2bConfigs {
  h:=math2bHandler(config)
  for i,a:=range math2bFieldArrangements {
   for j,b:=range math2bFieldArrangements {
    expected:=math2bExpected(config,a,b)
    got:=math2bActual(h,a,b)
    cases++
    if got!=expected{
     t.Fatalf("MATH2B_DIFFERENTIAL_COUNTEREXAMPLE config=%s a-index=%d b-index=%d a=%q b=%q expected=%q actual=%q",
       config.name,i,j,a,b,expected,got)
    }
   }
  }
  // Split field lists and comma-lists must coincide for this bounded grammar.
  m1:=math2bActual(h,[]string{"miss","ping"},[]string{"pong"})
  m2:=math2bActual(h,[]string{"miss,ping"},[]string{"pong"})
  if m1!=m2{t.Fatalf("MATH2B_METAMORPHIC_FAILURE config=%s repeated=%q comma=%q",config.name,m1,m2)}
 }
 if cases!=720 {t.Fatalf("MATH2B_WRONG_CENSUS %d",cases)}
 t.Logf("MATH2B_INDEPENDENT_REFERENCE_GRID_PASS cases=%d",cases)
}
