package f20audit

import "errors"

// This is a type-check for claims, NOT proof that one test covers a public API.
var ErrScopePromotion=errors.New("attempted to upgrade internal helper evidence to public API guarantee")
type ClaimScope string
const (
 SameTestInput ClaimScope="same-original-test-input"
 EntirePublicAPI ClaimScope="entire-public-API"
 CompleteClientContexts ClaimScope="all-client-contexts"
)
func CanSupport(c OriginalCase,claim ClaimScope)error{
 if err:=c.Validate();err!=nil{return err}
 if claim==SameTestInput{return nil}
 // No F20 cohort fixture ever established complete exported API coverage,
 // even if it called an exported method. No upgrade from one trace.
 return ErrScopePromotion
}
