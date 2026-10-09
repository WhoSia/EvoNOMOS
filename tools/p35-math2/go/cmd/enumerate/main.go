package main
import("encoding/json";"os";math2 "evonomos/p35math2")
func main(){if err:=json.NewEncoder(os.Stdout).Encode(math2.Evaluate());err!=nil{panic(err)}}
