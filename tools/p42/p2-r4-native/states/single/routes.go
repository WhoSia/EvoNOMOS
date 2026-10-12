package single

import (
  "net/http"
  echo "github.com/labstack/echo/v4"
)
func health(c echo.Context) error {return c.String(http.StatusOK,"health")}
func verb(c echo.Context) error {
 c.Response().Header().Set("X-Evo-Route","verb")
 return c.String(http.StatusOK,"new:"+c.Param("name"))
}
func legacy(c echo.Context) error {
 c.Response().Header().Set("X-Evo-Route","legacy")
 return c.String(http.StatusOK,"legacy:"+c.Param("name"))
}
func Build() *echo.Echo {
 e:=echo.New()
 e.GET("/health",health)
 e.GET(`/r/:name\:cancel`,verb)
 return e
}
