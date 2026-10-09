package middleware

import (
    "strings"
    "testing"
)

// Post-treatment bounded audit, NOT part of the prospective D13 freeze.
// A separately written scanner serves as the source-independent local grammar
// reference. Domain: every byte string of length 0..6 over a,b,quote,comma,
// space,tab (55,987 values). Only routing-observable tokens are asserted.
func p35O5ReferenceScanner(raw string) ([]string,bool) {
    const (start=iota; bare; quoted; afterQuoted)
    state:=start
    result:=[]string{}
    var b strings.Builder
    push:=func(){
        s:=strings.TrimSpace(b.String())
        if s!="" {result=append(result,s)}
        b.Reset()
    }
    for i:=0;i<len(raw);i++ {
        c:=raw[i]
        switch state {
        case start:
            switch c {
            case ' ', '\t', ',': continue
            case '"': state=quoted
            default: b.WriteByte(c); state=bare
            }
        case bare:
            if c=='"' {return nil,false}
            if c==',' {push();state=start;continue}
            b.WriteByte(c)
        case quoted:
            if c=='"' {
                if i+1<len(raw) && raw[i+1]=='"' {b.WriteByte('"');i++} else {state=afterQuoted}
            } else {b.WriteByte(c)}
        case afterQuoted:
            if c==',' {push();state=start;continue}
            if c!=' ' && c!='\t' {return nil,false}
        }
    }
    if state==quoted {return nil,false}
    push()
    return result,true
}
func TestP35O5PostTreatmentBoundedParserAudit(t *testing.T){
    alphabet:=[]byte{'a','b','"',',',' ','\t'}
    count:=0
    for length:=0;length<=6;length++{
        combinations:=1
        for i:=0;i<length;i++ {combinations*=len(alphabet)}
        for index:=0;index<combinations;index++ {
            code:=index
            word:=make([]byte,length)
            for i:=0;i<length;i++ {word[i]=alphabet[code%len(alphabet)]; code/=len(alphabet)}
            raw:=string(word)
            actual,ok:=p35O3ResearchTokens(raw)
            expected,eok:=p35O5ReferenceScanner(raw)
            // Original CSV rejects the empty byte stream as EOF; scanner
            // admits it as an empty list. Both produce no route match.
            if raw=="" && len(actual)==0 && len(expected)==0 {
                count++
                continue
            }
            if ok!=eok || strings.Join(actual,"\x00")!=strings.Join(expected,"\x00") {
                t.Fatalf("P35_O5_BOUNDED_GRAMMAR_MISMATCH raw=%q native=%q ok=%v reference=%q ok=%v",raw,actual,ok,expected,eok)
            }
            count++
        }
    }
    if count!=55987 {t.Fatalf("wrong bounded enumeration %d",count)}
    t.Logf("P35_O5_BOUNDED_OBSERVABLE_GRAMMAR_PASS inputs=%d",count)
}
