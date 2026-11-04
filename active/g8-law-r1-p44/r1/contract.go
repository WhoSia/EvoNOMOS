package r1

import (
 "fmt"
 "net/http"
 "net/url"

 "github.com/go-chi/chi/v5"
)

// ChiAdapterSettings names three independently authorized, application-owned interventions.
// These are synthetic edit units, not developer hours or arbitrary upstream editing powers.
type ChiAdapterSettings struct {
 RegisterHEAD bool
 DecodeParam bool
 MatchMethodError bool
}

func Standard(stage int) http.Handler {
 mux := http.NewServeMux()
 mux.HandleFunc("GET /items/{id}",func(w http.ResponseWriter,r *http.Request){
  _,_=fmt.Fprint(w,r.PathValue("id"))
 })
 if stage>=1 {mux.HandleFunc("GET /lookup/{id}",func(w http.ResponseWriter,r *http.Request){
  _,_=fmt.Fprint(w,"lookup:",r.PathValue("id"))
 })}
 if stage>=2 {mux.HandleFunc("GET /lookup/{id}/meta",func(w http.ResponseWriter,r *http.Request){
  _,_=fmt.Fprint(w,"meta:",r.PathValue("id"))
 })}
 return mux
}

func Chi(stage int,c ChiAdapterSettings) http.Handler {
 mux := chi.NewRouter()
 item := func(w http.ResponseWriter,r *http.Request) {
  id:=chi.URLParam(r,"id")
  if c.DecodeParam {
   v,e:=url.PathUnescape(id)
   if e!=nil {http.Error(w,"invalid encoded parameter",http.StatusBadRequest);return}
   id=v
  }
  _,_=fmt.Fprint(w,id)
 }
 mux.Get("/items/{id}",item)
 if c.RegisterHEAD {mux.Head("/items/{id}",item)}
 if c.MatchMethodError {
  mux.MethodNotAllowed(func(w http.ResponseWriter,r *http.Request){
   w.Header().Set("Allow","GET, HEAD")
   http.Error(w,"Method Not Allowed",http.StatusMethodNotAllowed)
  })
 }
 if stage>=1 {mux.Get("/lookup/{id}",func(w http.ResponseWriter,r *http.Request) {
  _,_=fmt.Fprint(w,"lookup:",chi.URLParam(r,"id"))
 })}
 if stage>=2 {mux.Get("/lookup/{id}/meta",func(w http.ResponseWriter,r *http.Request) {
  _,_=fmt.Fprint(w,"meta:",chi.URLParam(r,"id"))
 })}
 return mux
}

func RawChi(stage int) http.Handler{return Chi(stage,ChiAdapterSettings{})}
func FullChi(stage int) http.Handler{return Chi(stage,ChiAdapterSettings{true,true,true})}
