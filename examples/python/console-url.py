import requests
import json

url = "https://api.novoserve.com/v1/console-url/000-000"

payload = json.dumps({
  "remoteIp": "127.0.0.1",
  "whitelabel": "yes"
})
headers = {
  'Authorization': 'Basic [BASE64 STRING OF KEY+SECRET]',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
