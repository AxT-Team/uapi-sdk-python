# PostTextAesEncryptAdvanced200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | 加密后的密文（Base64编码） | [optional] 
**mode** | **str** | 使用的加密模式 | [optional] 
**padding** | **str** | 使用的填充方式 | [optional] 
**iv** | **str** | 使用的IV（Base64编码）。GCM模式不返回此字段 | [optional] 

## Example

```python
from uapi.models.post_text_aes_encrypt_advanced200_response import PostTextAesEncryptAdvanced200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesEncryptAdvanced200Response from a JSON string
post_text_aes_encrypt_advanced200_response_instance = PostTextAesEncryptAdvanced200Response.from_json(json)
# print the JSON string representation of the object
print(PostTextAesEncryptAdvanced200Response.to_json())

# convert the object into a dict
post_text_aes_encrypt_advanced200_response_dict = post_text_aes_encrypt_advanced200_response_instance.to_dict()
# create an instance of PostTextAesEncryptAdvanced200Response from a dict
post_text_aes_encrypt_advanced200_response_from_dict = PostTextAesEncryptAdvanced200Response.from_dict(post_text_aes_encrypt_advanced200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


