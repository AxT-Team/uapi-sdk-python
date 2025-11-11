# GetMiscWorldtime200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **str** |  | [optional] 
**offset_seconds** | **int** |  | [optional] 
**offset_string** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**timestamp_unix** | **int** |  | [optional] 
**timezone** | **str** |  | [optional] 
**weekday** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_worldtime200_response import GetMiscWorldtime200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWorldtime200Response from a JSON string
get_misc_worldtime200_response_instance = GetMiscWorldtime200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscWorldtime200Response.to_json())

# convert the object into a dict
get_misc_worldtime200_response_dict = get_misc_worldtime200_response_instance.to_dict()
# create an instance of GetMiscWorldtime200Response from a dict
get_misc_worldtime200_response_from_dict = GetMiscWorldtime200Response.from_dict(get_misc_worldtime200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


