<?php

$apiKey = 'apikey';
$apiSecret = 'apisecret';
$serverTag = '000-000';

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.novoserve.com/v0/servers/'.$serverTag.'/ipmi-link',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_USERPWD => $apiKey.':'.$apiSecret,
  CURLOPT_POSTFIELDS =>'{
    "remoteIp": "127.0.0.1",
    "whitelabel": "yes"
  }',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;