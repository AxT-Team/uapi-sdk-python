# PostTextAesEncrypt400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_text_aes_encrypt400_response import PostTextAesEncrypt400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAesEncrypt400Response from a JSON string
post_text_aes_encrypt400_response_instance = PostTextAesEncrypt400Response.from_json(json)
# print the JSON string representation of the object
print(PostTextAesEncrypt400Response.to_json())

# convert the object into a dict
post_text_aes_encrypt400_response_dict = post_text_aes_encrypt400_response_instance.to_dict()
# create an instance of PostTextAesEncrypt400Response from a dict
post_text_aes_encrypt400_response_from_dict = PostTextAesEncrypt400Response.from_dict(post_text_aes_encrypt400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


