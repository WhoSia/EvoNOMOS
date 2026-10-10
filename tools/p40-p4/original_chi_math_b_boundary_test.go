package p40p4

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "strings"
 "testing"

 "github.com/go-chi/chi/v5"
)

// These are NEW integration checks against the unmodified, pinned go-chi source.
// Never treat synthetic owner permissions as genuine project maintainer authority.
func TestP40MathBIndependentTreeIdentityIsNecessary(t *testing.T) {
  pattern := "/service/unique"
  freshParent := originalParent()
  freshChild := mountRoot("FRESH")
  var freshPanic any
  func() {
    defer func(){ freshPanic=recover() }()
    freshParent.Mount(pattern, freshChild)
  }()
  if freshPanic != nil { t.Fatalf("fresh tree rejected: %v", freshPanic) }
  request(t,freshParent,"/old","unchanged")
  request(t,freshParent,pattern+"/item","FRESH:item")

  aliasParent := originalParent()
  // With returns chi.Router and shares the underlying routing tree with its parent.
  inlineAlias := aliasParent.With(func(next http.Handler) http.Handler{return next})
  var aliasPanic any
  func() {
    defer func(){ aliasPanic=recover() }()
    aliasParent.Mount(pattern,inlineAlias)
  }()
  if aliasPanic == nil || !strings.Contains(fmt.Sprint(aliasPanic),
      "attempting to Mount() a router onto itself") {
    t.Fatalf("expected tree-identity alias guard, got: %#v",aliasPanic)
  }
  request(t,aliasParent,"/old","unchanged")
  t.Log("P40_MATH_B_ORIGINAL_CHI_NAMESPACE_EQUAL_INTERFACE_ALIAS_DIVERGENCE_PASS")
}

func TestP40MathBIndependentNamespaceAndOrderGuardCourts(t *testing.T) {
  const p = "/service/new"
  r := originalParent()
  r.Mount(p,mountRoot("A"))
  request(t,r,p+"/item","A:item")
  var conflict any
  func() {
    defer func(){ conflict=recover() }()
    r.Mount(p,mountRoot("B"))
  }()
  if conflict==nil || !strings.Contains(fmt.Sprint(conflict),
      "attempting to Mount() a handler on an existing path") {
    t.Fatalf("expected duplicate route despite fresh child tree: %v",conflict)
  }

  wrongOrder:=originalParent() // /old route already registered
  var late any
  func() {
    defer func(){ late=recover() }()
    wrongOrder.Use(func(next http.Handler) http.Handler{return next})
  }()
  if late==nil || !strings.Contains(fmt.Sprint(late),
      "all middlewares must be defined before routes on a mux") {
    t.Fatalf("expected order guard although no duplicate mount: %v", late)
  }
  correct:=chi.NewRouter()
  correct.Use(func(next http.Handler) http.Handler{return next})
  correct.Get("/old",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"unchanged")})
  correct.Mount(p,mountRoot("A"))
  request(t,correct,"/old","unchanged")
  request(t,correct,p+"/item","A:item")
  t.Log("P40_MATH_B_ORIGINAL_CHI_THREE_INDEPENDENT_BOUNDARY_GUARDS_PASS")
}

func TestP40MathBSourceRoutePatternProbe(t *testing.T) {
 // Exploratory: differing textual parameters need not identify independent routes.
 cases:=[]struct{ a,b,reqA,reqB string }{
  {"/service/{first}", "/service/{second}","/service/abc/item","/service/abc/item"},
  {"/service/{number:[0-9]+}", "/service/{letter:[a-z]+}","/service/123/item","/service/abc/item"},
 }
 for i,c:=range cases {
  r:=originalParent()
  r.Mount(c.a,mountRoot("A"))
  var got any
  func(){
   defer func(){ got=recover() }()
   r.Mount(c.b,mountRoot("B"))
  }()
  if got!=nil {
   t.Logf("P40_MATH_B_ORIGINAL_CHI_PATTERN_PROBE_%d blocked=%v",i,got)
   continue
  }
  // Do not judge only from successful registration: observe both clients.
  read:=func(path string)(int,string){
   w:=httptest.NewRecorder()
   req:=httptest.NewRequest(http.MethodGet,path,nil)
   r.ServeHTTP(w,req)
   return w.Code, strings.TrimSpace(w.Body.String())
  }
  codeA,bodyA:=read(c.reqA)
  codeB,bodyB:=read(c.reqB)
  t.Logf("P40_MATH_B_ORIGINAL_CHI_PATTERN_PROBE_%d registered codeA=%d bodyA=%q codeB=%d bodyB=%q",i,codeA,bodyA,codeB,bodyB)
 }
}

func TestP40MathBRegexDisjointnessStillDoesNotGuaranteeRegistration(t *testing.T) {
  digitPattern := "/service/{number:[0-9]+}"
  alphaPattern := "/service/{letter:[a-z]+}"
  checkSingleton := func(pattern, path, label string) {
    t.Helper()
    r := originalParent()
    r.Mount(pattern, mountRoot(label))
    request(t,r,"/old","unchanged")
    request(t,r,path+"/item",label+":item")
  }
  // The request languages [0-9]+ and [a-z]+ do not intersect.
  checkSingleton(digitPattern,"/service/123","NUM")
  checkSingleton(alphaPattern,"/service/abc","ALPHA")
  for _,patterns:=range [][2]string{
    {digitPattern,alphaPattern},{alphaPattern,digitPattern},
  } {
    r:=originalParent()
    r.Mount(patterns[0],mountRoot("FIRST"))
    var conflict any
    func(){
      defer func(){conflict=recover()}()
      r.Mount(patterns[1],mountRoot("SECOND"))
    }()
    if conflict==nil || !strings.Contains(fmt.Sprint(conflict),
      "attempting to Mount() a handler on an existing path") {
      t.Fatalf("expected conservative structural route rejection: %#v",conflict)
    }
    request(t,r,"/old","unchanged")
  }
  t.Log("P40_MATH_B_ORIGINAL_CHI_DISJOINT_REGEX_SINGLETONS_GLOBAL_REJECTION_BOTH_ORDERS_PASS")
}

func TestP40MathBP3MethodSplitDoesNotRepairChiMountReservation(t *testing.T) {
  digitPattern:="/service/{number:[0-9]+}"
  alphaPattern:="/service/{letter:[a-z]+}"
  digitChild:=func()chi.Router{
    r:=chi.NewRouter()
    r.Get("/item",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"NUM")})
    return r
  }
  alphaChild:=func()chi.Router{
    r:=chi.NewRouter()
    r.Post("/item",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"ALPHA")})
    return r
  }
  loneN:=originalParent()
  loneN.Mount(digitPattern,digitChild())
  request(t,loneN,"/old","unchanged")
  request(t,loneN,"/service/123/item","NUM")
  loneA:=originalParent()
  loneA.Mount(alphaPattern,alphaChild())
  request(t,loneA,"/old","unchanged")
  post:=httptest.NewRecorder()
  loneA.ServeHTTP(post,httptest.NewRequest(http.MethodPost,"/service/abc/item",nil))
  if post.Code!=200 || strings.TrimSpace(post.Body.String())!="ALPHA" {
    t.Fatalf("standalone POST child invalid: (%d,%q)",post.Code,post.Body.String())
  }
  for i,flip:=range []bool{false,true}{
    parent:=originalParent()
    if !flip{parent.Mount(digitPattern,digitChild())}else{parent.Mount(alphaPattern,alphaChild())}
    var recovered any
    func(){
      defer func(){recovered=recover()}()
      if !flip{parent.Mount(alphaPattern,alphaChild())}else{parent.Mount(digitPattern,digitChild())}
    }()
    if recovered==nil || !strings.Contains(fmt.Sprint(recovered),
      "attempting to Mount() a handler on an existing path") {
      t.Fatalf("chi method split order %d should not bypass Mount's source reservation: %v",i,recovered)
    }
    request(t,parent,"/old","unchanged")
  }
  t.Log("P40_MATH_B_P3_CHI_METHOD_SPLIT_DOES_NOT_REPAIR_MOUNT_RESERVATION_PASS")
}
