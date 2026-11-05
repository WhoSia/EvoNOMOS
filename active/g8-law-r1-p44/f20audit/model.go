package f20audit

import (
 "errors"
 "regexp"
 "time"
)

type ObserverKind string
const (
 RoutePattern ObserverKind="route-pattern"
 AllowedMethodsHelper ObserverKind="internal-allowed-methods"
 InternalPanic ObserverKind="internal-panic-text"
)
type OriginalCase struct {
 ID string
 Repo string
 ParentSHA string
 FixedSHA string
 AuthoredUTC string
 CommitSubject string
 Observer ObserverKind
 Input string
 Before string
 After string
 OriginalJobID int64
 PublicAPI bool
 SubjectDisclosedBeforeOracle bool
}
var ErrEvidence=errors.New("invalid historical original source evidence")
var hexCommit=regexp.MustCompile(`^[a-f0-9]{40}$`)

func (c OriginalCase) Validate() error {
 if c.ID==""||c.Repo==""||c.Input==""||c.CommitSubject==""||
 !hexCommit.MatchString(c.ParentSHA)||!hexCommit.MatchString(c.FixedSHA)||
 c.ParentSHA==c.FixedSHA||c.Before==c.After||c.OriginalJobID<=0{
  return ErrEvidence
 }
 if _,err:=time.Parse(time.RFC3339,c.AuthoredUTC);err!=nil{return ErrEvidence}
 switch c.Observer {
 case RoutePattern:
  if !c.PublicAPI{return ErrEvidence}
 case AllowedMethodsHelper,InternalPanic:
  if c.PublicAPI{return ErrEvidence}
 default:return ErrEvidence
 }
 return nil
}
