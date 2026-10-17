package middleware

import (
 "net/http"
 "net/http/httptest"
 "os"
 "reflect"
 "testing"
)

// Source snapshots are authentic upstream code; only THIS fixture is authored.
// A method signature/outer concrete type cannot expose the stateful transport
// side effect of Flush when Discard is set.
func TestEvoNOMOSP10P4QAuthenticChi1185DiscardFlushEffect(t *testing.T) {
 phase:=os.Getenv("P10P4Q_CHI_SOURCE_PHASE")
 if phase!="baseline" && phase!="merged" {t.Fatalf("unexpected phase %q",phase)}
 for _,discard:=range []bool{false,true}{
  for _,controller:=range []bool{false,true}{
   label:="direct"
   if controller {label="ResponseController"}
   t.Run(label+"/"+map[bool]string{false:"passthrough",true:"discard"}[discard],func(t *testing.T){
    sink:=httptest.NewRecorder()
    wrapped:=NewWrapResponseWriter(sink,1)
    if typ:=reflect.TypeOf(wrapped).String();typ!="*middleware.flushWriter" {
     t.Fatalf("unexpected source wrapper concrete type %s",typ)
    }
    f,ok:=wrapped.(http.Flusher)
    if !ok {t.Fatal("outer source writer does not support http.Flusher")}
    if discard {wrapped.Discard()}
    if controller {
     if err:=http.NewResponseController(wrapped).Flush();err!=nil {
      t.Fatalf("ResponseController.Flush %v",err)
     }
    } else {f.Flush()}
    expected:=!discard||phase=="baseline"
    if sink.Flushed!=expected {
     t.Fatalf("phase=%s discard=%t mechanism=%s transportFlushed=%t, expected=%t",
      phase,discard,label,sink.Flushed,expected)
    }
    if wrapped.Status()!=http.StatusOK||wrapped.BytesWritten()!=0||sink.Body.Len()!=0{
     t.Fatalf("observable status/bytes/body diverged: status=%d count=%d body=%q",
      wrapped.Status(),wrapped.BytesWritten(),sink.Body.String())
    }
    t.Logf("CHI1185_NATIVE phase=%s discard=%t mechanism=%s wrapper=flushWriter hasFlusher=true wrapperStatus=200 wrapperBytes=0 bodyBytes=0 transportFlush=%t",
     phase,discard,label,sink.Flushed)
   })
  }
 }
}
