package main
import("encoding/json";"os";math1 "evonomos/p35math1")
func main(){if e:=json.NewEncoder(os.Stdout).Encode(math1.Evaluate());e!=nil{panic(e)}}
