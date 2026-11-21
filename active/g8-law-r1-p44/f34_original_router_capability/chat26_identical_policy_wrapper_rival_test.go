package originalrouters

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "evonomos/f34-original-router-capability/f37arms/callbackarm"
    "evonomos/f34-original-router-capability/f37arms/handlerarm"
)

// A researcher-authored identical application policy imposed outside either
// frozen arm. This is not a reproduction of external Chi issue #1035.
func chat26ReservedItemPolicy(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
        if r.Method==http.MethodGet && r.URL.Path=="/item/me" {
            http.Error(w,"reserved identifier",http.StatusForbidden)
            return
        }
        next.ServeHTTP(w,r)
    })
}

func TestChat26SameDemandAndEqualInformationWrapperRival(t *testing.T) {
    interfaceArm:=handlerarm.New("chi-v","http-v")
    callbackArm:=http.HandlerFunc(callbackarm.New("chi-v","http-v"))
    arms:=[]struct{name string;original http.Handler}{
        {"interface",interfaceArm},
        {"callback",callbackArm},
    }
    originalReq:=httptest.NewRequest("GET","/item/me",nil)
    originalReq.Header.Set("X-Router","chi")
    for _,arm:=range arms{
        out:=httptest.NewRecorder()
        arm.original.ServeHTTP(out,originalReq)
        if out.Code!=200 || out.Body.String()!="chi-v:me"{
            t.Fatalf("original arm %s baseline incorrect %d/%q",arm.name,out.Code,out.Body.String())
        }
    }
    requests:=[]struct{provider,path,body string;status int}{
        {"chi","/item/me","reserved identifier\n",403},
        {"httprouter","/item/me","reserved identifier\n",403},
        {"chi","/item/a","chi-v:a",200},
        {"httprouter","/item/a","http-v:a",200},
        {"CHI","/item/abc","chi-v:abc",200},
        {"HTTPROUTER","/item/abc","http-v:abc",200},
        {"chi","/legacy","old",200},
        {"","/legacy","unknown router\n",400},
    }
    for _,arm:=range arms{
        t.Run(arm.name,func(t *testing.T){
            guarded:=chat26ReservedItemPolicy(arm.original)
            for _,tc:=range requests{
                req:=httptest.NewRequest("GET",tc.path,nil)
                req.Header.Set("X-Router",tc.provider)
                out:=httptest.NewRecorder()
                guarded.ServeHTTP(out,req)
                if out.Code!=tc.status || out.Body.String()!=tc.body{
                    t.Fatalf("%s %s %s => %d/%q instead of %d/%q",
                        arm.name,tc.provider,tc.path,out.Code,out.Body.String(),tc.status,tc.body)
                }
            }
            t.Logf("%s: same source-level outer wrapper provides policy on 8 matched calls",arm.name)
        })
    }
}
