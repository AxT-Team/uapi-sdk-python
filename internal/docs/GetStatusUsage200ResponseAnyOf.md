# GetStatusUsage200ResponseAnyOf

查询所有端点时返回的聚合统计数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[GetStatusUsage200ResponseAnyOfEndpointsInner]**](GetStatusUsage200ResponseAnyOfEndpointsInner.md) |  | [optional] 
**unaggregated** | [**GetStatusUsage200ResponseAnyOfUnaggregated**](GetStatusUsage200ResponseAnyOfUnaggregated.md) |  | [optional] 

## Example

```python
from uapi.models.get_status_usage200_response_any_of import GetStatusUsage200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusUsage200ResponseAnyOf from a JSON string
get_status_usage200_response_any_of_instance = GetStatusUsage200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print(GetStatusUsage200ResponseAnyOf.to_json())

# convert the object into a dict
get_status_usage200_response_any_of_dict = get_status_usage200_response_any_of_instance.to_dict()
# create an instance of GetStatusUsage200ResponseAnyOf from a dict
get_status_usage200_response_any_of_from_dict = GetStatusUsage200ResponseAnyOf.from_dict(get_status_usage200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


