package zerolog_test

import (
 "bytes"
 "context"
 "encoding/json"
 "os"
 "testing"

 "github.com/rs/zerolog"
)

type evoTraceKey struct{}
type evoHook struct{ observed []string }

func (h *evoHook) Run(e *zerolog.Event, _ zerolog.Level, _ string) {
 v,_:=e.GetCtx().Value(evoTraceKey{}).(string)
 h.observed=append(h.observed,v)
}

func expectedOutputTrace() string {
 switch os.Getenv("EVO_ORIGINAL_SOURCE_ARM") {
 case "pre":return ""
 case "post":return "trace-77"
 default:panic("EVO_ORIGINAL_SOURCE_ARM must be pre or post")
 }
}

func evoLogger(out *bytes.Buffer, hook *evoHook, ctx context.Context) zerolog.Logger {
 return zerolog.New(out).Hook(hook).With().Str("service","api").Ctx(ctx).Logger()
}

func TestEvoOldContextObserverPreserved(t *testing.T) {
 var buf bytes.Buffer
 h:=&evoHook{}
 ctx:=context.WithValue(context.Background(),evoTraceKey{},"trace-77")
 l:=evoLogger(&buf,h,ctx)
 l.Info().Msg("old")
 if len(h.observed)!=1||h.observed[0]!="trace-77"{t.Fatalf("old trace lost: %+v",h.observed)}
 var body map[string]any
 if err:=json.Unmarshal(bytes.TrimSpace(buf.Bytes()),&body);err!=nil{t.Fatal(err)}
 if body["service"]!="api"||body["message"]!="old"{t.Fatalf("old body changed: %+v",body)}
}

func TestEvoOriginalOutputHistoricalFailureOrFix(t *testing.T) {
 var original,redirected bytes.Buffer
 h:=&evoHook{}
 ctx:=context.WithValue(context.Background(),evoTraceKey{},"trace-77")
 l:=evoLogger(&original,h,ctx)
 after:=l.Output(&redirected)
 after.Info().Msg("redirect")
 if len(h.observed)!=1||h.observed[0]!=expectedOutputTrace() {
  t.Fatalf("Output source arm %s trace got=%v want=%q",os.Getenv("EVO_ORIGINAL_SOURCE_ARM"),h.observed,expectedOutputTrace())
 }
 if original.Len()!=0{t.Fatal("redirected log wrote to old writer")}
 var body map[string]any
 if err:=json.Unmarshal(bytes.TrimSpace(redirected.Bytes()),&body);err!=nil{t.Fatal(err)}
 if body["service"]!="api"||body["message"]!="redirect"{t.Fatalf("writer/field migration broke: %+v",body)}
}

func TestEvoTwoConsecutiveOutputCopies(t *testing.T) {
 var from,middle,destination bytes.Buffer
 h:=&evoHook{}
 ctx:=context.WithValue(context.Background(),evoTraceKey{},"trace-77")
 l:=evoLogger(&from,h,ctx)
 second:=l.Output(&middle).Output(&destination)
 second.Info().Msg("two")
 if len(h.observed)!=1||h.observed[0]!=expectedOutputTrace(){t.Fatalf("two-step copy trace %v",h.observed)}
 if from.Len()!=0||middle.Len()!=0||destination.Len()==0{t.Fatal("writer copy routing invalid")}
}

func TestEvoClassicalExplicitEventContextRepair(t *testing.T) {
 var from,to bytes.Buffer
 h:=&evoHook{}
 ctx:=context.WithValue(context.Background(),evoTraceKey{},"trace-77")
 l:=evoLogger(&from,h,ctx)
 derived:=l.Output(&to)
 derived.Info().Ctx(ctx).Msg("manual")
 if len(h.observed)!=1||h.observed[0]!="trace-77"{t.Fatalf("ordinary event-level repair failed: %v",h.observed)}
}

func TestEvoDifferentWithContextPathNotFixedByOutputPR(t *testing.T) {
 var original,redirected bytes.Buffer
 h:=&evoHook{}
 ctx:=context.WithValue(context.Background(),evoTraceKey{},"trace-77")
 parent:=zerolog.New(&original).Hook(h)
 attached:=parent.WithContext(ctx)
 fetched:=zerolog.Ctx(attached)
 fetched.Info().Msg("attached")
 derived:=fetched.Output(&redirected)
 derived.Info().Msg("attached-redirect")
 if len(h.observed)!=2||h.observed[0]!=""||h.observed[1]!=""{
  t.Fatalf("distinct WithContext operator unexpectedly propagated trace: %+v",h.observed)
 }
}
