package math0

type Design uint8

const (
    Live Design = iota
    Snapshot
)

type World struct {
    AtConstruction bool `json:"at_construction"`
    Current bool `json:"current"`
}

func Initial(b bool) World { return World{AtConstruction: b, Current: b} }
func Update(w World) World { w.Current = !w.Current; return w }

func Observe(d Design, w World) bool {
    if d == Live { return w.Current }
    return w.AtConstruction
}

type Countermodel struct {
    Start bool `json:"start"`
    InitialAgreement bool `json:"initial_agreement"`
    LaterDisagreement bool `json:"later_disagreement"`
}

func Enumerate() []Countermodel {
    output := make([]Countermodel,0,2)
    for _,b:=range []bool{false,true}{
        w:=Initial(b)
        later:=Update(w)
        output=append(output,Countermodel{
          Start:b,
          InitialAgreement:Observe(Live,w)==Observe(Snapshot,w),
          LaterDisagreement:Observe(Live,later)!=Observe(Snapshot,later),
        })
    }
    return output
}
