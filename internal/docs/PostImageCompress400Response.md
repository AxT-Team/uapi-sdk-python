# PostImageCompress400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 机器可读的错误代码。 | [optional] 
**message** | **str** | 人类可读的错误描述信息。 | [optional] 

## Example

```python
from uapi.models.post_image_compress400_response import PostImageCompress400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageCompress400Response from a JSON string
post_image_compress400_response_instance = PostImageCompress400Response.from_json(json)
# print the JSON string representation of the object
print(PostImageCompress400Response.to_json())

# convert the object into a dict
post_image_compress400_response_dict = post_image_compress400_response_instance.to_dict()
# create an instance of PostImageCompress400Response from a dict
post_image_compress400_response_from_dict = PostImageCompress400Response.from_dict(post_image_compress400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


