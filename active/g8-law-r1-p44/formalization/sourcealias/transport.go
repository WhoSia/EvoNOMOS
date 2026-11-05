package sourcealias

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "go/format"
 "go/parser"
 "go/token"
 "strconv"
)

var ErrCertificateIntegrity=errors.New("certificate receipt does not match trusted seal")
var ErrUnsupportedSource=errors.New("source not valid in the closed single-file grammar")
type Status string
const (
 Reused Status="REUSED_EXACT_AST"
 Invalidated Status="INVALIDATED_SOURCE_CHANGED"
 Unknown Status="UNKNOWN_UNSUPPORTED_SOURCE"
)
type Certificate struct{
 CanonicalSourceDigest string
 Shared bool
 LegacyAfterWrite string
 FutureAfterWrite string
}
type Seal struct{EvidenceDigest string}

// CanonicalDigest uses the standard Go parser and formatter.
// This permits whitespace-formatting changes only, NOT semantic source edits,
// renaming of identifiers, new compiler directives or additional files.
func CanonicalDigest(src string)(string,error){
 fs:=token.NewFileSet()
 file,err:=parser.ParseFile(fs,"fixture.go",src,parser.AllErrors|parser.ParseComments)
 if err!=nil || len(file.Comments)!=0{return "",ErrUnsupportedSource}
 var buf bytes.Buffer
 if err:=format.Node(&buf,fs,file);err!=nil{return "",err}
 sum:=sha256.Sum256(buf.Bytes())
 return hex.EncodeToString(sum[:]),nil
}
func evidenceBytes(c Certificate)string{
 // Explicit unambiguous length-prefixing, even if future strings contain '|'
 return strconv.Itoa(len(c.CanonicalSourceDigest))+":"+c.CanonicalSourceDigest+
  ":"+strconv.FormatBool(c.Shared)+
  ":"+strconv.Itoa(len(c.LegacyAfterWrite))+":"+c.LegacyAfterWrite+
  ":"+strconv.Itoa(len(c.FutureAfterWrite))+":"+c.FutureAfterWrite
}
func evidenceDigest(c Certificate)string{
 s:=sha256.Sum256([]byte(evidenceBytes(c)))
 return hex.EncodeToString(s[:])
}
// Issue performs an exact, typed source reanalysis once. The resulting receipt
// must be anchored by a TRUSTED external artifact store or verified issuer.
// A caller-created forged certificate+receipt is not authenticated by hashing.
func Issue(src string)(Certificate,Seal,error){
 facts,err:=Analyze(src);if err!=nil{return Certificate{},Seal{},err}
 digest,err:=CanonicalDigest(src);if err!=nil{return Certificate{},Seal{},err}
 c:=Certificate{CanonicalSourceDigest:digest,Shared:facts.Shared,LegacyAfterWrite:facts.LegacyAfterWrite,FutureAfterWrite:facts.FutureAfterWrite}
 return c,Seal{EvidenceDigest:evidenceDigest(c)},nil
}
// Verify reuses the previously anchored source-derived facts ONLY when the
// entire parsed source AST canonically matches the original source. Changes
// to even harmless identifiers invalidate this conservative exact-cache.
// It does NOT repeat go/types, but does reparse and format the whole file.
func Verify(src string,c Certificate,expectedTrustedSeal Seal)(Status,error){
 if evidenceDigest(c)!=expectedTrustedSeal.EvidenceDigest{return Unknown,ErrCertificateIntegrity}
 digest,err:=CanonicalDigest(src)
 if err!=nil{return Unknown,err}
 if digest!=c.CanonicalSourceDigest{return Invalidated,nil}
 return Reused,nil
}
