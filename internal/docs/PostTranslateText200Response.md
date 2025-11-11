# PostTranslateText200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_lang** | **str** | The source language detected. | [optional] 
**translated_text** | **str** | The translated text. | [optional] 

## Example

```python
from uapi.models.post_translate_text200_response import PostTranslateText200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateText200Response from a JSON string
post_translate_text200_response_instance = PostTranslateText200Response.from_json(json)
# print the JSON string representation of the object
print(PostTranslateText200Response.to_json())

# convert the object into a dict
post_translate_text200_response_dict = post_translate_text200_response_instance.to_dict()
# create an instance of PostTranslateText200Response from a dict
post_translate_text200_response_from_dict = PostTranslateText200Response.from_dict(post_translate_text200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


