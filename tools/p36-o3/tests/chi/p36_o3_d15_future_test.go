package middleware

import "testing"

// Separate sealed future-demand oracle. It is NOT required to pass D14.
// It is not a test of every future repair grammar.
func TestP36O3D15RestoreOriginalClosure(t *testing.T){
 for _,label:=range []string{"alpha","beta"} {
  t.Run(label,func(t *testing.T){
   p:=p36O3Case(label)
   if !p.DisableRoute("X-P35-O3","target"){t.Fatal("setup disable failed")}
   if got:=p36O3Got(p,"target");got!="secondary"{t.Fatalf("post-disable expected secondary got %q",got)}
   if !p.EnableRoute("X-P35-O3","target") {
    t.Fatalf("P36_O3_D15_RESTORE_EXPECTED_NEGATIVE_OR_BUG world=%s: no retained original closure",label)
   }
   if got:=p36O3Got(p,"target");got!=label {
    t.Fatalf("P36_O3_D15_RESTORE_EXPECTED_NEGATIVE_OR_BUG world=%s: got %q want %q",label,got,label)
   }
  })
 }
}
