//go:build p41_negative_provider
package invalidprovider

import echo "github.com/labstack/echo/v5"

// Go compiling this sub-package with -tags p41_negative_provider MUST fail
// against the ORIGINAL Echo Router interface because this provider lacks Route.
// All the other required Router methods are present with exact real signatures.
type Incomplete struct{}
func (*Incomplete) Add(echo.Route) (echo.RouteInfo,error) {return echo.RouteInfo{},nil}
func (*Incomplete) Remove(string,string)error{return nil}
func (*Incomplete) Routes() echo.Routes{return nil}
var _ echo.Router = (*Incomplete)(nil)
