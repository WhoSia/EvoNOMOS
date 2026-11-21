package gin
import("strings";"testing")
// RETROSPECTIVE internal helper boundary. This is NOT proof about an
// externally supported HTTP route beginning without "/".
// In the original Go source, wildcard at index 0 makes i-- negative.
// The upstream correction guards negative i before indexing path[i].
func TestF20WildcardErrorType(t *testing.T){
 var message any
 func(){
  defer func(){message=recover()}()
  tree:=&node{}
  tree.insertChild("*all","*all",nil)
 }()
 msg,ok:=message.(string)
 t.Logf("F20_GIN catchall_at_index_zero_panic=%v",message)
 if !ok||!strings.HasPrefix(msg,"no / before catch-all in path"){
  t.Fatalf("wrong boundary panic kind: %v",message)
 }
}
