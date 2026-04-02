# PostTextAesEncryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | 密钥长度必须为 16、24 或 32 字节，分别对应 AES-128、AES-192、AES-256。 | 
**text** | **str** | 待加密的明文文本。 | 

## Example

```python
from uapi.models.post_text_aes_encrypt_request import PostTextAesEncryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesEncryptRequest from a JSON string
post_text_aes_encrypt_request_instance = PostTextAesEncryptRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextAesEncryptRequest.to_json())

# convert the object into a dict
post_text_aes_encrypt_request_dict = post_text_aes_encrypt_request_instance.to_dict()
# create an instance of PostTextAesEncryptRequest from a dict
post_text_aes_encrypt_request_from_dict = PostTextAesEncryptRequest.from_dict(post_text_aes_encrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


