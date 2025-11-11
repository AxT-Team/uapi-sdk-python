# PostTranslateTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 待翻译的文本内容。 | 

## Example

```python
from uapi.models.post_translate_text_request import PostTranslateTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateTextRequest from a JSON string
post_translate_text_request_instance = PostTranslateTextRequest.from_json(json)
# print the JSON string representation of the object
print(PostTranslateTextRequest.to_json())

# convert the object into a dict
post_translate_text_request_dict = post_translate_text_request_instance.to_dict()
# create an instance of PostTranslateTextRequest from a dict
post_translate_text_request_from_dict = PostTranslateTextRequest.from_dict(post_translate_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


