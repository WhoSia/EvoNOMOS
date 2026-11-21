package issue825
import("fmt";"net/http";"github.com/go-chi/chi/v5";"github.com/go-chi/chi/v5/middleware")
func observeOuter(next http.Handler)http.Handler{
 return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  w.Header().Set("X-Outer-Observed",middleware.GetReqID(r.Context()))
  next.ServeHTTP(w,r)
 })
}
// PreserveRequestID performs an application-only clone/forwarding adapter, with
// neither upstream middleware byte changes nor edits to global RequestIDHeader.
func PreserveRequestID(next http.Handler)http.Handler{
 return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if id:=middleware.GetReqID(r.Context());id!=""{
   rr:=r.Clone(r.Context());rr.Header=r.Header.Clone()
   rr.Header.Set(middleware.RequestIDHeader,id)
   next.ServeHTTP(w,rr);return
  }
  next.ServeHTTP(w,r)
 })
}
func Build(kind string,preserve bool)http.Handler{
 handler:=func(w http.ResponseWriter,r *http.Request){fmt.Fprint(w,middleware.GetReqID(r.Context()))}
 var router http.Handler
 switch kind{
 case "stdlib":
  m:=http.NewServeMux();m.HandleFunc("GET /id",handler);router=m
 case "chi":
  m:=chi.NewRouter();m.Get("/id",handler);router=m
 default:panic("unknown router")
 }
 inner:=middleware.RequestID(router)
 if preserve{inner=PreserveRequestID(inner)}
 return middleware.RequestID(observeOuter(inner))
}
