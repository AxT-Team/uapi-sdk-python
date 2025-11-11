# GetNetworkPortscan200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**port_status** | **str** | \&quot;open\&quot;, \&quot;closed\&quot;, 或 \&quot;timeout\&quot; | [optional] 
**protocol** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_portscan200_response import GetNetworkPortscan200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPortscan200Response from a JSON string
get_network_portscan200_response_instance = GetNetworkPortscan200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPortscan200Response.to_json())

# convert the object into a dict
get_network_portscan200_response_dict = get_network_portscan200_response_instance.to_dict()
# create an instance of GetNetworkPortscan200Response from a dict
get_network_portscan200_response_from_dict = GetNetworkPortscan200Response.from_dict(get_network_portscan200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


