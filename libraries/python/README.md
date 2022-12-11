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
print(server['results']['id'])
print(server['results']['location']['dataCenter'])
```

## In-depth usage
These examples showcase the possible actions that are exposed by this library.
These all assume that a pre-existing API object called `novoapi` has been previously created.
(See the 'Basic usage' chapter above.)  

### Servers
#### Get information about all servers
```python
novoapi.get_all_servers()
```
#### Get information about a specific server
```python
novoapi.get_server("123-123")
```

### Power actions
#### Get the current power state
```python
novoapi.get_power_state("123-123")
```
#### Power a server on
```python
novoapi.power_on("123-123")
```
#### Power a server off
```python
novoapi.power_off("123-123")
```
#### Reboot a server
```python
novoapi.reboot("123-123")
```
#### Cold boot a server
```python
novoapi.cold_boot("123-123")
```

### Bandwidth statistics
#### Get the bandwidth statistics for a server
```python
novoapi.get_bandwidth_usage("123-123", from_epoch=1577833200, until_epoch=1609455600)
```
#### Get a graph of bandwidth statistics for a server (base64 encoded string)
```python
novoapi.get_bandwidth_graph("123-123", from_epoch=1577833200, until_epoch=1609455600, width=500, height=500)
```

### Console URL
#### Generate a console URL for a server accessible from a specific IP address
```python
novoapi.get_ipmi_link("123-123", "192.168.0.1")
```
#### Generate a whitelabel console URL
```python
novoapi.get_ipmi_link("123-123", "192.168.0.1", whitelabel="yes")
```

### Virtual media
These endpoints control the virtual media mounted on a server.
#### Get the currently mounted ISO for a server
```python
novoapi.get_virtual_media("123-123")
```
#### Mount a specific ISO on a server
```python
novoapi.mount_virtual_media("123-123", "http://webiso.nl.novoserve.org/path/to/iso")
```
#### Unmount the ISO on a server
```python
novoapi.unmount_virtual_media("123-123")
```
#### Get all possible virtual media options for a server
```python
novoapi.get_virtual_media_images("123-123")
```

### Network configuration
#### Get the current network configuration for a server
```python
novoapi.get_network_config("123-123")
```
#### Shut down a port for a server
```python
network_config = {
    "shutdown": True
}
novoapi.set_network_config("123-123", network_config)
```
#### Reconfigure a port for a server
```python
network_config = {
    "l2-domain": "12-3456",
    "bonding": True,
    "rateLimit": 1000
}
novoapi.set_network_config("123-123", network_config)
```

### Layer 2 domains
#### Get all L2 domains
```python
novoapi.get_l2_domains()
```
#### Get specific L2 domain by ID
```python
novoapi.get_l2_domain("12-3456")
```
#### Set the name for an L2 domain
```python
novoapi.set_l2_domain_name("12-3456", l2_domain_name="l2-domain-1")
```

### Networks
#### Get all networks
```python
novoapi.get_networks()
```
#### Get specific network by ID
```python
novoapi.get_network(1234)
```
#### Set the name for a network
```python
novoapi.set_network_name(1234, network_name="network-1")
```

### rDNS records
#### Get all rDNS records
```python
novoapi.get_rdns_records()
```
#### Create/set an rDNS record
```python
novoapi.set_rdns_record(ip="192.168.0.1", record="host1.domain.test")
```
#### Get all rDNS records for a specific network
```python
novoapi.get_rdns_records_for_network(network_id=1234)
```
#### Get a specific rDNS record by ID
```python
novoapi.get_rdns_record(1234)
```
#### Delete an rDNS record by ID
```python
novoapi.delete_rdns_record(1234)
```
