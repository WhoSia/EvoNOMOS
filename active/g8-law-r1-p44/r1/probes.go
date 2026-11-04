package r1

// The six-probe set was declared in P43 before the first original Chi CI run.
// The broad probes were originally exploratory: they are NOT an independent
// prospective holdout for P44. These distinctions must be disclosed.
var Narrow=[]Probe{
 {"GET","/items/alpha"},{"HEAD","/items/alpha"},
 {"GET","/items/123"},{"HEAD","/items/123"},
 {"GET","/items/"},{"GET","/items/alpha/"},
}
var ExploratoryFromP43=[]Probe{
 {"POST","/items/alpha"},{"OPTIONS","/items/alpha"},
 {"GET","/items/a%2Fb"},{"GET","/items/%61lpha"},
 {"HEAD","/items/a%2Fb"},{"GET","/items/%2e%2e"},
}
func Broad() []Probe {
 out:=append([]Probe{},Narrow...)
 return append(out,ExploratoryFromP43...)
}
