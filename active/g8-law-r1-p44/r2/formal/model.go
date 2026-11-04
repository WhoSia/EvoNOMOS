package formal
import "math/bits"
// Three independently authorized application route edits, one per named demand.
// The state and goal are bitsets of already fulfilled demands; invalid bits reject.
func CostFromState(state,goal,rights uint8)(int,bool){
 const allowed=uint8(0b111)
 if state & ^allowed!=0||goal & ^allowed!=0||rights & ^allowed!=0{return 0,false}
 missing:=goal &^ state
 if missing &^ rights !=0{return 0,false}
 return bits.OnesCount8(missing),true
}
func PredictedCost(stage int)(int,int){return stage,3+stage}
