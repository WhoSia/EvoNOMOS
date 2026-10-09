// Package archive is owner B's typed historical store and optional reader.
// It is project-written code, not an upstream gjson implementation.
package archive

import (
 "errors"
 "fmt"
 "sync"

 "github.com/tidwall/gjson"
)

var ErrNoOriginal=errors.New("historical input lexeme not retained")

type Event struct { ID int; Original []byte }
type Store struct { mu sync.RWMutex; entries []Event }
func New()*Store{return &Store{}}
func (s *Store) AppendSemantic(id int,raw []byte){
 s.mu.Lock();defer s.mu.Unlock()
 s.entries=append(s.entries,Event{ID:id,Original:append([]byte(nil),raw...)})
}
func (s *Store) State()(id int, revision int){
 s.mu.RLock();defer s.mu.RUnlock()
 if len(s.entries)>0 {id=s.entries[len(s.entries)-1].ID}
 return id,len(s.entries)
}
func (s *Store) EventAt(n int)(Event,error){
 s.mu.RLock();defer s.mu.RUnlock()
 if n<0||n>=len(s.entries){return Event{},fmt.Errorf("index out of range: %d",n)}
 e:=s.entries[n]
 return Event{ID:e.ID,Original:append([]byte(nil),e.Original...)},nil
}
func (s *Store) OriginalKeyAt(n int)(string,error){
 e,err:=s.EventAt(n);if err!=nil{return "",err}
 if len(e.Original)==0{return "",ErrNoOriginal}
 var lexeme string
 var found bool
 var bad error
 obj:=gjson.ParseBytes(e.Original)
 if !obj.IsObject(){return "",fmt.Errorf("historical root not object")}
 obj.ForEach(func(k,v gjson.Result)bool{
  if k.Str!="id"{return true}
  if v.Type!=gjson.Number{bad=fmt.Errorf("historical id is not number");return false}
  lexeme=k.Raw;found=true
  return false
 })
 if bad!=nil{return "",bad}
 if !found{return "",fmt.Errorf("historical id missing")}
 return lexeme,nil
}
