# PostTextMd5Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 需要计算哈希值的文本 | 

## Example

```python
from uapi.models.post_text_md5_request import PostTextMd5Request

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextMd5Request from a JSON string
post_text_md5_request_instance = PostTextMd5Request.from_json(json)
# print the JSON string representation of the object
print(PostTextMd5Request.to_json())

# convert the object into a dict
post_text_md5_request_dict = post_text_md5_request_instance.to_dict()
# create an instance of PostTextMd5Request from a dict
post_text_md5_request_from_dict = PostTextMd5Request.from_dict(post_text_md5_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


