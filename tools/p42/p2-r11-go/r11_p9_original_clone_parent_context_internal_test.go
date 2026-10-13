package chi

import (
 "context"
 "os"
 "testing"
)
func TestR11P9AuthorialCloneParentContextRetention(t *testing.T){
 expect:=os.Getenv("R11P9_EXPECT_DETACH")
 if expect!="0"&&expect!="1"{t.Fatal("Missing preregistered version-specific internal resource retention oracle")}
 x:=NewRouteContext()
 x.parentCtx=context.WithValue(context.Background(),struct{}{},"request-scope")
 x.URLParams.Keys=[]string{"id"}
 x.URLParams.Values=[]string{"Ada"}
 cloned:=x.Clone()
 if cloned.URLParam("id")!="Ada"{t.Fatal("clone lost declared observable")}
 detached:=cloned.parentCtx==nil
 if detached!=(expect=="1"){t.Fatalf("original upstream source parentCtx detachment not as frozen: expected=%v actual=%v",expect,detached)}
 t.Logf("R11_P9_ORIGINAL_CLONE_RESOURCE_FRAME_NATIVE_PASS detached=%v expected=%v",detached,expect=="1")
}
