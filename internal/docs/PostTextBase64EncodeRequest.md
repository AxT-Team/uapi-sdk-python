# PostTextBase64EncodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from uapi.models.post_text_base64_encode_request import PostTextBase64EncodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextBase64EncodeRequest from a JSON string
post_text_base64_encode_request_instance = PostTextBase64EncodeRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextBase64EncodeRequest.to_json())

# convert the object into a dict
post_text_base64_encode_request_dict = post_text_base64_encode_request_instance.to_dict()
# create an instance of PostTextBase64EncodeRequest from a dict
post_text_base64_encode_request_from_dict = PostTextBase64EncodeRequest.from_dict(post_text_base64_encode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


