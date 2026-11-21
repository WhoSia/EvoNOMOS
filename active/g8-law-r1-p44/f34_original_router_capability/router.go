package originalrouters

import (
 "fmt"
 "net/http"
 "strings"

 "github.com/go-chi/chi/v5"
 "github.com/julienschmidt/httprouter"
)

// RouterKind selects two independently maintained original Go router projects.
type RouterKind string
const (Chi RouterKind = "chi"; HTTPRouter RouterKind = "httprouter")

// Build creates a separate immutable HTTP handler graph with its own provider.
// The upstream router sources are NOT patched.
func Build(kind RouterKind, provider string) (http.Handler, error) {
 switch kind {
 case Chi:
  r:=chi.NewRouter()
  r.Get("/legacy",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,"old")})
  r.Get("/item/{id}",func(w http.ResponseWriter,r *http.Request){
   fmt.Fprint(w,provider+":"+chi.URLParam(r,"id"))
  })
  return r,nil
 case HTTPRouter:
  r:=httprouter.New()
  r.GET("/legacy",func(w http.ResponseWriter,r *http.Request,p httprouter.Params){fmt.Fprint(w,"old")})
  r.GET("/item/:id",func(w http.ResponseWriter,r *http.Request,p httprouter.Params){
   fmt.Fprint(w,provider+":"+p.ByName("id"))
  })
  return r,nil
 default:
  return nil,fmt.Errorf("unknown original router: %s",kind)
 }
}

// Pick is a bounded app-owned selector; never mutates an upstream router.
// http.Handler is an interface, but a function callback can implement exactly
// the same selection logic and is a strong non-interface abstraction rival.
func Pick(handlers map[RouterKind]http.Handler) http.HandlerFunc {
 return func(w http.ResponseWriter,r *http.Request) {
  kind:=RouterKind(strings.ToLower(r.Header.Get("X-Router")))
  h,ok:=handlers[kind]
  if !ok {http.Error(w,"unknown router",http.StatusBadRequest);return}
  h.ServeHTTP(w,r)
 }
}
