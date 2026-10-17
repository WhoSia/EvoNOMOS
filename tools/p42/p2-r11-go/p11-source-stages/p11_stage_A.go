package gin

// EvoNOMOS-owned application-fixture source only.
// Each stage is copied separately into the unmodified pinned Gin checkout.
const evonomosP11Stage = "A"
const evonomosP11HasA = true
const evonomosP11HasB = false

func evonomosP11Install(router *Engine) {
    router.GET("/a", func(c *Context) { c.String(200, "A") })
}
