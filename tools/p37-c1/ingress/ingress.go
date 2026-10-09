// Package ingress is owner A; it depends only on its port, not archive.Store.
// The HTTP router is the original, externally pinned go-chi/chi core.
package ingress

import (
 "encoding/json"
 "io"
 "net/http"

 "github.com/go-chi/chi/v5"
)
type StorePort interface{
 AppendSemantic(id int,raw []byte)
 State()(id int,revision int)
}
type Component struct{ router http.Handler }
func New(store StorePort,forwardOriginal bool)*Component{
 router:=chi.NewRouter()
 router.Post("/events",func(w http.ResponseWriter,r *http.Request){
  payload,err:=io.ReadAll(io.LimitReader(r.Body,8192))
  if err!=nil{http.Error(w,"read",http.StatusBadRequest);return}
  var item struct{ ID int `json:"id"` }
  if err=json.Unmarshal(payload,&item);err!=nil{http.Error(w,"json",http.StatusBadRequest);return}
  forwarded:=[]byte(nil)
  if forwardOriginal{forwarded=payload}
  store.AppendSemantic(item.ID,forwarded)
  w.WriteHeader(http.StatusNoContent)
 })
 router.Get("/state",func(w http.ResponseWriter,r *http.Request){
  id,rev:=store.State()
  w.Header().Set("Content-Type","application/json")
  _=json.NewEncoder(w).Encode(struct{
   ID int `json:"id"`
   Revision int `json:"revision"`
  }{id,rev})
 })
 return &Component{router:router}
}
func(c *Component)ServeHTTP(w http.ResponseWriter,r *http.Request){c.router.ServeHTTP(w,r)}
