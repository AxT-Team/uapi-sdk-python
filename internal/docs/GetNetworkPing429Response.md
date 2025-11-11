# GetNetworkPing429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_ping429_response import GetNetworkPing429Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPing429Response from a JSON string
get_network_ping429_response_instance = GetNetworkPing429Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPing429Response.to_json())

# convert the object into a dict
get_network_ping429_response_dict = get_network_ping429_response_instance.to_dict()
# create an instance of GetNetworkPing429Response from a dict
get_network_ping429_response_from_dict = GetNetworkPing429Response.from_dict(get_network_ping429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


