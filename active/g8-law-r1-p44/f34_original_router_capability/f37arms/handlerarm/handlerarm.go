// Package handlerarm independently builds a pinned original-router application
// with http.Handler as its application-owned selection abstraction.
//
// F37 baseline: the input behavior and sources are frozen before any
// independently authored future change. This package must not call
// originalrouters.Build/Pick or the callbackarm rival.
package handlerarm

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

// New creates and privately owns both original router instances and a fixed
// handler map. Callers cannot mutate the selection configuration after
// construction through this API. The upstream router implementations are
// unmodified; this package only registers application routes.
func New(chiVersion, httpRouterVersion string) http.Handler {
    first := chi.NewRouter()
    first.Get("/legacy", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "old")
    })
    first.Get("/item/{id}", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, chiVersion+":"+chi.URLParam(r, "id"))
    })

    second := httprouter.New()
    second.GET("/legacy", func(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
        fmt.Fprint(w, "old")
    })
    second.GET("/item/:id", func(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
        fmt.Fprint(w, httpRouterVersion+":"+p.ByName("id"))
    })

    providers := map[Kind]http.Handler{
        Chi: first,
        HTTPRouter: second,
    }

    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        target := Kind(strings.ToLower(r.Header.Get("X-Router")))
        selected, ok := providers[target]
        if !ok {
            http.Error(w, "unknown router", http.StatusBadRequest)
            return
        }
        selected.ServeHTTP(w, r)
    })
}
