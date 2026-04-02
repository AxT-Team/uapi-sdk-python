# GetMiscHotboard200ResponseOneOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, object]** | 额外信息，不同平台该字段内容不同，例如微博热搜的标签（如“新”“爆”）。 | [optional] 
**hot_value** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**cover** | **str** | 封面图 URL，音乐类热榜返回专辑封面，其他平台一般不返回。 | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard200_response_one_of_list_inner import GetMiscHotboard200ResponseOneOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard200ResponseOneOfListInner from a JSON string
get_misc_hotboard200_response_one_of_list_inner_instance = GetMiscHotboard200ResponseOneOfListInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard200ResponseOneOfListInner.to_json())

# convert the object into a dict
get_misc_hotboard200_response_one_of_list_inner_dict = get_misc_hotboard200_response_one_of_list_inner_instance.to_dict()
# create an instance of GetMiscHotboard200ResponseOneOfListInner from a dict
get_misc_hotboard200_response_one_of_list_inner_from_dict = GetMiscHotboard200ResponseOneOfListInner.from_dict(get_misc_hotboard200_response_one_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


