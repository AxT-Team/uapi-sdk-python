# GetMiscHotboard200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, object]** | 额外信息，不同平台该字段内容不同，例如微博热搜的标签（如&#39;新&#39;、&#39;爆&#39;）。 | [optional] 
**hot_value** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard200_response_list_inner import GetMiscHotboard200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard200ResponseListInner from a JSON string
get_misc_hotboard200_response_list_inner_instance = GetMiscHotboard200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard200ResponseListInner.to_json())

# convert the object into a dict
get_misc_hotboard200_response_list_inner_dict = get_misc_hotboard200_response_list_inner_instance.to_dict()
# create an instance of GetMiscHotboard200ResponseListInner from a dict
get_misc_hotboard200_response_list_inner_from_dict = GetMiscHotboard200ResponseListInner.from_dict(get_misc_hotboard200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


