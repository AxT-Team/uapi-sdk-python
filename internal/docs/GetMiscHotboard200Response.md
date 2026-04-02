# GetMiscHotboard200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**update_time** | **str** | 热榜更新时间。时光机无匹配快照时可能为空字符串。 | [optional] 
**snapshot_time** | **int** | 时光机模式返回的快照实际时间戳（毫秒）。当前热榜模式下通常不返回。 | [optional] 
**list** | [**List[GetMiscHotboard200ResponseOneOfListInner]**](GetMiscHotboard200ResponseOneOfListInner.md) | 热榜条目列表。 | [optional] 
**keyword** | **str** | 搜索关键词。 | [optional] 
**count** | **int** | 匹配到的结果数量。 | [optional] 
**results** | [**List[GetMiscHotboard200ResponseOneOf1ResultsInner]**](GetMiscHotboard200ResponseOneOf1ResultsInner.md) | 搜索结果数组。 | [optional] 
**sources** | **List[str]** | 支持历史数据的平台列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard200_response import GetMiscHotboard200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard200Response from a JSON string
get_misc_hotboard200_response_instance = GetMiscHotboard200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard200Response.to_json())

# convert the object into a dict
get_misc_hotboard200_response_dict = get_misc_hotboard200_response_instance.to_dict()
# create an instance of GetMiscHotboard200Response from a dict
get_misc_hotboard200_response_from_dict = GetMiscHotboard200Response.from_dict(get_misc_hotboard200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


