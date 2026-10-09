// P36-O2 independent-source treatment: this code compiles INSIDE pinned
// gorilla/mux v1.8.1, using original Router.NewRoute, Headers and ServeHTTP.
// It is a research-only adapter over the declared exact-header common subset.
package mux

import (
  "net/http"
  "sync"
)

type p36O2RouteEntry struct {
    header string
    values []string
    middleware func(next http.Handler) http.Handler
}

type P35EpochRouter struct {
    mu sync.Mutex
    next http.Handler
    registered []p36O2RouteEntry
    defaultMiddleware func(http.Handler) http.Handler
    published *Router
    revision uint64
    publishedRevision uint64
    rebuilds uint64
}

func NewP35EpochRouter(next http.Handler) *P35EpochRouter {
    if next == nil {next=http.NotFoundHandler()}
    p:=&P35EpochRouter{next:next}
    p.published=p.compileLocked()
    return p
}

// compileLocked recompiles the genuine mux.Router from a private frozen list.
// It is called only while mu is held; the result is never mutated afterwards.
func(p *P35EpochRouter)compileLocked()*Router{
    router:=NewRouter()
    router.NotFoundHandler=p.next
    for _,entry:=range p.registered {
        for _,value:=range entry.values {
            router.NewRoute().Headers(entry.header,value).Handler(entry.middleware(p.next))
        }
    }
    if p.defaultMiddleware!=nil {router.NotFoundHandler=p.defaultMiddleware(p.next)}
    return router
}
func (p *P35EpochRouter)publishLocked(){
    p.published=p.compileLocked()
    p.publishedRevision=p.revision
    p.rebuilds++
}
func(p *P35EpochRouter)updatedLocked(){
    p.revision++
    p.publishLocked()
}
func(p *P35EpochRouter)Register(header,match string,middleware func(http.Handler)http.Handler){
    p.mu.Lock();defer p.mu.Unlock()
    p.registered=append(p.registered,p36O2RouteEntry{header:header,values:[]string{match},middleware:middleware})
    p.updatedLocked()
}
func(p *P35EpochRouter)RegisterAny(header string,match []string,middleware func(http.Handler)http.Handler){
    p.mu.Lock();defer p.mu.Unlock()
    copyValues:=append([]string(nil),match...)
    p.registered=append(p.registered,p36O2RouteEntry{header:header,values:copyValues,middleware:middleware})
    p.updatedLocked()
}
func(p *P35EpochRouter)RegisterDefault(middleware func(http.Handler)http.Handler){
    p.mu.Lock();defer p.mu.Unlock()
    p.defaultMiddleware=middleware
    p.updatedLocked()
}
func(p *P35EpochRouter)ServeHTTP(w http.ResponseWriter,r *http.Request){
    p.mu.Lock()
    // Every completed registration has already been published.
    published:=p.published
    p.mu.Unlock()
    published.ServeHTTP(w,r)
}
func(p *P35EpochRouter)Stats()(revision,published,rebuilds uint64){
    p.mu.Lock();defer p.mu.Unlock()
    return p.revision,p.publishedRevision,p.rebuilds
}
