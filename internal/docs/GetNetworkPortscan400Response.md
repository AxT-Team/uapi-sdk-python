# GetNetworkPortscan400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_portscan400_response import GetNetworkPortscan400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPortscan400Response from a JSON string
get_network_portscan400_response_instance = GetNetworkPortscan400Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPortscan400Response.to_json())

# convert the object into a dict
get_network_portscan400_response_dict = get_network_portscan400_response_instance.to_dict()
# create an instance of GetNetworkPortscan400Response from a dict
get_network_portscan400_response_from_dict = GetNetworkPortscan400Response.from_dict(get_network_portscan400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


