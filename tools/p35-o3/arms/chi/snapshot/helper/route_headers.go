package middleware

import (
	"encoding/csv"
	"io"
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

// p35P7Group is an immutable compilation of one registered header group.
// Route/rule slices are copied so later sequential modifications are not
// visible to an already-constructed handler.
type p35P7Group struct {
	header string
	matchers []HeaderRoute
}

func (hr HeaderRouter) Handler(next http.Handler) http.Handler {
	groups := make([]p35P7Group, 0, len(hr))
	for key, registered := range hr {
		if key == "*" { continue }
		copyMatchers := make([]HeaderRoute, len(registered))
		for i, m := range registered {
			copyMatchers[i] = m
			copyMatchers[i].MatchAny = append([]Pattern(nil), m.MatchAny...)
		}
		groups = append(groups, p35P7Group{header:key, matchers:copyMatchers})
	}
	sort.Slice(groups, func(i, j int) bool { return groups[i].header < groups[j].header })
	var fallback func(next http.Handler) http.Handler
	if defaults:=hr["*"]; len(defaults)>0 { fallback=defaults[0].Middleware }
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		var firstWildcard func(next http.Handler) http.Handler
		for _, group := range groups {
			values := r.Header.Values(group.header)
			if len(values) == 0 { continue }
			for _, matcher := range group.matchers {
				strength := p35Math2BestMatch(matcher,values,true,strings.EqualFold(group.header,"X-EvoNOMOS-Mode"))
				if strength==0 {continue}
				if strength==2 {matcher.Middleware(next).ServeHTTP(w,r);return}
				if firstWildcard==nil {firstWildcard=matcher.Middleware}
				break
			}
		}
		if firstWildcard!=nil {firstWildcard(next).ServeHTTP(w,r);return}
		if fallback != nil {
			fallback(next).ServeHTTP(w, r)
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
func p35Math2BestMatch(rule HeaderRoute, values []string, comma bool, researchHeader bool) int {
	best:=0
	for _,raw:=range values {
		tokens:=[]string{raw}
		if comma {
			if researchHeader {
				reader:=csv.NewReader(strings.NewReader(raw))
				reader.FieldsPerRecord=-1
				reader.TrimLeadingSpace=true
				var err error
				tokens,err=reader.Read()
				if err!=nil {continue}
				if _,err=reader.Read();err!=io.EOF {continue}
			} else {tokens=strings.Split(raw,",")}
		}
		for _,token:=range tokens {
			if comma {token=strings.TrimSpace(token)}
			s:=p35P7MatchStrength(rule,strings.ToLower(token))
			if s>best {best=s}
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
