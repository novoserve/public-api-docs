var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://api.novoserve.com/v0/servers/000-000/ipmi-link',
  'headers': {
    'Authorization': 'Basic [BASE64 STRING OF KEY+SECRET]',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "remoteIp": "127.0.0.1",
    "whitelabel": "yes"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
