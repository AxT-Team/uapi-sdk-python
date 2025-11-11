# GetNetworkPingmyip404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_pingmyip404_response import GetNetworkPingmyip404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPingmyip404Response from a JSON string
get_network_pingmyip404_response_instance = GetNetworkPingmyip404Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPingmyip404Response.to_json())

# convert the object into a dict
get_network_pingmyip404_response_dict = get_network_pingmyip404_response_instance.to_dict()
# create an instance of GetNetworkPingmyip404Response from a dict
get_network_pingmyip404_response_from_dict = GetNetworkPingmyip404Response.from_dict(get_network_pingmyip404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


