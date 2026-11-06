package core
import ("context";"fmt";"net/http";"sync";"sync/atomic")
type CaptureMode uint8
const (LiveAlias CaptureMode=iota; FrozenValue)
type Shared struct{mu sync.RWMutex;value string}
func NewShared(v string)*Shared{return &Shared{value:v}}
func(s *Shared)Value()string{s.mu.RLock();defer s.mu.RUnlock();return s.value}
func(s *Shared)Set(v string){s.mu.Lock();s.value=v;s.mu.Unlock()}
type View struct{shared *Shared;frozen string;mode CaptureMode}
func(v View)Read()string{if v.mode==LiveAlias{return v.shared.Value()};return v.frozen}
type contextKey struct{}
func Captured(ctx context.Context)(View,bool){v,ok:=ctx.Value(contextKey{}).(View);return v,ok}
type Barrier struct{Entered chan struct{};Release chan struct{};used atomic.Bool}
func NewBarrier()*Barrier{return &Barrier{Entered:make(chan struct{}),Release:make(chan struct{})}}
func Capture(mode CaptureMode,s *Shared,b *Barrier)func(http.Handler)http.Handler{
 return func(next http.Handler)http.Handler{return http.HandlerFunc(func(w http.ResponseWriter,r *http.Request){
  if r.Method!=http.MethodGet||r.URL.Path!="/items/alpha"{next.ServeHTTP(w,r);return}
  v:=View{mode:mode,shared:s}
  if mode==FrozenValue{v.frozen=s.Value()}
  ctx:=context.WithValue(r.Context(),contextKey{},v)
  if b!=nil&&b.used.CompareAndSwap(false,true){close(b.Entered);select{case <-b.Release:case <-r.Context().Done():return}}
  next.ServeHTTP(w,r.WithContext(ctx))
 })}
}
func ItemHandler(getID func(context.Context)string)http.HandlerFunc{return func(w http.ResponseWriter,r *http.Request){
 v,ok:=Captured(r.Context());if !ok{http.Error(w,"missing snapshot",500);return}
 w.WriteHeader(200);_,_=fmt.Fprintf(w,"%s|%s",v.Read(),getID(r.Context()))
}}
func UpdateHandler(s *Shared)http.HandlerFunc{return func(w http.ResponseWriter,r *http.Request){
 label:=r.URL.Query().Get("label");if label==""{http.Error(w,"missing label",400);return}
 s.Set(label);w.WriteHeader(200);_,_=fmt.Fprintf(w,"updated:%s",label)
}}
