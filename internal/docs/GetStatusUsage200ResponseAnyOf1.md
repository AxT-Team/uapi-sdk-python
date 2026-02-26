# GetStatusUsage200ResponseAnyOf1

查询指定path参数时返回的单个端点统计数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from uapi.models.get_status_usage200_response_any_of1 import GetStatusUsage200ResponseAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusUsage200ResponseAnyOf1 from a JSON string
get_status_usage200_response_any_of1_instance = GetStatusUsage200ResponseAnyOf1.from_json(json)
# print the JSON string representation of the object
print(GetStatusUsage200ResponseAnyOf1.to_json())

# convert the object into a dict
get_status_usage200_response_any_of1_dict = get_status_usage200_response_any_of1_instance.to_dict()
# create an instance of GetStatusUsage200ResponseAnyOf1 from a dict
get_status_usage200_response_any_of1_from_dict = GetStatusUsage200ResponseAnyOf1.from_dict(get_status_usage200_response_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


