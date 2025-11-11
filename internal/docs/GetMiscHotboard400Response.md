# GetMiscHotboard400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_hotboard400_response import GetMiscHotboard400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHotboard400Response from a JSON string
get_misc_hotboard400_response_instance = GetMiscHotboard400Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscHotboard400Response.to_json())

# convert the object into a dict
get_misc_hotboard400_response_dict = get_misc_hotboard400_response_instance.to_dict()
# create an instance of GetMiscHotboard400Response from a dict
get_misc_hotboard400_response_from_dict = GetMiscHotboard400Response.from_dict(get_misc_hotboard400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


