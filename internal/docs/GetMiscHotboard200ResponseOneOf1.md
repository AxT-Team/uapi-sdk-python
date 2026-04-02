# GetMiscHotboard200ResponseOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**keyword** | **str** | 搜索关键词。 | [optional] 
**count** | **int** | 匹配到的结果数量。 | [optional] 
**results** | [**List[GetMiscHotboard200ResponseOneOf1ResultsInner]**](GetMiscHotboard200ResponseOneOf1ResultsInner.md) | 搜索结果数组。 | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard200_response_one_of1 import GetMiscHotboard200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard200ResponseOneOf1 from a JSON string
get_misc_hotboard200_response_one_of1_instance = GetMiscHotboard200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard200ResponseOneOf1.to_json())

# convert the object into a dict
get_misc_hotboard200_response_one_of1_dict = get_misc_hotboard200_response_one_of1_instance.to_dict()
# create an instance of GetMiscHotboard200ResponseOneOf1 from a dict
get_misc_hotboard200_response_one_of1_from_dict = GetMiscHotboard200ResponseOneOf1.from_dict(get_misc_hotboard200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


