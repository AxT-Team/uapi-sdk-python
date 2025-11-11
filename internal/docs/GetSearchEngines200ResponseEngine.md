# GetSearchEngines200ResponseEngine

搜索引擎的基本信息

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 引擎标识名称 | [optional] 
**display_name** | **str** | 引擎显示名称 | [optional] 
**description** | **str** | 引擎描述 | [optional] 
**available** | **bool** | 引擎是否可用 | [optional] 
**version** | **str** | 引擎版本号 | [optional] 
**features** | **List[str]** | 支持的特性列表 | [optional] 

## Example

```python
from uapi.models.get_search_engines200_response_engine import GetSearchEngines200ResponseEngine

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchEngines200ResponseEngine from a JSON string
get_search_engines200_response_engine_instance = GetSearchEngines200ResponseEngine.from_json(json)
# print the JSON string representation of the object
print(GetSearchEngines200ResponseEngine.to_json())

# convert the object into a dict
get_search_engines200_response_engine_dict = get_search_engines200_response_engine_instance.to_dict()
# create an instance of GetSearchEngines200ResponseEngine from a dict
get_search_engines200_response_engine_from_dict = GetSearchEngines200ResponseEngine.from_dict(get_search_engines200_response_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


