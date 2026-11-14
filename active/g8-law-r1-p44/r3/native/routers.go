package native
import("net/http";"evonomos/p44r3core";"github.com/go-chi/chi/v5";"github.com/go-chi/chi/v5/middleware")
func Build(kind string,mode core.CaptureMode,shared *core.Shared,barrier *core.Barrier)http.Handler{
 var router http.Handler
 switch kind{
 case "stdlib":
  m:=http.NewServeMux()
  m.HandleFunc("GET /items/{id}",core.ItemHandler(middleware.GetReqID))
  m.HandleFunc("POST /policy/{id}",core.UpdateHandler(shared))
  router=m
 case "chi":
  m:=chi.NewRouter()
  m.Get("/items/{id}",core.ItemHandler(middleware.GetReqID))
  m.Post("/policy/{id}",core.UpdateHandler(shared))
  router=m
 default:panic("unrecognized router")
 }
 return middleware.RequestID(core.Capture(mode,shared,barrier)(router))
}
