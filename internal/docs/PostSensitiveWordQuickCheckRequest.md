# PostSensitiveWordQuickCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 需要检测的文本内容。支持简体和繁体中文。 | 

## Example

```python
from uapi.models.post_sensitive_word_quick_check_request import PostSensitiveWordQuickCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSensitiveWordQuickCheckRequest from a JSON string
post_sensitive_word_quick_check_request_instance = PostSensitiveWordQuickCheckRequest.from_json(json)
# print the JSON string representation of the object
print(PostSensitiveWordQuickCheckRequest.to_json())

# convert the object into a dict
post_sensitive_word_quick_check_request_dict = post_sensitive_word_quick_check_request_instance.to_dict()
# create an instance of PostSensitiveWordQuickCheckRequest from a dict
post_sensitive_word_quick_check_request_from_dict = PostSensitiveWordQuickCheckRequest.from_dict(post_sensitive_word_quick_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


