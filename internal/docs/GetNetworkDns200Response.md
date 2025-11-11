# GetNetworkDns200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**domain** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**records** | [**List[GetNetworkDns200ResponseRecordsInner]**](GetNetworkDns200ResponseRecordsInner.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_dns200_response import GetNetworkDns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkDns200Response from a JSON string
get_network_dns200_response_instance = GetNetworkDns200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkDns200Response.to_json())

# convert the object into a dict
get_network_dns200_response_dict = get_network_dns200_response_instance.to_dict()
# create an instance of GetNetworkDns200Response from a dict
get_network_dns200_response_from_dict = GetNetworkDns200Response.from_dict(get_network_dns200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


