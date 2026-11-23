// Package ownercomposition checks composition of independently maintained
// app-owned flag specifications against the original pinned pflag dependency.
// It does not modify or make claims about ownership of the upstream repository.
package ownercomposition

import (
 "fmt"
 "io"

 "github.com/spf13/pflag"
)

type Owner struct {
 Flags *pflag.FlagSet
 Tenant *string
 Channel *string
}

func NewOwner(owner string, newDemand bool) Owner {
 f := pflag.NewFlagSet(owner,pflag.ContinueOnError)
 f.SetOutput(io.Discard)
 o := Owner{Flags:f}
 o.Tenant=f.String("tenant-"+owner,"","original independent tenant field")
 if newDemand {o.Channel=f.String("channel",owner+"default","new independent owner-local channel")}
 return o
}

func SharedMerge(a,b Owner) *pflag.FlagSet {
 shared:=pflag.NewFlagSet("shared",pflag.ContinueOnError)
 shared.SetOutput(io.Discard)
 shared.AddFlagSet(a.Flags) // original AddFlagSet intentionally skips duplicate names
 shared.AddFlagSet(b.Flags)
 return shared
}

// CheckedMerge is the conventional normalized-name guard competitor. It
// abstains/refuses conflicting integrations instead of silently dropping B.
func CheckedMerge(a,b Owner) (*pflag.FlagSet,error) {
 shared:=pflag.NewFlagSet("checked",pflag.ContinueOnError)
 shared.SetOutput(io.Discard)
 var duplicate string
 for _,owner:=range []Owner{a,b}{
  owner.Flags.VisitAll(func(flag *pflag.Flag){
   if shared.Lookup(flag.Name)!=nil {duplicate=flag.Name;return}
   shared.AddFlag(flag)
  })
  if duplicate!="" {return nil,fmt.Errorf("owner flag-name collision: %s",duplicate)}
 }
 return shared,nil
}

// DirectRegister uses the original AddFlag API; it panics on duplicate names.
// Calling tests recover from panic only to classify the source failure.
func DirectRegister(a,b Owner) *pflag.FlagSet {
 shared:=pflag.NewFlagSet("direct",pflag.ContinueOnError)
 shared.SetOutput(io.Discard)
 for _,owner:=range []Owner{a,b}{
  owner.Flags.VisitAll(func(flag *pflag.Flag){shared.AddFlag(flag)})
 }
 return shared
}

// PrefixRename is a strong app-owned namespace construction rival. Each
// owner retains its distinct local channel semantics.
func PrefixRename(newDemand bool) (f *pflag.FlagSet, tenantA,tenantB,chanA,chanB *string) {
 f=pflag.NewFlagSet("prefix",pflag.ContinueOnError)
 f.SetOutput(io.Discard)
 tenantA=f.String("tenant-a","","old client A")
 tenantB=f.String("tenant-b","","old client B")
 if newDemand {
  chanA=f.String("a-channel","Adefault","independent A channel")
  chanB=f.String("b-channel","Bdefault","independent B channel")
 }
 return
}
