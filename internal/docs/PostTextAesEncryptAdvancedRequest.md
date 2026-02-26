# PostTextAesEncryptAdvancedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 待加密的明文文本 | 
**key** | **str** | 加密密钥（支持任意长度） | 
**mode** | **str** | 加密模式：GCM/CBC/ECB/CTR/OFB/CFB（可选，默认GCM） | [optional] 
**padding** | **str** | 填充方式：PKCS7/ZERO/NONE（可选，默认PKCS7） | [optional] 
**iv** | **str** | 自定义IV（可选，Base64编码，16字节）。GCM模式无需此参数 | [optional] 
**output_format** | **str** | 输出格式：base64（默认）或hex | [optional] 

## Example

```python
from uapi.models.post_text_aes_encrypt_advanced_request import PostTextAesEncryptAdvancedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesEncryptAdvancedRequest from a JSON string
post_text_aes_encrypt_advanced_request_instance = PostTextAesEncryptAdvancedRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextAesEncryptAdvancedRequest.to_json())

# convert the object into a dict
post_text_aes_encrypt_advanced_request_dict = post_text_aes_encrypt_advanced_request_instance.to_dict()
# create an instance of PostTextAesEncryptAdvancedRequest from a dict
post_text_aes_encrypt_advanced_request_from_dict = PostTextAesEncryptAdvancedRequest.from_dict(post_text_aes_encrypt_advanced_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


