# GetNetworkWxdomain502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_wxdomain502_response import GetNetworkWxdomain502Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkWxdomain502Response from a JSON string
get_network_wxdomain502_response_instance = GetNetworkWxdomain502Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkWxdomain502Response.to_json())

# convert the object into a dict
get_network_wxdomain502_response_dict = get_network_wxdomain502_response_instance.to_dict()
# create an instance of GetNetworkWxdomain502Response from a dict
get_network_wxdomain502_response_from_dict = GetNetworkWxdomain502Response.from_dict(get_network_wxdomain502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


