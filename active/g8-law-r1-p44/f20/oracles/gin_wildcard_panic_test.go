package gin
import("strings";"testing")
// Retrospective historical fix oracle; demonstrates error-message identity,
// not the absence of panic on a deliberately illegal wildcard route.
func TestF20WildcardErrorType(t *testing.T){
 var message any
 func(){defer func(){message=recover()}();tree:=&node{};tree.addRoute("/foo/b*r",nil)}()
 msg,ok:=message.(string)
 t.Logf("F20_GIN invalid_wildcard_panic=%v",message)
 if !ok||!strings.HasPrefix(msg,"no / before catch-all in path"){t.Fatalf("unexpected panic string: %v",message)}
}
