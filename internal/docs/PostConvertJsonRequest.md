# PostConvertJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | 需要被格式化的原始JSON字符串。 | 

## Example

```python
from uapi.models.post_convert_json_request import PostConvertJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostConvertJsonRequest from a JSON string
post_convert_json_request_instance = PostConvertJsonRequest.from_json(json)
# print the JSON string representation of the object
print(PostConvertJsonRequest.to_json())

# convert the object into a dict
post_convert_json_request_dict = post_convert_json_request_instance.to_dict()
# create an instance of PostConvertJsonRequest from a dict
post_convert_json_request_from_dict = PostConvertJsonRequest.from_dict(post_convert_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


