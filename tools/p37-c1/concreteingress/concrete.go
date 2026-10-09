// Package concreteingress is a post-C1 negative control: its public constructor
// directly requires the CONCRETE archive.Store, a high-level to low-level
// source dependency under the frozen static DIP predicate.
package concreteingress

import (
 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/archive"
 "github.com/WhoSia/EvoNOMOS/tools/p37-c1/ingress"
)
func New(store *archive.Store)*ingress.Component{
 // Retaining original provenance is permitted even with this concrete dependency.
 return ingress.New(store,true)
}
