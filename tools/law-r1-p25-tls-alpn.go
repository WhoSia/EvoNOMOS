package main

import (
	"context"
	"crypto/ed25519"
	"crypto/rand"
	"crypto/tls"
	"crypto/x509"
	"crypto/x509/pkix"
	"encoding/json"
	"fmt"
	"math/big"
	"net"
	"os"
	"runtime"
	"time"
)

type Cell struct {
	Name string `json:"name"`
	Q int `json:"q"`
	G int `json:"g"`
	ClientProtos []string `json:"client_protos"`
	ServerProtos []string `json:"server_protos"`
	ReferenceSelected string `json:"reference_selected"`
	LiveSelected string `json:"live_selected"`
	Y int `json:"y"`
	ClientHandshakeOK bool `json:"client_handshake_ok"`
	ServerHandshakeOK bool `json:"server_handshake_ok"`
}

func referenceNegotiateALPN(serverProtos, clientProtos []string) (string,error) {
	if len(serverProtos)==0 || len(clientProtos)==0 { return "",nil }
	var http11fallback bool
	for _,s:=range serverProtos{
		for _,c:=range clientProtos{
			if s==c { return s,nil }
			if s=="h2" && c=="http/1.1" { http11fallback=true }
		}
	}
	if http11fallback { return "",nil }
	return "",fmt.Errorf("unsupported")
}

func cert() tls.Certificate {
	pub,priv,err:=ed25519.GenerateKey(rand.Reader);if err!=nil{panic(err)}
	tmpl:=&x509.Certificate{
		SerialNumber:big.NewInt(1),
		Subject:pkix.Name{CommonName:"localhost"},
		NotBefore:time.Now().Add(-time.Hour),
		NotAfter:time.Now().Add(time.Hour),
		KeyUsage:x509.KeyUsageDigitalSignature,
		ExtKeyUsage:[]x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
		DNSNames:[]string{"localhost"},
	}
	der,err:=x509.CreateCertificate(rand.Reader,tmpl,tmpl,pub,priv);if err!=nil{panic(err)}
	return tls.Certificate{Certificate:[][]byte{der},PrivateKey:priv}
}

func live(clientProtos,serverProtos []string)(string,bool,bool,error){
	a,b:=net.Pipe()
	defer a.Close(); defer b.Close()
	srv:=tls.Server(a,&tls.Config{Certificates:[]tls.Certificate{cert()},NextProtos:serverProtos})
	cli:=tls.Client(b,&tls.Config{InsecureSkipVerify:true,NextProtos:clientProtos})
	ctx,cancel:=context.WithTimeout(context.Background(),5*time.Second);defer cancel()
	type res struct{err error}
	ch:=make(chan res,1)
	go func(){ch<-res{srv.HandshakeContext(ctx)}}()
	cerr:=cli.HandshakeContext(ctx)
	sres:=<-ch
	if cerr!=nil || sres.err!=nil { return "",cerr==nil,sres.err==nil,fmt.Errorf("client=%v server=%v",cerr,sres.err) }
	return cli.ConnectionState().NegotiatedProtocol,true,true,nil
}

func main(){
	target:="proto1"
	cases:=[]struct{name string;q,g int}{
		{"Q0_G0",0,0},{"Q0_G1",0,1},{"Q1_G0",1,0},{"Q1_G1",1,1},
	}
	var cells []Cell
	pass:=true
	for _,c:=range cases{
		var cp,sp []string
		if c.q==1 {cp=[]string{target}}
		if c.g==1 {sp=[]string{target}}
		ref,rerr:=referenceNegotiateALPN(sp,cp)
		if rerr!=nil {fmt.Fprintln(os.Stderr,rerr);os.Exit(2)}
		got,cok,sok,err:=live(cp,sp)
		if err!=nil {fmt.Fprintln(os.Stderr,c.name,err);os.Exit(2)}
		y:=0;if got==target{y=1}
		expected:=0;if c.q==1&&c.g==1{expected=1}
		if y!=expected || got!=ref {pass=false}
		cells=append(cells,Cell{Name:c.name,Q:c.q,G:c.g,ClientProtos:cp,ServerProtos:sp,ReferenceSelected:ref,LiveSelected:got,Y:y,ClientHandshakeOK:cok,ServerHandshakeOK:sok})
	}
	payload:=map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P25",
		"family":"GO_TLS_ALPN_TARGET_PROTOCOL_NEGOTIATION",
		"source_commit":"47cf464896de41e404e0efeca4fa2cc1e321872c",
		"go_runtime":runtime.Version(),
		"status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
		"chain":[]string{"ClientHello NextProtos","TLS parser -> clientHello.alpnProtocols","Q(target present)","server NextProtos gate","NegotiatedProtocol"},
		"cells":cells,
		"truth_table":[]int{cells[0].Y,cells[1].Y,cells[2].Y,cells[3].Y},
	}
	os.MkdirAll("out-p25",0755)
	b,_:=json.MarshalIndent(payload,"","  ")
	os.WriteFile("out-p25/p25-tls-alpn.json",append(b,'\n'),0644)
	fmt.Println("P25_TLS_ALPN="+payload["status"].(string))
	for _,c:=range cells{fmt.Printf("%s=%d selected=%q\n",c.Name,c.Y,c.LiveSelected)}
	if !pass {os.Exit(3)}
}
