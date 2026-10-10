package p40mathbp3

import (
    "fmt"
    "net/http"
    "net/http/httptest"
    "strings"
    "testing"
    router "github.com/julienschmidt/httprouter"
)

const pinnedOriginalHttprouterCommit = "484018016424d215c0b87c42f4c9b57d980fbd00"

type registration struct {
    method string
    pattern string
    response string
}
func makeHandler(response string) router.Handle {
    return func(w http.ResponseWriter, req *http.Request, p router.Params) {
        fmt.Fprint(w, response)
    }
}
func originalParent() *router.Router {
    r:=router.New()
    r.GET("/old",makeHandler("unchanged"))
    return r
}
func register(r *router.Router, e registration) {
    r.Handle(e.method,e.pattern,makeHandler(e.response))
}
func assertResponse(t *testing.T, r *router.Router, method,path,want string) {
    t.Helper()
    w:=httptest.NewRecorder()
    request:=httptest.NewRequest(method,path,nil)
    r.ServeHTTP(w,request)
    if w.Code!=200 || strings.TrimSpace(w.Body.String())!=want {
        t.Fatalf("%s %s got (%d, %q), expected (200,%q)",method,path,w.Code,w.Body.String(),want)
    }
}
func tryRegister(r *router.Router, e registration)(panicValue any){
    defer func(){panicValue=recover()}()
    register(r,e)
    return nil
}
func TestOriginalHttprouterDisjointRequestLanguagesButSameMethodRegistrationConflicts(t *testing.T){
    // A has suffix /a; B has suffix /b. They cannot match the same request.
    a:=registration{method:"GET", pattern:"/service/:name/a",response:"A"}
    b:=registration{method:"GET", pattern:"/service/static/b",response:"B"}
    oneA:=originalParent();register(oneA,a)
    assertResponse(t,oneA,"GET","/old","unchanged")
    assertResponse(t,oneA,"GET","/service/example/a","A")
    oneB:=originalParent();register(oneB,b)
    assertResponse(t,oneB,"GET","/old","unchanged")
    assertResponse(t,oneB,"GET","/service/static/b","B")
    for i,edits:=range [][2]registration{{a,b},{b,a}}{
        combined:=originalParent()
        register(combined,edits[0])
        got:=tryRegister(combined,edits[1])
        if got==nil || !strings.Contains(fmt.Sprint(got),"conflict"){
            t.Fatalf("order %d expected internal radix-tree wildcard conflict, got %#v",i,got)
        }
        assertResponse(t,combined,"GET","/old","unchanged")
    }
    t.Log("P40_MATH_B_P3_ORIGINAL_HTTPROUTER_DISJOINT_HTTP_LANGUAGES_SAME_METHOD_REJECTION_BOTH_ORDERS_PASS")
}
func TestOriginalHttprouterMethodPartitionAvoidsConflict(t *testing.T){
    a:=registration{"GET","/service/:name/a","A"}
    b:=registration{"POST","/service/static/b","B"}
    for i,edits:=range [][2]registration{{a,b},{b,a}}{
        combined:=originalParent()
        for _,e:=range edits{
            if got:=tryRegister(combined,e);got!=nil{t.Fatalf("order %d method-isolated registration failed: %v",i,got)}
        }
        assertResponse(t,combined,"GET","/old","unchanged")
        assertResponse(t,combined,"GET","/service/example/a","A")
        assertResponse(t,combined,"POST","/service/static/b","B")
    }
    t.Log("P40_MATH_B_P3_ORIGINAL_HTTPROUTER_PER_METHOD_SOURCE_TREE_FRAME_PASS")
}
func TestOriginalHttprouterDifferentLiteralBranchesAcceptBoth(t *testing.T){
    a:=registration{"GET","/service/alice/a","A"}
    b:=registration{"GET","/service/bob/b","B"}
    for i,edits:=range [][2]registration{{a,b},{b,a}}{
        combined:=originalParent()
        for _,e:=range edits{
            if got:=tryRegister(combined,e);got!=nil{t.Fatalf("distinct literals order %d: %v",i,got)}
        }
        assertResponse(t,combined,"GET","/old","unchanged")
        assertResponse(t,combined,"GET","/service/alice/a","A")
        assertResponse(t,combined,"GET","/service/bob/b","B")
    }
    t.Log("P40_MATH_B_P3_ORIGINAL_HTTPROUTER_LITERAL_BRANCH_CONTROL_PASS")
}
