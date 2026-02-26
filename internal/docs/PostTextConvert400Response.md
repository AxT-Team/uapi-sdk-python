# PostTextConvert400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_details** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_text_convert400_response import PostTextConvert400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextConvert400Response from a JSON string
post_text_convert400_response_instance = PostTextConvert400Response.from_json(json)
# print the JSON string representation of the object
print(PostTextConvert400Response.to_json())

# convert the object into a dict
post_text_convert400_response_dict = post_text_convert400_response_instance.to_dict()
# create an instance of PostTextConvert400Response from a dict
post_text_convert400_response_from_dict = PostTextConvert400Response.from_dict(post_text_convert400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


