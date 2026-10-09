package e4

import (
 "bytes"
 "context"
 "net/http"
 "net/http/httptest"
 "testing"

 scs "github.com/alexedwards/scs/v2"
 gsessions "github.com/gorilla/sessions"
)

const p37E4CookieName="p37_e4_session"

func p37E4GorillaIssuer(t *testing.T)(*gsessions.CookieStore,*http.Cookie){
 t.Helper()
 store:=gsessions.NewCookieStore(bytes.Repeat([]byte{'A'},32))
 req:=httptest.NewRequest(http.MethodGet,"http://e4.example/issue",nil)
 sess,err:=store.New(req,p37E4CookieName)
 if err!=nil{t.Fatal(err)}
 sess.Values["stage"]="kept"
 reply:=httptest.NewRecorder()
 if err=store.Save(req,reply,sess);err!=nil{t.Fatal(err)}
 cs:=reply.Result().Cookies()
 if len(cs)!=1{t.Fatalf("Gorilla original cookie count=%d",len(cs))}
 return store,cs[0]
}

func p37E4SCSIssuer(t *testing.T)(*scs.SessionManager,*http.Cookie){
 t.Helper()
 manager:=scs.New()
 ctx,err:=manager.Load(context.Background(),"")
 if err!=nil{t.Fatal(err)}
 manager.Put(ctx,"stage","kept")
 token,_,err:=manager.Commit(ctx)
 if err!=nil||token==""{t.Fatalf("original SCS commit token=%q err=%v",token,err)}
 return manager,&http.Cookie{Name:p37E4CookieName,Value:token}
}

func TestP37E4IndependentAlgorithmCapabilityMatrix(t *testing.T){
 g,oldCookie:=p37E4GorillaIssuer(t)
 s,newCookie:=p37E4SCSIssuer(t)
 wrongStore:=scs.New() // independently allocated backend has no token state.
 cases:=[]struct{
  name string
  bridge Bridge
  wantOld,wantNew bool
 }{
  {"gorilla_only",Bridge{Gorilla:g},true,false},
  {"scs_only",Bridge{Server:s},false,true},
  {"both_original_capabilities",Bridge{Gorilla:g,Server:s},true,true},
  {"server_only_no_old_key",Bridge{Server:s},false,true},
  {"old_key_only_no_server_store",Bridge{Gorilla:g},true,false},
  {"wrong_server_store",Bridge{Gorilla:g,Server:wrongStore},true,false},
 }
 for _,tc:=range cases{
  t.Run(tc.name,func(t *testing.T){
   oldOK:=tc.bridge.CanReadStage(oldCookie)
   newOK:=tc.bridge.CanReadStage(newCookie)
   if oldOK!=tc.wantOld||newOK!=tc.wantNew{
    t.Fatalf("original algorithm result old=%v new=%v want=(%v,%v)",
       oldOK,newOK,tc.wantOld,tc.wantNew)
   }
  })
 }
}

func TestP37E4SafeOwnerSequentialRolloutAndNoPrematureContraction(t *testing.T){
 g,oldCookie:=p37E4GorillaIssuer(t)
 s,newCookie:=p37E4SCSIssuer(t)
 stages:=[]struct{
  label string;reader Bridge;issued *http.Cookie
 }{
  {"initial_old_writer_and_reader",Bridge{Gorilla:g},oldCookie},
  {"B_expand_first",Bridge{Gorilla:g,Server:s},oldCookie},
  {"A_switch_to_independent_SCS",Bridge{Gorilla:g,Server:s},newCookie},
 }
 for _,tc:=range stages{
  t.Run(tc.label,func(t *testing.T){
   if !tc.reader.CanReadStage(tc.issued){t.Fatal("lost live compatibility")}
   if !tc.reader.CanReadStage(oldCookie){t.Fatal("lost legacy compatibility")}
  })
 }
 if !((Bridge{Server:s}).CanReadStage(newCookie)){t.Fatal("new-only reader should read new state")}
 if (Bridge{Server:s}).CanReadStage(oldCookie){t.Fatal("early contraction must not read old state")}
}

func TestP37E4NoAlgorithmOnlySemanticCongruenceUnderFutureContext(t *testing.T){
 g,oldCookie:=p37E4GorillaIssuer(t)
 s,newCookie:=p37E4SCSIssuer(t)
 full:=Bridge{Gorilla:g,Server:s}
 if !full.CanReadStage(oldCookie)||!full.CanReadStage(newCookie){
  t.Fatal("same current semantic observation absent")
 }
 // A future read context restricted to the server-side store distinguishes
 // the two original states, despite identical current semantic payload.
 scsOnly:=Bridge{Server:s}
 if scsOnly.CanReadStage(oldCookie)||!scsOnly.CanReadStage(newCookie){
  t.Fatal("future context failed to distinguish historical representations")
 }
}
