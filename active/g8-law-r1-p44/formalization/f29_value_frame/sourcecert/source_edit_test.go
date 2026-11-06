package sourcecert
import ("errors";"strings";"testing")
func TestExactOneSourceEditA(t *testing.T){
 before:=write(t,a,b);after:=write(t,strings.Replace(a,"\"a0\"","\"new\"",1),b)
 r,e:=CheckLiteralEdit(before,after,"A",true,true)
 if e!=nil||r.Cost!=1||r.After.Left!="new"{t.Fatal(r,e)}
}
func TestExactOneSourceEditB(t *testing.T){
 before:=write(t,a,b);after:=write(t,a,strings.Replace(b,"\"b0\"","\"new\"",1))
 r,e:=CheckLiteralEdit(before,after,"B",true,true)
 if e!=nil||r.Cost!=1||r.After.Right!="new"{t.Fatal(r,e)}
}
func TestCombinedEditHOLD(t *testing.T){
 before:=write(t,a,b)
 after:=write(t,strings.Replace(a,"\"a0\"","\"new\"",1),strings.Replace(b,"\"b0\"","\"new\"",1))
 if _,e:=CheckLiteralEdit(before,after,"A",true,true);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestWhitespaceEditHOLD(t *testing.T){
 before:=write(t,a,b)
 bad:=strings.Replace(strings.Replace(a,"\"a0\"","\"new\"",1),"package fixture","package  fixture",1)
 if _,e:=CheckLiteralEdit(before,write(t,bad,b),"A",true,true);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestNoopEditHOLD(t *testing.T){
 root:=write(t,a,b);if _,e:=CheckLiteralEdit(root,root,"A",true,true);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestUndeclaredEditHOLD(t *testing.T){
 root:=write(t,a,b);if _,e:=CheckLiteralEdit(root,root,"X",true,true);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestTwoStagePatchPath(t *testing.T){
 x:=write(t,a,b);y:=write(t,strings.Replace(a,"\"a0\"","\"new\"",1),b)
 z:=write(t,strings.Replace(a,"\"a0\"","\"new\"",1),strings.Replace(b,"\"b0\"","\"new\"",1))
 ab,e1:=CheckLiteralEdit(x,y,"A",true,true)
 bc,e2:=CheckLiteralEdit(y,z,"B",true,true)
 if e1!=nil||e2!=nil||ab.Cost+bc.Cost!=2||bc.After.Legacy!="old"||bc.After.Left!="new"||bc.After.Right!="new"{t.Fatal(ab,bc,e1,e2)}
}
