# PostTranslateText500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_translate_text500_response import PostTranslateText500Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateText500Response from a JSON string
post_translate_text500_response_instance = PostTranslateText500Response.from_json(json)
# print the JSON string representation of the object
print(PostTranslateText500Response.to_json())

# convert the object into a dict
post_translate_text500_response_dict = post_translate_text500_response_instance.to_dict()
# create an instance of PostTranslateText500Response from a dict
post_translate_text500_response_from_dict = PostTranslateText500Response.from_dict(post_translate_text500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


