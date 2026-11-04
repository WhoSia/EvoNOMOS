package r2
import ("fmt";"net/http";"net/url";"github.com/go-chi/chi/v5")
type Demand struct{Name,Pattern,ResponsePrefix string}
var FrozenDemands=[]Demand{
 {"revisions","/ledger/{id}/revisions","revisions:"},
 {"audit","/ledger/{id}/audit","audit:"},
 {"summary","/ledger/{id}/summary","summary:"},
}
func StdlibRouter(enabled []int)http.Handler{
 m:=http.NewServeMux()
 m.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,r.PathValue("id"))})
 for _,idx:=range enabled{
  d:=FrozenDemands[idx]
  m.HandleFunc("GET "+d.Pattern,func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,d.ResponsePrefix,r.PathValue("id"))})
 }
 return m
}
func ChiRouter(enabled []int)http.Handler{
 m:=chi.NewRouter()
 item:=func(w http.ResponseWriter,r *http.Request){
  v,e:=url.PathUnescape(chi.URLParam(r,"id"));if e!=nil{http.Error(w,"invalid encoded parameter",http.StatusBadRequest);return}
  fmt.Fprint(w,v)
 }
 m.Get("/items/{id}",item)
 m.Head("/items/{id}",item)
 m.MethodNotAllowed(func(w http.ResponseWriter,r *http.Request){
  w.Header().Set("Allow","GET, HEAD");http.Error(w,"Method Not Allowed",http.StatusMethodNotAllowed)
 })
 for _,idx:=range enabled{
  d:=FrozenDemands[idx]
  m.Get(d.Pattern,func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,d.ResponsePrefix,chi.URLParam(r,"id"))})
 }
 return m
}
