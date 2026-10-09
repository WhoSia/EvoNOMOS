package math2

type Step string
type State string

const (
 A Step = "a"
 B Step = "b"
 Zero State = "zero"
 One State = "one"
 Two State = "two"
 Three State = "three"
 Four State = "four"
)

type Edge struct{Demand Step; From, To State}
var Edges=[]Edge{
 {A,Zero,One},{A,Two,Four},
 {B,Zero,Two},{B,One,Three},
}
func Successors(d Step,from State)[]State{
 out:=[]State{}
 for _,e:=range Edges{if e.Demand==d&&e.From==from{out=append(out,e.To)}}
 return out
}
func Reach2(first,second Step,start State)[]State{
 out:=[]State{}
 for _,mid:=range Successors(first,start){out=append(out,Successors(second,mid)...)}
 return out
}
func Contains[T comparable](xs []T,x T)bool{for _,a:=range xs{if a==x{return true}};return false}

type Patch string
const(
 Inline Patch="inline"
 Helper Patch="helper"
)
var Admissible=[]Patch{Inline,Helper}
func MayHelper()bool{return Contains(Admissible,Helper)}
func MustHelper()bool{
 if len(Admissible)==0{return false}
 for _,p:=range Admissible{if p!=Helper{return false}}
 return true
}
type Receipt struct{
 AdmissiblePatches []Patch `json:"admissible_patches"`
 MayHelper bool `json:"may_helper"`
 MustHelper bool `json:"must_helper"`
 AB []State `json:"ab"`
 BA []State `json:"ba"`
 PathsCommute bool `json:"paths_commute"`
}
func Evaluate()Receipt{
 ab:=Reach2(A,B,Zero);ba:=Reach2(B,A,Zero)
 return Receipt{append([]Patch{},Admissible...),MayHelper(),MustHelper(),ab,ba,
  len(ab)==len(ba)&&len(ab)==1&&ab[0]==ba[0]}
}
