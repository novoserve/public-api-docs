<?php

require 'Client.php';

use NovoServe\API\Client;

$api = new Client('APIKEY', 'APISECRET');
$api->ignoreCertificate(true);

$example = $api->post('servers/123-123/ipmi-link/', ['remoteIp' => '127.0.0.1']);
var_dump($example);
