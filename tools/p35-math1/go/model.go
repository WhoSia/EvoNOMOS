package math1

type Action string
const (
 Tick Action = "tick"
 Noop Action = "noop"
)

var Alphabet = []Action{Tick,Noop}

type Machine struct {
 Step [2][2]bool
 Out [2]bool
}

func bit(b bool) int {if b{return 1};return 0}
func actionIndex(a Action) int {if a==Tick{return 0};return 1}

func (m Machine) Run(s bool, word []Action) bool {
 for _,a:=range word{s=m.Step[actionIndex(a)][bit(s)]}
 return s
}
func (m Machine) Observe(s bool,word []Action)bool{return m.Out[bit(m.Run(s,word))]}

func Toggle() Machine {return Machine{
 Step:[2][2]bool{{true,false},{false,true}},
 Out:[2]bool{false,true},
}}
func Stutter() Machine {return Machine{
 Step:[2][2]bool{{false,true},{false,true}},
 Out:[2]bool{false,true},
}}
func Silent()Machine{return Machine{
 Step:[2][2]bool{{false,true},{false,true}},
 Out:[2]bool{false,false},
}}

func Words(k int)[][]Action{
 result:=[][]Action{{}}
 layer:=[][]Action{{}}
 for length:=1;length<=k;length++{
  next:=make([][]Action,0,len(layer)*len(Alphabet))
  for _,w:=range layer{
   for _,a:=range Alphabet{
    v:=append(append([]Action{},w...),a)
    next=append(next,v)
   }
  }
  result=append(result,next...)
  layer=next
 }
 return result
}

func EqUpTo(k int,a Machine,sa bool,b Machine,sb bool)bool{
 for _,w:=range Words(k){
  if a.Observe(sa,w)!=b.Observe(sb,w){return false}
 }
 return true
}

func ShortestSeparator(k int,a Machine,sa bool,b Machine,sb bool)([]Action,bool){
 for _,w:=range Words(k){if a.Observe(sa,w)!=b.Observe(sb,w){return w,true}}
 return nil,false
}

type Pair struct{Left,Right bool}
func PairObserve(left,env Machine,sl,se bool,word []Action)Pair{
 return Pair{left.Observe(sl,word),env.Observe(se,word)}
}
func IndependentProductEq(k int,a Machine,sa bool,b Machine,sb bool,e Machine,se bool)bool{
 for _,w:=range Words(k){if PairObserve(a,e,sa,se,w)!=PairObserve(b,e,sb,se,w){return false}}
 return true
}

func AllMachines(limit int)[]Machine{
 if limit<0||limit>64{panic("bound range 0..64")}
 res:=make([]Machine,0,limit)
 for n:=0;n<limit;n++{
  m:=Machine{}
  for o:=0;o<2;o++{m.Out[o]=(n>>(o))&1!=0}
  for i:=0;i<2;i++{for o:=0;o<2;o++{m.Step[i][o]=(n>>(2+i*2+o))&1!=0}}
  res=append(res,m)
 }
 return res
}

// Exhaustively check a finite, explicitly bounded family; NOT a proof
// of the universal Lean theorem.
func CheckSmallProducts(k,modelLimit int)(int,int){
 machines:=AllMachines(modelLimit)
 cases:=0;violations:=0
 for _,a:=range machines{for _,b:=range machines{
  for _,sa:=range []bool{false,true}{for _,sb:=range []bool{false,true}{
   if !EqUpTo(k,a,sa,b,sb){continue}
   for _,e:=range machines{for _,se:=range []bool{false,true}{
    cases++
    if !IndependentProductEq(k,a,sa,b,sb,e,se){violations++}
   }}
  }}
 }}
 return cases,violations
}

type Receipt struct{
 TraceDepth int `json:"trace_depth"`
 FirstSeparator []Action `json:"first_separator"`
 FirstLength int `json:"first_length"`
 DepthZeroEqual bool `json:"depth_zero_equal"`
 DepthOneEqual bool `json:"depth_one_equal"`
 HiddenOutputEqualUpToThree bool `json:"hidden_output_equal_up_to_three"`
 StateProbeSeparatesAtEmpty bool `json:"state_probe_separates_at_empty"`
 ProductCases int `json:"product_cases"`
 ProductViolations int `json:"product_violations"`
}

func Evaluate()Receipt{
 w,ok:=ShortestSeparator(3,Toggle(),false,Stutter(),false)
 if !ok {w=[]Action{}}
 count,violation:=CheckSmallProducts(2,16)
 return Receipt{
 TraceDepth:3,FirstSeparator:w,FirstLength:len(w),
 DepthZeroEqual:EqUpTo(0,Toggle(),false,Stutter(),false),
 DepthOneEqual:EqUpTo(1,Toggle(),false,Stutter(),false),
 HiddenOutputEqualUpToThree:EqUpTo(3,Silent(),false,Silent(),true),
 StateProbeSeparatesAtEmpty:false!=true,
 ProductCases:count,ProductViolations:violation,
 }
}
