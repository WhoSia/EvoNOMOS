package p41p1

import (
  "net/http"
  "net/http/httptest"
  "testing"
  echo "github.com/labstack/echo/v5"
)

const originalPinnedEchoSource = "3882266a3641a36fc2111b48cd597adab1c1ecea"

type observation struct {
  Status int
  Body string
  MatchedTemplate string
  HandlerID string
}

func buildRouter(withSecondRoute bool) (*echo.Echo,*string,*string) {
  e:=echo.New()
  handlerName:=new(string)
  matchName:=new(string)
  e.GET("/old",func(c *echo.Context)error{return c.String(http.StatusOK,"baseline")})
  e.GET("/v2/*/tags/list",func(c *echo.Context)error{
    *handlerName="TAGS"
    *matchName=c.Path()
    return c.String(http.StatusOK,"SAME_RESPONSE")
  })
  if withSecondRoute{
    // Real #2619 issue-derived structural route: permitted source registration
    // but may absorb requests meant for the tags route.
    e.GET("/v2/*/blobs/uploads/:ref",func(c *echo.Context)error{
      *handlerName="UPLOADS"
      *matchName=c.Path()
      return c.String(http.StatusOK,"SAME_RESPONSE")
    })
  }
  return e,handlerName,matchName
}

func probe(t *testing.T,e *echo.Echo, handlerName, matchName *string) observation {
  t.Helper()
  old:=httptest.NewRecorder()
  e.ServeHTTP(old,httptest.NewRequest(http.MethodGet,"/old",nil))
  if old.Code!=200||old.Body.String()!="baseline"{
    t.Fatalf("old client contract violation: %d %q",old.Code,old.Body.String())
  }
  rec:=httptest.NewRecorder()
  e.ServeHTTP(rec,httptest.NewRequest(http.MethodGet,"/v2/foo/bar/tags/list",nil))
  return observation{rec.Code,rec.Body.String(),*matchName,*handlerName}
}

func TestP41P1IdenticalHTTPResponseDifferentSourceSelectedHandler(t *testing.T) {
  alone, aloneHandler,aloneRoute:=buildRouter(false)
  withCollision,collisionHandler,collisionRoute:=buildRouter(true)
  a:=probe(t,alone,aloneHandler,aloneRoute)
  b:=probe(t,withCollision,collisionHandler,collisionRoute)

  if a.Status!=200||b.Status!=200||a.Body!="SAME_RESPONSE"||b.Body!="SAME_RESPONSE"{
    t.Fatalf("client-only selected response assumptions failed: control=%+v collision=%+v",a,b)
  }
  if a.Status!=b.Status||a.Body!=b.Body{
    t.Fatalf("client coarse outputs diverged: control=%+v collision=%+v",a,b)
  }
  if a.HandlerID!="TAGS"||b.HandlerID!="UPLOADS"{
    t.Fatalf("expected different *native source-selected* handler IDs: control=%+v collision=%+v",a,b)
  }
  if a.MatchedTemplate!="/v2/*/tags/list"||
     b.MatchedTemplate!="/v2/*/blobs/uploads/:ref"{
    t.Fatalf("original route selection evidence changed: control=%+v collision=%+v",a,b)
  }
  t.Logf("P41_P1_SAME_HTTP_STATUS_BODY_DIFFERENT_ACTUAL_HANDLER_PASS status=%d body=%q correct=%q shadowed=%q",a.Status,a.Body,a.HandlerID,b.HandlerID)
  t.Logf("P41_P1_ORIGINAL_ROUTE_IDENTITY_READOUT_PASS correct=%q shadowed=%q",a.MatchedTemplate,b.MatchedTemplate)
}
