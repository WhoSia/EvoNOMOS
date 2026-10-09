package main

import (
  "encoding/json"
  "os"
  math0 "evonomos/p35math0"
)

func main() {
    if err:=json.NewEncoder(os.Stdout).Encode(math0.Enumerate());err!=nil{panic(err)}
}
