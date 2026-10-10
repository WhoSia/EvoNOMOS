package p40p6echo

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "testing"
 echo "github.com/labstack/echo/v5"
)

type headCase struct{
 head bool
 get bool
 auto bool
}
func nativeHead(c headCase)(string,int,int,string){
 router:=echo.NewWithConfig(echo.Config{Router:echo.NewRouter(echo.RouterConfig{AutoHandleHEAD:c.auto})})
 n:=0
 if c.get{
  router.GET("/p6/head",func(ctx *echo.Context)error{
   n++
   ctx.Response().Header().Set("X-P6-Handler","fallback")
   return ctx.String(http.StatusOK,"GET-body-not-present-in-HEAD")
  })
 }
 if c.head{
  router.HEAD("/p6/head",func(ctx *echo.Context)error{
   ctx.Response().Header().Set("X-P6-Handler","direct")
   return ctx.NoContent(http.StatusOK)
  })
 }
 output:=httptest.NewRecorder()
 router.ServeHTTP(output,httptest.NewRequest(http.MethodHead,"/p6/head",nil))
 name:=output.Header().Get("X-P6-Handler")
 if name==""{name="unavailable"}
 return name,n,output.Code,output.Body.String()
}

func TestP40P6ASTGeneratedSourceBranchAgainstNativeEchoFullBooleanCourt(t *testing.T){
 total:=0
 for _,h:=range []bool{false,true}{
  for _,g:=range []bool{false,true}{
   for _,a:=range []bool{false,true}{
    c:=headCase{head:h,get:g,auto:a}
    expected:=p6ExtractedHead(h,g,a)
    observed,calls,status,body:=nativeHead(c)
    if observed!=expected{
     t.Fatalf("P40_P6_AST_NATIVE_COUNTERTRACE source=%s native=%s head=%t get=%t auto=%t status=%d body=%q",expected,observed,h,g,a,status,body)
    }
    if calls!=btoi(expected=="fallback"){
     t.Fatalf("P40_P6_AST_NATIVE_EFFECT_MISMATCH h=%t g=%t a=%t expected=%s calls=%d",h,g,a,expected,calls)
    }
    if expected!="unavailable"&&(status!=200||body!=""){
     t.Fatalf("HEAD status/body failed: expected=%s status=%d body=%q",expected,status,body)
    }
    if expected=="unavailable"&&status==200{
     t.Fatalf("unregistered HEAD should not return OK h=%t g=%t a=%t",h,g,a)
    }
    t.Logf("P40_P6_SOURCE_AST_NATIVE_BOUNDED_EQUIVALENCE head=%t get=%t auto=%t extracted=%s native=%s calls=%d status=%d",h,g,a,expected,observed,calls,status)
    total++
   }
  }
 }
 if total!=8{t.Fatalf("expected 8 test states, got %d",total)}
 t.Log("P40_P6_EIGHT_OF_EIGHT_AST_EXTRACTED_VS_ORIGINAL_ECHO_PASS")
}

func btoi(b bool)int{if b{return 1};return 0}

func TestP40P6MinimalSingleBitHEADSideEffectRepair(t *testing.T){
 // Reachable starting point: only GET registered, automatic HEAD enabled,
 // original HEAD handler missing. One-bit edits are: install explicit HEAD,
 // disable GET, disable automatic HEAD. The last two eliminate HEAD success.
 start:=headCase{head:false,get:true,auto:true}
 name,calls,status,_:=nativeHead(start)
 if name!="fallback"||calls!=1||status!=200{t.Fatalf("source start wrong %s %d %d",name,calls,status)}
 fixes:=0
 edits:=[]struct{name string; c headCase}{
  {"add_explicit_head",headCase{true,true,true}},
  {"remove_get_handler",headCase{false,false,true}},
  {"disable_auto_head",headCase{false,true,false}},
 }
 for _,e:=range edits{
  name,calls,status,_:=nativeHead(e.c)
  fulfills:=status==200&&calls==0&&name=="direct"
  if fulfills{
   fixes++
   if e.name!="add_explicit_head"{t.Fatalf("unexpected one-bit fix %s",e.name)}
  }
  t.Logf("P40_P6_ONE_BIT_REPAIR_CERT candidate=%s outcome=%s status=%d effect=%d fulfills=%t",e.name,name,status,calls,fulfills)
 }
 if fixes!=1{t.Fatalf("expected exactly one bounded one-bit repair, found %d",fixes)}
 t.Log("P40_P6_ONE_BIT_HEAD_EFFECT_REPAIR_UNIQUE_AND_MINIMAL_PASS")
}

func TestP40P6PosthocEchoWildcardCountertrace(t *testing.T){
 // Known P5 issue #2619 countertrace, not preregistered P6 prediction.
 r:=echo.New()
 r.GET("/v2/*/tags/list",func(c *echo.Context)error{return c.String(200,"tags")})
 r.GET("/v2/*/blobs/uploads/:ref",func(c *echo.Context)error{return c.String(200,"uploads")})
 rec:=httptest.NewRecorder()
 r.ServeHTTP(rec,httptest.NewRequest(http.MethodGet,"/v2/foo/bar/tags/list",nil))
 if rec.Code!=200||rec.Body.String()!="uploads"{
  t.Fatalf("P40_P6_WILDCARD_COUNTERTRACE_CHANGED status=%d body=%s",rec.Code,rec.Body.String())
 }
 t.Log(fmt.Sprintf("P40_P6_ECHO_ISSUE_2619_ROUTE_IDENTITY_COUNTERTRACE_EXPECT_TAGS_GOT_UPLOADS status=%d",rec.Code))
}
