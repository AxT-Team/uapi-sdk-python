# PostTextAesDecryptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | 密钥，长度必须为16、24或32字节，对应AES-128/192/256。 | 
**text** | **str** | Base64编码的密文。 | 
**nonce** | **str** | 16�ֽڵ�IV/Nonce����Ϊ16���ַ� | 

## Example

```python
from uapi.models.post_text_aes_decrypt_request import PostTextAesDecryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesDecryptRequest from a JSON string
post_text_aes_decrypt_request_instance = PostTextAesDecryptRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextAesDecryptRequest.to_json())

# convert the object into a dict
post_text_aes_decrypt_request_dict = post_text_aes_decrypt_request_instance.to_dict()
# create an instance of PostTextAesDecryptRequest from a dict
post_text_aes_decrypt_request_from_dict = PostTextAesDecryptRequest.from_dict(post_text_aes_decrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


