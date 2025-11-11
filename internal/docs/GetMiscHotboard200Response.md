# GetMiscHotboard200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetMiscHotboard200ResponseListInner]**](GetMiscHotboard200ResponseListInner.md) | 热榜条目列表。 | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **str** |  | [optional] 

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


