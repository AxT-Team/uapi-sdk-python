# PostTextMd5VerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | 
**text** | **str** |  | 

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


