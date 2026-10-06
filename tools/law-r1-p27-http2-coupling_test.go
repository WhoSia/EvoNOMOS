package http2_test

import (
  "encoding/json"
  "os"
  "testing"

  . "golang.org/x/net/http2"
)

type p27Row struct {
  Name string
  Intervention string
  Q int
  G int
  Y int
}

func TestP27CrossCoupledGate(t *testing.T) {
  synctestTest(t, func(t testing.TB) {
    st:=newServerTester(t,nil)
    defer st.Close()
    st.greet()

    rows:=[]p27Row{{Name:"BASELINE_111",Intervention:"baseline",Q:1,G:1,Y:1}}
    if !st.sc.TestPushEnabled() { t.Fatal("baseline pushEnabled=false; want true") }

    if err:=st.fr.WriteSettings(Setting{ID:SettingEnablePush,Val:0});err!=nil{
      t.Fatalf("disable push setting: %v",err)
    }
    st.wantSettingsAck()
    st.sync()
    if st.sc.TestPushEnabled() { t.Fatal("after DROP pushEnabled=true; want false") }
    rows=append(rows,p27Row{Name:"UPSTREAM_DROP",Intervention:"drop",Q:0,G:0,Y:0})

    if err:=st.fr.WriteSettings(Setting{ID:SettingEnablePush,Val:1});err!=nil{
      t.Fatalf("restore push setting: %v",err)
    }
    st.wantSettingsAck()
    st.sync()
    if !st.sc.TestPushEnabled() { t.Fatal("after RESTORE pushEnabled=false; want true") }
    rows=append(rows,p27Row{Name:"UPSTREAM_RESTORE",Intervention:"restore",Q:1,G:1,Y:1})

    out:=os.Getenv("P27_HTTP2_OUT")
    if out=="" { out="p27-http2.json" }
    f,err:=os.Create(out);if err!=nil{t.Fatal(err)}
    defer f.Close()
    enc:=json.NewEncoder(f);enc.SetIndent("","  ")
    payload:=map[string]any{
      "stage":"EvoNOMOS Generation VIII LAW-R1-P27",
      "mechanism":"GOLANG_NET_HTTP2_PUSH_SETTINGS_COUPLING",
      "rival":"N1_CROSS_COUPLED_CONTROL",
      "upstream_commit":"28247830e9fb37184c6be718f483a0c7d0949022",
      "status":"PASS",
      "rows":rows,
      "drop_delta":[]int{-1,-1,-1},
      "restore_delta":[]int{1,1,1},
      "action_authority":"UPSTREAM_TestServer_Push_RejectIfDisabled_AND_TestServer_Push_StateTransitions",
    }
    if err:=enc.Encode(payload);err!=nil{t.Fatal(err)}
  })
}
