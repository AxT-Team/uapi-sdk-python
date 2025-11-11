# PostTextBase64Decode400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_text_base64_decode400_response import PostTextBase64Decode400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextBase64Decode400Response from a JSON string
post_text_base64_decode400_response_instance = PostTextBase64Decode400Response.from_json(json)
# print the JSON string representation of the object
print(PostTextBase64Decode400Response.to_json())

# convert the object into a dict
post_text_base64_decode400_response_dict = post_text_base64_decode400_response_instance.to_dict()
# create an instance of PostTextBase64Decode400Response from a dict
post_text_base64_decode400_response_from_dict = PostTextBase64Decode400Response.from_dict(post_text_base64_decode400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


