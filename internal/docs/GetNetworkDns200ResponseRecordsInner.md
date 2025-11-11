# GetNetworkDns200ResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**flag** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**pri** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 

## Example

```python
from uapi.models.get_network_dns200_response_records_inner import GetNetworkDns200ResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkDns200ResponseRecordsInner from a JSON string
get_network_dns200_response_records_inner_instance = GetNetworkDns200ResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetNetworkDns200ResponseRecordsInner.to_json())

# convert the object into a dict
get_network_dns200_response_records_inner_dict = get_network_dns200_response_records_inner_instance.to_dict()
# create an instance of GetNetworkDns200ResponseRecordsInner from a dict
get_network_dns200_response_records_inner_from_dict = GetNetworkDns200ResponseRecordsInner.from_dict(get_network_dns200_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


