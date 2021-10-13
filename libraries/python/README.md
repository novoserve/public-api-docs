# NovoServe API Python library
## Introduction
This directory contains a Python library to interact with the NovoServe public API.
This library requires the `requests` library, so make sure to install it.

## Basic usage
```python
# Import the library
import novoapi

# Create an API object and pass the credentials
novoapi = novoapi.NovoServeApi("username", "apikey123")

# Use the newly created object to control servers
novoapi.power_off("123-123")
novoapi.power_on("123-123")
novoapi.reboot("123-123")

# The JSON response is automatically converted to a standard Python dictionary, and can be used as such.
server = novoapi.get_server("123-123")
print(server['id'])
print(server['location']['dataCenter'])
```

## In-depth usage
These examples showcase the possible actions that are exposed by this library.
These all assume that a pre-existing API object called `novoapi` has been previously created.
(See the 'Basic usage' chapter above.)  
All functions output 
### Power actions
#### Get the current power state
```python
novoapi.get_powerstate("123-123")
```
#### Power a server off
```python
novoapi.power_off("123-123")
```
#### Power a server on
```python
novoapi.power_on("123-123")
```
#### Reboot a server
```python
novoapi.reboot("123-123")
```
#### Cold boot a server
```python
novoapi.cold_boot("123-123")
```

### Servers
#### Get information about a specific server
```python
novoapi.get_server("123-123")
```
#### Get information about all servers
```python
novoapi.get_all_servers()
```

### Web ISO
#### Get all possible web ISO options
```python
novoapi.get_webiso_options()
```
#### Get the currently mounted ISO for a server
```python
novoapi.get_webiso("123-123")
```
#### Mount a specific ISO on a server
```python
novoapi.set_webiso("123-123", "https://webiso.novoserve.com/path/to/iso")
```
#### Unmount the ISO on a server
```python
novoapi.delete_webiso("123-123")
```

### Bandwidth statistics
#### Get the bandwidth statistics for a server
```python
novoapi.get_bandwidth("123-123")
```

### Console URL
#### Generate a console URL for a server accessible from a specific IP address
```python
novoapi.get_console_url("123-123", "192.168.0.1")
```