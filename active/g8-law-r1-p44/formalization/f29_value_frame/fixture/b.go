package fixture

type Right struct { Value string }
func FutureB() string { return (Right{Value: "b0"}).Value }
