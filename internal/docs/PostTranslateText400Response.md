# PostTranslateText400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_translate_text400_response import PostTranslateText400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateText400Response from a JSON string
post_translate_text400_response_instance = PostTranslateText400Response.from_json(json)
# print the JSON string representation of the object
print(PostTranslateText400Response.to_json())

# convert the object into a dict
post_translate_text400_response_dict = post_translate_text400_response_instance.to_dict()
# create an instance of PostTranslateText400Response from a dict
post_translate_text400_response_from_dict = PostTranslateText400Response.from_dict(post_translate_text400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


