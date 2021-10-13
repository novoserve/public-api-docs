package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://api.novoserve.com/v0/servers/000-000/ipmi-link"
  method := "POST"

  payload := strings.NewReader(`{`+"
  "+`
      "remoteIp": "127.0.0.1",`+"
  "+`
      "whitelabel": "yes"`+"
  "+`
  }`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Basic [BASE64 STRING OF KEY+SECRET]")
  req.Header.Add("Content-Type", "application/json")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
