# NovoServe Public API Documentation
This repository contains code examples for NovoServe's Public API.

The API documentation is hosted on our API server.
- [API documentation](https://api.novoserve.com/docs)
- [Raw OpenAPI specification](https://api.novoserve.com/v0/swagger.json)

## Code examples
Code examples to use our API are located in the `examples/` directory.  
Some code examples add an 'Authorization' header, which contains a base64 string of your API key and secret for authentication.  
Generating a base64 string can be easily done in most programming languages, but for simplicity the following command in bash can also be used:
```shell
echo -n 'key:secret' | base64
```
Replace `'key:secret'` with your own credentials, and this will result in a base64 string that can be used across the code examples.

## Python library
A Python library to interact with our API can be found under `libraries/python/`.  
For more information, please consult the README located at `libraries/python/README.md`.
