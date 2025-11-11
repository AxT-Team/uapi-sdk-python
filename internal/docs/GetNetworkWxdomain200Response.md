# GetNetworkWxdomain200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**title** | **str** | 状态标题 | [optional] 
**type** | **str** | 状态类型 | [optional] 

## Example

```python
from uapi.models.get_network_wxdomain200_response import GetNetworkWxdomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkWxdomain200Response from a JSON string
get_network_wxdomain200_response_instance = GetNetworkWxdomain200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkWxdomain200Response.to_json())

# convert the object into a dict
get_network_wxdomain200_response_dict = get_network_wxdomain200_response_instance.to_dict()
# create an instance of GetNetworkWxdomain200Response from a dict
get_network_wxdomain200_response_from_dict = GetNetworkWxdomain200Response.from_dict(get_network_wxdomain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


