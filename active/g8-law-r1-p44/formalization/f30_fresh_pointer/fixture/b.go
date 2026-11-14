package fixture

type Right struct { Value string }
func FutureB() string {
 p := &Right{Value: "b0"}
 return p.Value
}
