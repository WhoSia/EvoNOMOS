package fixture

type Left struct { Value string }
func Legacy() string { return "old" }
func FutureA() string {
 p := &Left{Value: "a0"}
 return p.Value
}
