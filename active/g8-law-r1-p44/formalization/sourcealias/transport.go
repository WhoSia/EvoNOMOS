package sourcealias

import (
 "crypto/sha256"
 "encoding/hex"
 "errors"
 "go/parser"
 "go/scanner"
 "go/token"
 "strconv"
)

var ErrCertificateIntegrity=errors.New("certificate receipt does not match trusted seal")
var ErrUnsupportedSource=errors.New("source not valid in the closed single-file grammar")
type Status string
const (
 Reused Status="REUSED_EXACT_TOKEN_SEQUENCE"
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

// CanonicalDigest hashes the exact Go lexer token sequence, including
// implicit semicolon tokens but excluding whitespace. Full-file parser first
// rejects comments, build tags and malformed Go. A matching token sequence
// implies matching parsed syntax within the original fixed build environment.
// This does NOT prove alpha-renaming/semantic equivalence.
func CanonicalDigest(src string)(string,error){
 fs:=token.NewFileSet()
 file,err:=parser.ParseFile(fs,"fixture.go",src,parser.AllErrors|parser.ParseComments)
 if err!=nil||file==nil||len(file.Comments)!=0{return "",ErrUnsupportedSource}
 var scan scanner.Scanner
 scan.Init(fs.AddFile("lex.go",-1,len(src)),[]byte(src),nil,0)
 h:=sha256.New()
 for{
  _,tok,lit:=scan.Scan()
  if tok==token.EOF{break}
  // Explicitly length-prefix token lexical content to avoid ambiguity.
  entry:=strconv.Itoa(int(tok))+":"+strconv.Itoa(len(lit))+":"+lit+";"
  _,_=h.Write([]byte(entry))
 }
 return hex.EncodeToString(h.Sum(nil)),nil
}
func evidenceBytes(c Certificate)string{
 return strconv.Itoa(len(c.CanonicalSourceDigest))+":"+c.CanonicalSourceDigest+
  ":"+strconv.FormatBool(c.Shared)+
  ":"+strconv.Itoa(len(c.LegacyAfterWrite))+":"+c.LegacyAfterWrite+
  ":"+strconv.Itoa(len(c.FutureAfterWrite))+":"+c.FutureAfterWrite
}
func evidenceDigest(c Certificate)string{
 s:=sha256.Sum256([]byte(evidenceBytes(c)))
 return hex.EncodeToString(s[:])
}
// Issue performs exact typed closed-grammar analysis. Its Seal must be pinned
// separately by a trusted external source: hashes are NOT authentication.
func Issue(src string)(Certificate,Seal,error){
 facts,err:=Analyze(src);if err!=nil{return Certificate{},Seal{},err}
 digest,err:=CanonicalDigest(src);if err!=nil{return Certificate{},Seal{},err}
 c:=Certificate{CanonicalSourceDigest:digest,Shared:facts.Shared,LegacyAfterWrite:facts.LegacyAfterWrite,FutureAfterWrite:facts.FutureAfterWrite}
 return c,Seal{EvidenceDigest:evidenceDigest(c)},nil
}
// Verify is conservative: it trusts prior typed source analysis only if a
// valid externally anchored certificate and exact token sequence match.
// Source token changes invalidate even when a full classical analyzer could
// prove equivalence. It parses and lexes but does not run go/types.
func Verify(src string,c Certificate,expectedTrustedSeal Seal)(Status,error){
 if evidenceDigest(c)!=expectedTrustedSeal.EvidenceDigest{return Unknown,ErrCertificateIntegrity}
 digest,err:=CanonicalDigest(src)
 if err!=nil{return Unknown,err}
 if digest!=c.CanonicalSourceDigest{return Invalidated,nil}
 return Reused,nil
}
