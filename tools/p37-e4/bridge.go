// Package e4 is EvoNOMOS-authored experimental integration of two genuinely
// independently evolved original session representations. It is NOT a
// security reviewed production session migration middleware.
package e4

import (
 "context"
 "net/http"
 "net/http/httptest"

 scs "github.com/alexedwards/scs/v2"
 gsessions "github.com/gorilla/sessions"
)

const cookieName = "p37_e4_session"

// Bridge exposes exactly the source capabilities owned by the reader.
// Gorilla: original client-state cookie decoder with known test-only key.
// Server: original SCS server-state token reader with the EXISTING backing store.
type Bridge struct {
 Gorilla *gsessions.CookieStore
 Server *scs.SessionManager
}

// CanReadStage accepts only the pre-registered finite legitimate session
// fixtures whose stage is kept. This tests protocol compatibility, not
// identity, authorization, anti-forgery, attack resilience, or user security.
func (b Bridge) CanReadStage(cookie *http.Cookie) bool {
 if cookie==nil||cookie.Name!=cookieName||cookie.Value=="" {return false}
 if b.Server!=nil {
  ctx,err:=b.Server.Load(context.Background(),cookie.Value)
  if err==nil && b.Server.GetString(ctx,"stage")=="kept" {return true}
 }
 if b.Gorilla!=nil {
  req:=httptest.NewRequest(http.MethodGet,"http://e4.example/read",nil)
  req.AddCookie(cookie)
  session,err:=b.Gorilla.New(req,cookieName)
  if err==nil && session!=nil && !session.IsNew {
   if stage,ok:=session.Values["stage"].(string);ok&&stage=="kept"{return true}
  }
 }
 return false
}
