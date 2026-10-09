package cookie

import (
 "bytes"
 "net/http"
 "net/http/httptest"
 "testing"

 gsessions "github.com/gin-contrib/sessions"
 "github.com/gin-gonic/gin"
)

func p37E3Keys()([]byte,[]byte){
 return bytes.Repeat([]byte{'A'},32),bytes.Repeat([]byte{'B'},32)
}
func p37E3Issue(t *testing.T,store Store)*http.Cookie{
 t.Helper()
 router:=gin.New()
 router.Use(gsessions.Sessions("p37_e3",store))
 router.GET("/issue",func(c *gin.Context){
  session:=gsessions.Default(c)
  session.Set("stage","kept")
  if err:=session.Save();err!=nil {
   t.Errorf("original gin session save: %v",err)
   c.Status(http.StatusInternalServerError)
   return
  }
  c.Status(http.StatusNoContent)
 })
 reply:=httptest.NewRecorder()
 router.ServeHTTP(reply,httptest.NewRequest(http.MethodGet,"http://example.test/issue",nil))
 if reply.Code!=http.StatusNoContent{t.Fatalf("issued status=%d body=%s",reply.Code,reply.Body.String())}
 cookies:=reply.Result().Cookies()
 if len(cookies)!=1{t.Fatalf("issued cookie count=%d, want=1",len(cookies))}
 return cookies[0]
}
func p37E3CanRead(t *testing.T,store Store,sessionCookie *http.Cookie)bool{
 t.Helper()
 router:=gin.New()
 router.Use(gsessions.Sessions("p37_e3",store))
 router.GET("/read",func(c *gin.Context){
  v:=gsessions.Default(c).Get("stage")
  if v!="kept"{
   c.Status(http.StatusNotFound)
   return
  }
  c.String(http.StatusOK,"kept")
 })
 req:=httptest.NewRequest(http.MethodGet,"http://example.test/read",nil)
 req.AddCookie(sessionCookie)
 reply:=httptest.NewRecorder()
 router.ServeHTTP(reply,req)
 return reply.Code==200&&reply.Body.String()=="kept"
}
func TestP37E3OriginalGinGorillaCompatibilityTransport(t *testing.T){
 oldKey,newKey:=p37E3Keys()
 w0,w1:=NewStore(oldKey),NewStore(newKey)
 r0,r1:=NewStore(oldKey),NewStore(newKey)
 rStar:=NewStore(newKey,nil,oldKey,nil)
 oldCookie:=p37E3Issue(t,w0)
 newCookie:=p37E3Issue(t,w1)
 cases:=[]struct{name string;live *http.Cookie;reader Store;wantLive,wantLegacy bool}{
  {"OLD_WRITER_OLD_READER",oldCookie,r0,true,true},
  {"NEW_WRITER_OLD_READER",newCookie,r0,false,true},
  {"OLD_WRITER_NEW_READER",oldCookie,r1,false,false},
  {"OLD_WRITER_DUAL_READER",oldCookie,rStar,true,true},
  {"NEW_WRITER_DUAL_READER",newCookie,rStar,true,true},
  {"NEW_WRITER_NEW_READER",newCookie,r1,true,false},
 }
 for _,tc:=range cases{
  t.Run(tc.name,func(t *testing.T){
   live:=p37E3CanRead(t,tc.reader,tc.live)
   legacy:=p37E3CanRead(t,tc.reader,oldCookie)
   if live!=tc.wantLive||legacy!=tc.wantLegacy{
    t.Fatalf("Gin actual live=%v legacy=%v want live=%v legacy=%v",live,legacy,tc.wantLive,tc.wantLegacy)
   }
  })
 }
}
