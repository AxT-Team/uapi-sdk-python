# PostTextMd5VerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | 用于比对的 MD5 哈希值（32 位小写十六进制字符串）。 | 
**text** | **str** | 待校验的原始文本，会先计算其 MD5 再与 hash 进行比对。 | 

## Example

```python
from uapi.models.post_text_md5_verify_request import PostTextMd5VerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextMd5VerifyRequest from a JSON string
post_text_md5_verify_request_instance = PostTextMd5VerifyRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextMd5VerifyRequest.to_json())

# convert the object into a dict
post_text_md5_verify_request_dict = post_text_md5_verify_request_instance.to_dict()
# create an instance of PostTextMd5VerifyRequest from a dict
post_text_md5_verify_request_from_dict = PostTextMd5VerifyRequest.from_dict(post_text_md5_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


