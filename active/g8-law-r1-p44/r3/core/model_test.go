package core
import("context";"net/http";"net/http/httptest";"testing")
func TestAliasVersusValueCopyWithMutex(t *testing.T){
 for _,tc:=range []struct{mode CaptureMode;want string}{{LiveAlias,"v2|req-A"},{FrozenValue,"v1|req-A"}}{
  s:=NewShared("v1");b:=NewBarrier()
  h:=Capture(tc.mode,s,b)(ItemHandler(func(context.Context)string{return "req-A"}))
  ch:=make(chan string,1)
  go func(){w:=httptest.NewRecorder();h.ServeHTTP(w,httptest.NewRequest(http.MethodGet,"/items/alpha",nil));ch<-w.Body.String()}()
  <-b.Entered;s.Set("v2");close(b.Release)
  if got:=<-ch;got!=tc.want{t.Fatalf("mode=%d got=%q want=%q",tc.mode,got,tc.want)}
 }
}
func TestSequentialOldClientSame(t *testing.T){for _,mode:=range []CaptureMode{LiveAlias,FrozenValue}{
 s:=NewShared("v1");h:=Capture(mode,s,nil)(ItemHandler(func(context.Context)string{return "req-A"}))
 w:=httptest.NewRecorder();h.ServeHTTP(w,httptest.NewRequest("GET","/items/alpha",nil))
 if w.Body.String()!="v1|req-A"{t.Fatal(w.Body.String())}
}}
