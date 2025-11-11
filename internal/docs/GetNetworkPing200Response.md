# GetNetworkPing200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** | 平均延迟(ms) | [optional] 
**code** | **int** |  | [optional] 
**host** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**max** | **float** | 最大延迟(ms) | [optional] 
**min** | **float** | 最小延迟(ms) | [optional] 

## Example

```python
from uapi.models.get_network_ping200_response import GetNetworkPing200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPing200Response from a JSON string
get_network_ping200_response_instance = GetNetworkPing200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPing200Response.to_json())

# convert the object into a dict
get_network_ping200_response_dict = get_network_ping200_response_instance.to_dict()
# create an instance of GetNetworkPing200Response from a dict
get_network_ping200_response_from_dict = GetNetworkPing200Response.from_dict(get_network_ping200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


