// P35-O6 research-only source extension to the pinned original Chi module.
// Matched API, distinct publication timing; direct external HeaderRouter
// map writes are intentionally excluded from the synchronization contract.
package middleware

import (
    "net/http"
    "sync"
)

type P35EpochRouter struct {
    mu sync.Mutex
    next http.Handler
    registry HeaderRouter
    published http.Handler
    revision uint64
    publishedRevision uint64
    rebuilds uint64
}

// NewP35EpochRouter constructs an empty synchronized registration surface.
// Constructor publication is not counted toward maintenance rebuilds.
func NewP35EpochRouter(next http.Handler) *P35EpochRouter {
    if next==nil {next=http.NotFoundHandler()}
    p:=&P35EpochRouter{next:next,registry:make(HeaderRouter)}
    p.published=p.registry.Handler(next)
    return p
}

func (p *P35EpochRouter) publishLocked(){
    frozen:=make(HeaderRouter,len(p.registry))
    for header,routes:=range p.registry {
        copyRoutes:=make([]HeaderRoute,len(routes))
        copy(copyRoutes,routes)
        for i:=range copyRoutes {
            copyRoutes[i].MatchAny=append([]Pattern(nil),copyRoutes[i].MatchAny...)
        }
        frozen[header]=copyRoutes
    }
    p.published=frozen.Handler(p.next)
    p.publishedRevision=p.revision
    p.rebuilds++
}

func (p *P35EpochRouter) updatedLocked(){
    p.revision++
    // Lazy policy: leave the old immutable snapshot active until ServeHTTP.
}

func (p *P35EpochRouter) Register(header,match string,wrap func(http.Handler) http.Handler){
    p.mu.Lock()
    defer p.mu.Unlock()
    p.registry.Route(header,match,wrap)
    p.updatedLocked()
}
func (p *P35EpochRouter) RegisterAny(header string,matches []string,wrap func(http.Handler) http.Handler){
    p.mu.Lock()
    defer p.mu.Unlock()
    p.registry.RouteAny(header,matches,wrap)
    p.updatedLocked()
}
func (p *P35EpochRouter) RegisterDefault(wrap func(http.Handler) http.Handler){
    p.mu.Lock()
    defer p.mu.Unlock()
    p.registry.RouteDefault(wrap)
    p.updatedLocked()
}

// Snapshot selection and registration both linearize under mu. User
// handlers run WITHOUT holding mu, avoiding registration re-entrancy deadlock.
func (p *P35EpochRouter) ServeHTTP(w http.ResponseWriter,r *http.Request){
    p.mu.Lock()
    if p.publishedRevision!=p.revision {p.publishLocked()}
    h:=p.published
    p.mu.Unlock()
    h.ServeHTTP(w,r)
}

func (p *P35EpochRouter) Stats()(revision,published,rebuilds uint64){
    p.mu.Lock()
    defer p.mu.Unlock()
    return p.revision,p.publishedRevision,p.rebuilds
}
