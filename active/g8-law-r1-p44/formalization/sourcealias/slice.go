package sourcealias

import (
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "go/ast"
 "go/parser"
 "go/token"
 "go/types"
 "strconv"
)

var ErrSliceScope = errors.New("source revision outside fixed two-file dependency grammar")

type SourcePair struct {
 Core string
 Auxiliary string
}
type SliceCertificate struct {
 CoreTokenDigest string
 Shared bool
 LegacyAfterWrite string
 FutureAfterWrite string
 Scope string
}
type SliceReceipt struct { Digest string }
type SliceVerdict string
const (
 SliceReused SliceVerdict="SLICE_REUSED_AFTER_AUXILIARY_CHANGE"
 SliceInvalid SliceVerdict="SLICE_INVALID_CORE_CHANGE"
 SliceUnknown SliceVerdict="SLICE_UNKNOWN_SCOPE_OR_TRUST"
)
const frozenScope="fixture.go+aux.go;aux=single-pure-constant-function;go=1.23.2;no-imports;no-globals;no-other-files"

// checkAux checks a strict, unconnected source declaration. The function is
// not reachable from Build/Write because the two functions' closed grammar
// contains no calls, pointers to it, reflection, globals, or imports.
// This is an explicit closed-world model, NOT Go-wide call-graph proof.
func checkAux(file *ast.File)error {
 if file==nil||file.Name.Name!="fixture"||len(file.Imports)!=0||len(file.Comments)!=0||len(file.Decls)!=1{
  return ErrSliceScope
 }
 f,ok:=file.Decls[0].(*ast.FuncDecl)
 if !ok||f.Recv!=nil||f.Name.Name!="Aux"||f.Type.Params==nil||len(f.Type.Params.List)!=0||
 f.Type.Results==nil||len(f.Type.Results.List)!=1||len(f.Type.Results.List[0].Names)!=0||
 !ident(f.Type.Results.List[0].Type,"string")||f.Body==nil||len(f.Body.List)!=1{
  return ErrSliceScope
 }
 if f.Type.TypeParams!=nil&&len(f.Type.TypeParams.List)!=0{return ErrSliceScope}
 ret,ok:=f.Body.List[0].(*ast.ReturnStmt)
 if !ok||len(ret.Results)!=1{return ErrSliceScope}
 l,ok:=ret.Results[0].(*ast.BasicLit)
 if !ok||l.Kind!=token.STRING{return ErrSliceScope}
 if _,err:=strconv.Unquote(l.Value);err!=nil{return ErrSliceScope}
 return nil
}

// AcceptSourcePair requires EXACTLY the two named sources supplied by an
// authenticated closed-world build manifest, which the caller must attest.
// It parses/types-checks ALL supplied code at both issue and verify time.
func AcceptSourcePair(pair SourcePair)error{
 if _,err:=Analyze(pair.Core);err!=nil{return ErrSliceScope}
 fs:=token.NewFileSet()
 core,err:=parser.ParseFile(fs,"fixture.go",pair.Core,parser.AllErrors|parser.ParseComments)
 if err!=nil{return ErrSliceScope}
 auxiliary,err:=parser.ParseFile(fs,"aux.go",pair.Auxiliary,parser.AllErrors|parser.ParseComments)
 if err!=nil||checkAux(auxiliary)!=nil{return ErrSliceScope}
 if _,err=(&types.Config{}).Check("fixture",fs,[]*ast.File{core,auxiliary},nil);err!=nil{return ErrSliceScope}
 return nil
}
func sliceDigest(c SliceCertificate)string {
 // fixed field order and length-prefixed strings avoid concatenation ambiguity
 fields:=[]string{c.CoreTokenDigest,c.LegacyAfterWrite,c.FutureAfterWrite,c.Scope,strconv.FormatBool(c.Shared)}
 h:=sha256.New()
 for _,s:=range fields{
  h.Write([]byte(strconv.Itoa(len(s))+":"+s))
 }
 return hex.EncodeToString(h.Sum(nil))
}

// IssueSlice pins the customer-relevant source token sequence and its typed
// alias effects. Caller must anchor the returned receipt in a trusted store.
func IssueSlice(pair SourcePair)(SliceCertificate,SliceReceipt,error){
 if err:=AcceptSourcePair(pair);err!=nil{return SliceCertificate{},SliceReceipt{},err}
 result,err:=Analyze(pair.Core);if err!=nil{return SliceCertificate{},SliceReceipt{},err}
 digest,err:=CanonicalDigest(pair.Core);if err!=nil{return SliceCertificate{},SliceReceipt{},err}
 cert:=SliceCertificate{digest,result.Shared,result.LegacyAfterWrite,result.FutureAfterWrite,frozenScope}
 return cert,SliceReceipt{sliceDigest(cert)},nil
}

// VerifySlice admits a genuine changed auxiliary program only after rejecting
// all unsupported cross-file effects and proving the core token sequence fixed.
// The independent trusted receipt is a REQUIRED assumption; a hash does not
// authenticate an adversarial issuer. No automatic discovery of Go build files.
func VerifySlice(pair SourcePair,cert SliceCertificate,trusted SliceReceipt)(SliceVerdict,error){
 if cert.Scope!=frozenScope||sliceDigest(cert)!=trusted.Digest{return SliceUnknown,ErrCertificateIntegrity}
 if err:=AcceptSourcePair(pair);err!=nil{return SliceUnknown,err}
 digest,err:=CanonicalDigest(pair.Core);if err!=nil{return SliceUnknown,err}
 if digest!=cert.CoreTokenDigest{return SliceInvalid,nil}
 return SliceReused,nil
}

// ClassicalFullSliceReanalysis is an equal-source-information rival. It
// computes the current source effect from scratch and rejects unmodeled code.
func ClassicalFullSliceReanalysis(pair SourcePair)(Result,error){
 if err:=AcceptSourcePair(pair);err!=nil{return Result{},err}
 return Analyze(pair.Core)
}
// ClassicalDependencyCache performs the identical scope validation with an
// ordinary persisted core token digest, without any special certificate layer.
func ClassicalDependencyCache(pair SourcePair,coreDigest string)(bool,error){
 if err:=AcceptSourcePair(pair);err!=nil{return false,err}
 got,err:=CanonicalDigest(pair.Core)
 if err!=nil{return false,err}
 return got==coreDigest,nil
}
