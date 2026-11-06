package fixture

type Left struct { Value string }
func Legacy() string { return "old" }
func FutureA() string { return (Left{Value: "a0"}).Value }
