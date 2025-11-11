# PostSensitiveWordQuickCheck200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**original_text** | **str** |  | [optional] 
**masked_text** | **str** |  | [optional] 
**forbidden_words** | **List[str]** |  | [optional] 

## Example

```python
from uapi.models.post_sensitive_word_quick_check200_response import PostSensitiveWordQuickCheck200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSensitiveWordQuickCheck200Response from a JSON string
post_sensitive_word_quick_check200_response_instance = PostSensitiveWordQuickCheck200Response.from_json(json)
# print the JSON string representation of the object
print(PostSensitiveWordQuickCheck200Response.to_json())

# convert the object into a dict
post_sensitive_word_quick_check200_response_dict = post_sensitive_word_quick_check200_response_instance.to_dict()
# create an instance of PostSensitiveWordQuickCheck200Response from a dict
post_sensitive_word_quick_check200_response_from_dict = PostSensitiveWordQuickCheck200Response.from_dict(post_sensitive_word_quick_check200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


