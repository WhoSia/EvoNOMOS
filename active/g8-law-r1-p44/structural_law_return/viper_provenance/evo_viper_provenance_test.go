package viper_test

import (
  "os"
  "reflect"
  "strings"
  "testing"

  "github.com/spf13/viper"
)

const evoEnvName = "APP_SERVICE_TOKEN"
const evoKey = "service.token"

type evoProjection struct {
  Value string
  IsSet bool
  InConfig bool
  AllSettings map[string]any
}

func evoOriginalSourceConfig(t *testing.T) *viper.Viper {
  t.Helper()
  v := viper.New()
  v.SetConfigType("yaml")
  if err:=v.ReadConfig(strings.NewReader("service:\n  token: same-token\n"));err!=nil {t.Fatal(err)}
  v.SetEnvPrefix("APP")
  v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
  v.AutomaticEnv()
  return v
}
func evoReadPublic(t *testing.T) evoProjection {
  t.Helper()
  v:=evoOriginalSourceConfig(t)
  return evoProjection{Value:v.GetString(evoKey),IsSet:v.IsSet(evoKey),InConfig:v.InConfig(evoKey),AllSettings:v.AllSettings()}
}
func evoWithEnv(t *testing.T, present bool, value string, run func()) {
  t.Helper()
  previous,hadPrevious:=os.LookupEnv(evoEnvName)
  if present {
    if err:=os.Setenv(evoEnvName,value);err!=nil{t.Fatal(err)}
  }else{
    if err:=os.Unsetenv(evoEnvName);err!=nil{t.Fatal(err)}
  }
  defer func(){
    var err error
    if hadPrevious{err=os.Setenv(evoEnvName,previous)}else{err=os.Unsetenv(evoEnvName)}
    if err!=nil{t.Errorf("restore env: %v",err)}
  }()
  run()
}

// Original source, independently authored outside Viper package.
// Both worlds expose exactly the same selected public value/IsSet/InConfig/AllSettings.
func TestEvoSamePublicProjectionDifferentActualProvenance(t *testing.T){
  var fromFile,fromEnv evoProjection
  evoWithEnv(t,false,"",func(){fromFile=evoReadPublic(t)})
  evoWithEnv(t,true,"same-token",func(){fromEnv=evoReadPublic(t)})
  if fromFile.Value!="same-token"||fromEnv.Value!="same-token"{t.Fatalf("source resolution unexpected %q/%q",fromFile.Value,fromEnv.Value)}
  if !fromFile.IsSet||!fromEnv.IsSet||!fromFile.InConfig||!fromEnv.InConfig{t.Fatalf("expected both true %+v %+v",fromFile,fromEnv)}
  if !reflect.DeepEqual(fromFile,fromEnv){t.Fatalf("presealed projection equality falsified: file=%+v env=%+v",fromFile,fromEnv)}
  t.Logf("EVO_VIPER_EQUAL_PUBLIC_PROJECTION true value=%q isSet=%t inConfig=%t",fromFile.Value,fromFile.IsSet,fromFile.InConfig)
}

func TestEvoValueOnlyDesignDecisionCannotMeetBoth(t *testing.T){
  var fromFile,fromEnv evoProjection
  evoWithEnv(t,false,"",func(){fromFile=evoReadPublic(t)})
  evoWithEnv(t,true,"same-token",func(){fromEnv=evoReadPublic(t)})
  if !reflect.DeepEqual(fromFile,fromEnv){t.Fatal("needed same z")}
  // A policy sees only z. For these two contexts its choice must be identical.
  // F=locally managed; E=externally managed. The minimum possible
  // worst-case unit regret is 1: choosing F hurts env, choosing E hurts file.
  actions:=[]string{"F","E"}
  minimumWorst:=2
  for _,a:=range actions{
    fileLoss,envLoss:=0,0
    if a!="F"{fileLoss=1}
    if a!="E"{envLoss=1}
    worst:=fileLoss;if envLoss>worst{worst=envLoss}
    if worst<minimumWorst{minimumWorst=worst}
  }
  if minimumWorst!=1{t.Fatalf("two-world minimax regret unexpectedly %d",minimumWorst)}
  t.Logf("EVO_VIPER_VALUE_ONLY_MINIMAX_REGRET %d",minimumWorst)
}

func TestEvoKnownSourceClassicEnvLookupExplainsBoth(t *testing.T){
  results:=[]string{}
  evoWithEnv(t,false,"",func(){
    value:=evoReadPublic(t).Value
    _,fromEnv:=os.LookupEnv(evoEnvName)
    if value!="same-token"||fromEnv{t.Fatal("file world not confirmed")}
    if fromEnv{results=append(results,"E")}else{results=append(results,"F")}
  })
  evoWithEnv(t,true,"same-token",func(){
    value:=evoReadPublic(t).Value
    _,fromEnv:=os.LookupEnv(evoEnvName)
    if value!="same-token"||!fromEnv{t.Fatal("env world not confirmed")}
    if fromEnv{results=append(results,"E")}else{results=append(results,"F")}
  })
  if !reflect.DeepEqual(results,[]string{"F","E"}){t.Fatalf("source-aware classic competitor failed: %v",results)}
  t.Logf("EVO_VIPER_CLASSICAL_KNOWN_ENV_2_OF_2 %v",results)
}

func TestEvoDifferentEnvironmentValueBreaksProjectionEquality(t *testing.T){
  var file,env evoProjection
  evoWithEnv(t,false,"",func(){file=evoReadPublic(t)})
  evoWithEnv(t,true,"different-token",func(){env=evoReadPublic(t)})
  if file.Value==env.Value{t.Fatalf("priority or env prefix unexpected: file=%q env=%q",file.Value,env.Value)}
  if reflect.DeepEqual(file,env){t.Fatal("expected control projection to split")}
  t.Logf("EVO_VIPER_NEGATIVE_CONTROL_DIFFERENT_VALUE file=%q env=%q",file.Value,env.Value)
}

func TestEvoOldClientConfigAvailableInBothWorlds(t *testing.T){
  for _,env:=range []bool{false,true}{
    evoWithEnv(t,env,"same-token",func(){
      v:=evoOriginalSourceConfig(t)
      if !v.InConfig(evoKey)||v.GetString(evoKey)!="same-token"{t.Fatalf("old behavior broken env=%v",env)}
    })
  }
}
