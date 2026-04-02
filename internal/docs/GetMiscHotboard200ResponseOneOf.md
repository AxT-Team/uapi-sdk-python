# GetMiscHotboard200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**update_time** | **str** | 热榜更新时间。时光机无匹配快照时可能为空字符串。 | [optional] 
**snapshot_time** | **int** | 时光机模式返回的快照实际时间戳（毫秒）。当前热榜模式下通常不返回。 | [optional] 
**list** | [**List[GetMiscHotboard200ResponseOneOfListInner]**](GetMiscHotboard200ResponseOneOfListInner.md) | 热榜条目列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard200_response_one_of import GetMiscHotboard200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard200ResponseOneOf from a JSON string
get_misc_hotboard200_response_one_of_instance = GetMiscHotboard200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard200ResponseOneOf.to_json())

# convert the object into a dict
get_misc_hotboard200_response_one_of_dict = get_misc_hotboard200_response_one_of_instance.to_dict()
# create an instance of GetMiscHotboard200ResponseOneOf from a dict
get_misc_hotboard200_response_one_of_from_dict = GetMiscHotboard200ResponseOneOf.from_dict(get_misc_hotboard200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


