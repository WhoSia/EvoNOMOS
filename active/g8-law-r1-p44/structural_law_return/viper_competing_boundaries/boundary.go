package boundaries

import (
  "os"
  "strings"

  "github.com/spf13/viper"
)

// This restricted app-owned study assumes one known environment variable.
// It does not implement Viper's full precedence/aliases/BindEnv semantics.
const envName = "APP_SERVICE_TOKEN"
const key = "service.token"

type Source uint8
const (
 File Source = iota
 Environment
)
type Record struct {
 Value string
 ID int
 source Source
 captured bool
}
func Config() (*viper.Viper,error) {
 v:=viper.New()
 v.SetConfigType("yaml")
 if err:=v.ReadConfig(strings.NewReader("service:\n  token: same-token\n"));err!=nil{return nil,err}
 v.SetEnvPrefix("APP")
 v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
 v.AutomaticEnv()
 return v,nil
}
func currentSource() Source {
 if _,ok:=os.LookupEnv(envName);ok{return Environment}
 return File
}
type Lazy struct{}
func (Lazy) Read(v *viper.Viper) Record {return Record{Value:v.GetString(key)}}
func (Lazy) GuessHistorical(_ Record) Source {return currentSource()}
func (Lazy) OriginNow() Source {return currentSource()}

type Snapshot struct{}
func (Snapshot) Read(v *viper.Viper) Record {
 return Record{Value:v.GetString(key),source:currentSource(),captured:true}
}
func (Snapshot) Historical(r Record) (Source,bool) {return r.source,r.captured}
func (Snapshot) OriginNow() Source {return currentSource()}

type Journal struct {
 next int
 events map[int]Source
}
func NewJournal() *Journal{return &Journal{events:make(map[int]Source)}}
func (j *Journal) Read(v *viper.Viper) Record {
 j.next++
 j.events[j.next]=currentSource()
 return Record{Value:v.GetString(key),ID:j.next}
}
func (j *Journal) Historical(r Record) (Source,bool) {s,ok:=j.events[r.ID];return s,ok}
func (j *Journal) OriginNow() Source {return currentSource()}
