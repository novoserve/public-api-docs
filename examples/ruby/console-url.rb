require "uri"
require "json"
require "net/http"

url = URI("https://api.novoserve.com/v1/console-url/000-000")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Basic [BASE64 STRING OF KEY+SECRET]"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "remoteIp": "127.0.0.1",
  "whitelabel": "yes"
})

response = https.request(request)
puts response.read_body
