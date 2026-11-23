// Package callbackarm independently builds a pinned original-router application
// with function callbacks as its application-owned selection abstraction.
//
// F37 baseline: no source in this package calls handlerarm or
// originalrouters.Build/Pick. The upstream routers still conform to
// http.Handler: our comparison is only of the app-owned dispatch boundary.
package callbackarm

import (
    "fmt"
    "net/http"
    "strings"

    "github.com/go-chi/chi/v5"
    "github.com/julienschmidt/httprouter"
)

type Kind string

const (
    Chi Kind = "chi"
    HTTPRouter Kind = "httprouter"
)

// New creates a private callback table and returns a function, not an
// interface-typed application selector. Construction does not expose mutable
// configuration to callers. Both upstream projects remain unmodified.
func New(chiVersion, httpRouterVersion string) func(http.ResponseWriter, *http.Request) {
    chiNative := chi.NewRouter()
    chiNative.Get("/legacy", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "old")
    })
    chiNative.Get("/item/{id}", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, chiVersion+":"+chi.URLParam(r, "id"))
    })

    otherNative := httprouter.New()
    otherNative.GET("/legacy", func(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
        fmt.Fprint(w, "old")
    })
    otherNative.GET("/item/:id", func(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
        fmt.Fprint(w, httpRouterVersion+":"+p.ByName("id"))
    })

    dispatch := map[Kind]func(http.ResponseWriter, *http.Request){
        Chi: chiNative.ServeHTTP,
        HTTPRouter: otherNative.ServeHTTP,
    }
    return func(w http.ResponseWriter, r *http.Request) {
        kind := Kind(strings.ToLower(r.Header.Get("X-Router")))
        call, found := dispatch[kind]
        if !found {
            http.Error(w, "unknown router", http.StatusBadRequest)
            return
        }
        call(w, r)
    }
}
