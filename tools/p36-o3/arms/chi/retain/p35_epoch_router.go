// P35-O6 research-only source extension to the pinned original Chi module.
// Matched API, distinct publication timing; direct external HeaderRouter
// map writes are intentionally excluded from the synchronization contract.
package middleware

import (
    "net/http"
    "sync"
    "strings"
)

type p36O3DisabledRoute struct { index int; route HeaderRoute }

type P35EpochRouter struct {
    disabled map[string][]p36O3DisabledRoute
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
    p.publishLocked()
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
    // Eager policy already published every completed registration.
    h:=p.published
    p.mu.Unlock()
    h.ServeHTTP(w,r)
}

func (p *P35EpochRouter) Stats()(revision,published,rebuilds uint64){
    p.mu.Lock()
    defer p.mu.Unlock()
    return p.revision,p.publishedRevision,p.rebuilds
}

 // D14: remove only the first registered enabled exact-match rule.
 // No support for wildcard or RouteAny removal in this scoped experiment.
func(p *P35EpochRouter) DisableRoute(header,match string)bool {
    p.mu.Lock()
    defer p.mu.Unlock()
    header=strings.ToLower(header)
    match=strings.ToLower(match)
    routes:=p.registry[header]
    for i,route:=range routes{
        if len(route.MatchAny)!=0 || route.MatchOne.wildcard || route.MatchOne.prefix!=match {continue}
        
        if p.disabled==nil {p.disabled=make(map[string][]p36O3DisabledRoute)}
        key:=header+"\x00"+match
        p.disabled[key]=append(p.disabled[key],p36O3DisabledRoute{index:i,route:route})
        
        keep:=make([]HeaderRoute,0,len(routes)-1)
        keep=append(keep,routes[:i]...)
        keep=append(keep,routes[i+1:]...)
        p.registry[header]=keep
        p.updatedLocked()
        return true
    }
    return false
}

// D15 was frozen as a separate future demand BEFORE writing these D14 arms.
// This method is not required to work for D14 acceptance.
func(p *P35EpochRouter) EnableRoute(header,match string)bool {
    
    p.mu.Lock()
    defer p.mu.Unlock()
    header=strings.ToLower(header)
    match=strings.ToLower(match)
    key:=header+"\x00"+match
    entries:=p.disabled[key]
    if len(entries)==0{return false}
    entry:=entries[0]
    if len(entries)==1 {delete(p.disabled,key)} else {p.disabled[key]=entries[1:]}
    routes:=p.registry[header]
    i:=entry.index
    if i>len(routes){i=len(routes)}
    newRoutes:=make([]HeaderRoute,0,len(routes)+1)
    newRoutes=append(newRoutes,routes[:i]...)
    newRoutes=append(newRoutes,entry.route)
    newRoutes=append(newRoutes,routes[i:]...)
    p.registry[header]=newRoutes
    p.updatedLocked()
    return true
    
}
