# GetImageTobase64502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_image_tobase64502_response import GetImageTobase64502Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageTobase64502Response from a JSON string
get_image_tobase64502_response_instance = GetImageTobase64502Response.from_json(json)
# print the JSON string representation of the object
print(GetImageTobase64502Response.to_json())

# convert the object into a dict
get_image_tobase64502_response_dict = get_image_tobase64502_response_instance.to_dict()
# create an instance of GetImageTobase64502Response from a dict
get_image_tobase64502_response_from_dict = GetImageTobase64502Response.from_dict(get_image_tobase64502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


