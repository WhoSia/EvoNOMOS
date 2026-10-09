package middleware

import (
	"net/http"
	"sort"
	"strings"
)

// RouteHeaders is a neat little header-based router that allows you to direct
// the flow of a request through a middleware stack based on a request header.
//
// For example, lets say you'd like to setup multiple routers depending on the
// request Host header, you could then do something as so:
//
//	r := chi.NewRouter()
//	rSubdomain := chi.NewRouter()
//	r.Use(middleware.RouteHeaders().
//		Route("Host", "example.com", middleware.New(r)).
//		Route("Host", "*.example.com", middleware.New(rSubdomain)).
//		Handler)
//	r.Get("/", h)
//	rSubdomain.Get("/", h2)
//
// Another example, imagine you want to setup multiple CORS handlers, where for
// your origin servers you allow authorized requests, but for third-party public
// requests, authorization is disabled.
//
//	r := chi.NewRouter()
//	r.Use(middleware.RouteHeaders().
//		Route("Origin", "https://app.skyweaver.net", cors.Handler(cors.Options{
//			AllowedOrigins:   []string{"https://api.skyweaver.net"},
//			AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
//			AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type"},
//			AllowCredentials: true, // <----------<<< allow credentials
//		})).
//		Route("Origin", "*", cors.Handler(cors.Options{
//			AllowedOrigins:   []string{"*"},
//			AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
//			AllowedHeaders:   []string{"Accept", "Content-Type"},
//			AllowCredentials: false, // <----------<<< do not allow credentials
//		})).
//		Handler)
func RouteHeaders() HeaderRouter {
	return HeaderRouter{}
}

type HeaderRouter map[string][]HeaderRoute

func (hr HeaderRouter) Route(header, match string, middlewareHandler func(next http.Handler) http.Handler) HeaderRouter {
	header = strings.ToLower(header)
	k := hr[header]
	if k == nil {
		hr[header] = []HeaderRoute{}
	}
	hr[header] = append(hr[header], HeaderRoute{MatchOne: NewPattern(match), Middleware: middlewareHandler})
	return hr
}

func (hr HeaderRouter) RouteAny(header string, match []string, middlewareHandler func(next http.Handler) http.Handler) HeaderRouter {
	header = strings.ToLower(header)
	k := hr[header]
	if k == nil {
		hr[header] = []HeaderRoute{}
	}
	patterns := []Pattern{}
	for _, m := range match {
		patterns = append(patterns, NewPattern(m))
	}
	hr[header] = append(hr[header], HeaderRoute{MatchAny: patterns, Middleware: middlewareHandler})
	return hr
}

func (hr HeaderRouter) RouteDefault(handler func(next http.Handler) http.Handler) HeaderRouter {
	hr["*"] = []HeaderRoute{{Middleware: handler}}
	return hr
}

func (hr HeaderRouter) Handler(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if len(hr) == 0 {
			next.ServeHTTP(w, r)
			return
		}
		// Read the actual mutable registry on each request. Stable header
		// precedence is lexical; registration order is retained per header.
		keys := make([]string, 0, len(hr))
		for header := range hr {
			if header != "*" { keys = append(keys, header) }
		}
		sort.Strings(keys)
		var firstWildcard func(next http.Handler) http.Handler
		for _, header := range keys {
			values := r.Header.Values(header)
			if len(values) == 0 { continue }
			for _, matcher := range hr[header] {
				strength := p35Math2BestMatch(matcher,values,true)
                if header=="x-evonomos-mode" { strength=p35O3Match(matcher,values) }
				if strength==0 {continue}
				if strength==2 {matcher.Middleware(next).ServeHTTP(w,r);return}
				if firstWildcard==nil {firstWildcard=matcher.Middleware}
				break
			}
		}
		if firstWildcard!=nil {firstWildcard(next).ServeHTTP(w,r);return}
		if fallback := hr["*"]; len(fallback) > 0 && fallback[0].Middleware != nil {
			fallback[0].Middleware(next).ServeHTTP(w, r)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func p35P7MatchStrength(rule HeaderRoute, value string) int {
	if len(rule.MatchAny)>0 {
		strength:=0
		for _,p:=range rule.MatchAny {
			if p.Match(value) {
				if !p.wildcard {return 2}
				strength=1
			}
		}
		return strength
	}
	if !rule.MatchOne.Match(value) {return 0}
	if rule.MatchOne.wildcard {return 1}
	return 2
}

// p35Math2BestMatch explicitly evaluates all physical field values and,
// when enabled, every unquoted comma token. It preserves registered-route
// priority by returning one strength for the current registered route.
func p35Math2BestMatch(rule HeaderRoute, values []string, comma bool) int {
	best:=0
	for _,raw:=range values {
		tokens:=[]string{raw}
		if comma {tokens=strings.Split(raw,",")}
		for _,token:=range tokens {
			if comma {token=strings.TrimSpace(token)}
			s:=p35P7MatchStrength(rule,strings.ToLower(token))
			if s>best {best=s}
		}
	}
	return best
}


// p35O3ResearchTokens is an independent finite-state field scanner.
// It rejects malformed quoting atomically at the physical-field boundary.
func p35O3ResearchTokens(raw string)([]string,bool){
    result:=[]string{}
    const (start=0;bare=1;quoted=2;afterQuoted=3)
    state:=start
    var token strings.Builder
    push:=func(){v:=strings.TrimSpace(token.String());if v!=""{result=append(result,v)};token.Reset()}
    for i:=0;i<len(raw);i++{
        c:=raw[i]
        switch state {
        case start:
            switch c {
            case ' ', '\t': continue
            case ',': continue
            case '"': state=quoted
            default: token.WriteByte(c);state=bare
            }
        case bare:
            if c=='"' {return nil,false}
            if c==',' {push();state=start;continue}
            token.WriteByte(c)
        case quoted:
            if c=='"' {
                if i+1<len(raw)&&raw[i+1]=='"' {token.WriteByte('"');i++} else {state=afterQuoted}
            } else {token.WriteByte(c)}
        case afterQuoted:
            if c==',' {push();state=start;continue}
            if c!=' '&&c!='\t' {return nil,false}
        }
    }
    if state==quoted {return nil,false}
    push()
    return result,true
}

func p35O3Match(rule HeaderRoute, values []string) int {
    best:=0
    for _,raw:=range values{
        tokens,ok:=p35O3ResearchTokens(raw)
        if !ok {continue}
        for _,token:=range tokens{
            strength:=p35P7MatchStrength(rule,strings.ToLower(token))
            if strength>best {best=strength}
        }
    }
    return best
}

type HeaderRoute struct {
	Middleware func(next http.Handler) http.Handler
	MatchOne   Pattern
	MatchAny   []Pattern
}

func (r HeaderRoute) IsMatch(value string) bool {
	if len(r.MatchAny) > 0 {
		for _, m := range r.MatchAny {
			if m.Match(value) {
				return true
			}
		}
	} else if r.MatchOne.Match(value) {
		return true
	}
	return false
}

type Pattern struct {
	prefix   string
	suffix   string
	wildcard bool
}

func NewPattern(value string) Pattern {
	p := Pattern{}
	if i := strings.IndexByte(value, '*'); i >= 0 {
		p.wildcard = true
		p.prefix = value[0:i]
		p.suffix = value[i+1:]
	} else {
		p.prefix = value
	}
	return p
}

func (p Pattern) Match(v string) bool {
	if !p.wildcard {
		return p.prefix == v
	}
	return len(v) >= len(p.prefix+p.suffix) && strings.HasPrefix(v, p.prefix) && strings.HasSuffix(v, p.suffix)
}
