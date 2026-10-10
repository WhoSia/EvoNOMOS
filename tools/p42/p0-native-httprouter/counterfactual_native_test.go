package p42httprouter

import(
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "testing"
 router "github.com/julienschmidt/httprouter"
)
type Obs struct {
 Status int `json:"status"`
 Body string `json:"body"`
 ContractHeader string `json:"contract_header"`
 HandlerID string `json:"handler_id"`
 Invocations int `json:"invocations"`
}
type Case struct{
 ID string `json:"id"`
 Ecosystem string `json:"ecosystem"`
 SourceAdmitted bool `json:"source_admitted"`
 OldFrame string `json:"old_frame"`
 NewGoal string `json:"new_goal"`
 HandlerResult string `json:"handler_result"`
 Authority string `json:"authority"`
 Observation Obs `json:"observation"`
}
func caseOutput(t *testing.T,c Case){
 t.Helper()
 b,err:=json.Marshal(c)
 if err!=nil {t.Fatal(err)}
 t.Log("P42_NATIVE_CASE "+string(b))
}
func request(t *testing.T,r *router.Router,method,path string)Obs{
 t.Helper()
 w:=httptest.NewRecorder()
 r.ServeHTTP(w,httptest.NewRequest(method,path,nil))
 return Obs{Status:w.Code,Body:w.Body.String(),ContractHeader:w.Header().Get("X-Contract")}
}
func baseline(t *testing.T)(*router.Router,*int){
 t.Helper()
 r:=router.New()
 invocations:=new(int)
 r.GET("/p42/old",func(w http.ResponseWriter,_ *http.Request,_ router.Params){
  *invocations++
  w.Header().Set("X-Contract","old")
  w.WriteHeader(200)
  _,_ =w.Write([]byte("OLD"))
 })
 return r,invocations
}
func TestP42HTTPRouterDisjointAndCollision(t *testing.T){
 r,calls:=baseline(t)
 fresh:=0
 r.GET("/p42/extension",func(w http.ResponseWriter,_ *http.Request,_ router.Params){
  fresh++
  w.Header().Set("X-Contract","extension")
  w.WriteHeader(201)
  _,_=w.Write([]byte("NEW"))
 })
 old:=request(t,r,http.MethodGet,"/p42/old")
 old.HandlerID="OLD";old.Invocations=*calls
 ext:=request(t,r,http.MethodGet,"/p42/extension")
 if old.Status!=200||old.Body!="OLD"||old.ContractHeader!="old"||*calls!=1||ext.Status!=201||ext.Body!="NEW"||ext.ContractHeader!="extension"||fresh!=1{
  t.Fatalf("disjoint contract drift: old=%+v new=%+v",old,ext)
 }
 caseOutput(t,Case{"httprouter-disjoint","httprouter",true,"PRESERVED","FULFILLED","OLD","UNKNOWN",old})

 // Registration panic is the ORIGINAL source rejection outcome. The router
 // stays a test fixture; no accepted combined program exists, so old frame
 // is epistemically NOT_APPLICABLE, not automatically preserved.
 rejected:=false
 func(){
  defer func(){if recovered:=recover();recovered!=nil{rejected=true}}()
  r.GET("/p42/old",func(w http.ResponseWriter,_ *http.Request,_ router.Params){
   w.Header().Set("X-Contract","replacement")
   w.WriteHeader(200)
   _,_=w.Write([]byte("REPLACED"))
  })
 }()
 if !rejected{t.Fatal("original httprouter source no longer rejects exact duplicate GET route")}
 caseOutput(t,Case{"httprouter-collision","httprouter",false,"NOT_APPLICABLE","REJECTED","NOT_APPLICABLE","UNKNOWN",Obs{}})
}
func TestP42HTTPRouterSamePathDifferentMethod(t *testing.T){
 r,calls:=baseline(t)
 postCalls:=0
 r.POST("/p42/old",func(w http.ResponseWriter,_ *http.Request,_ router.Params){
  postCalls++
  w.Header().Set("X-Contract","post")
  w.WriteHeader(202)
  _,_=w.Write([]byte("POST_HANDLED"))
 })
 old:=request(t,r,http.MethodGet,"/p42/old")
 old.HandlerID="OLD";old.Invocations=*calls
 post:=request(t,r,http.MethodPost,"/p42/old")
 if old.Status!=200||old.Body!="OLD"||old.ContractHeader!="old"||*calls!=1||post.Status!=202||post.Body!="POST_HANDLED"||post.ContractHeader!="post"||postCalls!=1{
  t.Fatalf("different method source contract drift old=%+v post=%+v calls=%d",old,post,postCalls)
 }
 caseOutput(t,Case{"httprouter-separate-method","httprouter",true,"PRESERVED","POST_OWN_HANDLER","OLD","UNKNOWN",old})
}
