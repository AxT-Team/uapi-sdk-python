# PostImageCompress500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 机器可读的错误代码。 | [optional] 
**message** | **str** | 人类可读的错误描述信息。 | [optional] 

## Example

```python
from uapi.models.post_image_compress500_response import PostImageCompress500Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageCompress500Response from a JSON string
post_image_compress500_response_instance = PostImageCompress500Response.from_json(json)
# print the JSON string representation of the object
print(PostImageCompress500Response.to_json())

# convert the object into a dict
post_image_compress500_response_dict = post_image_compress500_response_instance.to_dict()
# create an instance of PostImageCompress500Response from a dict
post_image_compress500_response_from_dict = PostImageCompress500Response.from_dict(post_image_compress500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


