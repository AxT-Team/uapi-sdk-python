# GetMiscTimestamp200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime_local** | **str** |  | [optional] 
**datetime_utc** | **str** |  | [optional] 
**input** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unix_timestamp** | **int** |  | [optional] 

## Example

```python
from uapi.models.get_misc_timestamp200_response import GetMiscTimestamp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTimestamp200Response from a JSON string
get_misc_timestamp200_response_instance = GetMiscTimestamp200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscTimestamp200Response.to_json())

# convert the object into a dict
get_misc_timestamp200_response_dict = get_misc_timestamp200_response_instance.to_dict()
# create an instance of GetMiscTimestamp200Response from a dict
get_misc_timestamp200_response_from_dict = GetMiscTimestamp200Response.from_dict(get_misc_timestamp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


