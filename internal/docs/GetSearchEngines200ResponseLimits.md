# GetSearchEngines200ResponseLimits

搜索结果数量限制

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **int** | 默认返回结果数 | [optional] 
**max** | **int** | 最大返回结果数 | [optional] 

## Example

```python
from uapi.models.get_search_engines200_response_limits import GetSearchEngines200ResponseLimits

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchEngines200ResponseLimits from a JSON string
get_search_engines200_response_limits_instance = GetSearchEngines200ResponseLimits.from_json(json)
# print the JSON string representation of the object
print(GetSearchEngines200ResponseLimits.to_json())

# convert the object into a dict
get_search_engines200_response_limits_dict = get_search_engines200_response_limits_instance.to_dict()
# create an instance of GetSearchEngines200ResponseLimits from a dict
get_search_engines200_response_limits_from_dict = GetSearchEngines200ResponseLimits.from_dict(get_search_engines200_response_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


