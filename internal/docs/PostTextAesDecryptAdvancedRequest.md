# PostTextAesDecryptAdvancedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 待解密的密文（Base64编码）。此值来自加密接口返回的ciphertext字段 | 
**key** | **str** | 解密密钥（必须与加密时相同） | 
**mode** | **str** | 加密模式（必须与加密时相同）：GCM/CBC/ECB/CTR/OFB/CFB | 
**padding** | **str** | 填充方式（可选，必须与加密时相同）：PKCS7/ZERO/NONE。GCM模式默认为NONE | [optional] 
**iv** | **str** | 初始化向量（非GCM模式必须提供，Base64编码）。此值来自加密接口返回的iv字段 | [optional] 

## Example

```python
from uapi.models.post_text_aes_decrypt_advanced_request import PostTextAesDecryptAdvancedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesDecryptAdvancedRequest from a JSON string
post_text_aes_decrypt_advanced_request_instance = PostTextAesDecryptAdvancedRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextAesDecryptAdvancedRequest.to_json())

# convert the object into a dict
post_text_aes_decrypt_advanced_request_dict = post_text_aes_decrypt_advanced_request_instance.to_dict()
# create an instance of PostTextAesDecryptAdvancedRequest from a dict
post_text_aes_decrypt_advanced_request_from_dict = PostTextAesDecryptAdvancedRequest.from_dict(post_text_aes_decrypt_advanced_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


