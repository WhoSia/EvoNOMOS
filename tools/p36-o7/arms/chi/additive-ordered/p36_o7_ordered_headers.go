// P36-O7B additive, opt-in chronological header routing inside
// go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00.
// This is a research-authored original-module extension, NOT preexisting upstream Chi.
// The legacy exported HeaderRouter map type and functions stay unchanged.
package middleware

import (
 "net/http"
 "strings"
)

type p36O7OrderedEntry struct {
 header string
 route HeaderRoute
}

// P36O7OrderedHeaderRouter stores cross-header registration chronology.
// It is configured before Handler publication; concurrent mutation is excluded.
type P36O7OrderedHeaderRouter struct {
 entries []p36O7OrderedEntry
 defaultMiddleware func(http.Handler)http.Handler
}

func P36O7NewOrderedHeaderRouter()*P36O7OrderedHeaderRouter{
 return &P36O7OrderedHeaderRouter{}
}

func (o *P36O7OrderedHeaderRouter)Route(header,match string,middleware func(http.Handler)http.Handler)*P36O7OrderedHeaderRouter{
 o.entries=append(o.entries,p36O7OrderedEntry{
   header:strings.ToLower(header),
   route:HeaderRoute{MatchOne:NewPattern(match),Middleware:middleware},
 })
 return o
}

func (o *P36O7OrderedHeaderRouter)RouteAny(header string,matches []string,middleware func(http.Handler)http.Handler)*P36O7OrderedHeaderRouter{
 patterns:=make([]Pattern,0,len(matches))
 for _,m:=range matches{patterns=append(patterns,NewPattern(m))}
 o.entries=append(o.entries,p36O7OrderedEntry{
   header:strings.ToLower(header),
   route:HeaderRoute{MatchAny:patterns,Middleware:middleware},
 })
 return o
}

func (o *P36O7OrderedHeaderRouter)RouteDefault(middleware func(http.Handler)http.Handler)*P36O7OrderedHeaderRouter{
 o.defaultMiddleware=middleware
 return o
}

func(o *P36O7OrderedHeaderRouter)Handler(next http.Handler)http.Handler{
 if next==nil {next=http.NotFoundHandler()}
 frozen:=make([]p36O7OrderedEntry,len(o.entries))
 copy(frozen,o.entries)
 for i:=range frozen{frozen[i].route.MatchAny=append([]Pattern(nil),frozen[i].route.MatchAny...)}
 def:=o.defaultMiddleware
 return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
   for _,entry:=range frozen{
     value:=r.Header.Get(entry.header)
     if value==""{continue}
     value=strings.ToLower(value)
     if entry.route.IsMatch(value){
       entry.route.Middleware(next).ServeHTTP(w,r)
       return
     }
   }
   if def!=nil{def(next).ServeHTTP(w,r);return}
   next.ServeHTTP(w,r)
 })
}
