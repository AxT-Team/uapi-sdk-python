# PostImageFrombase64Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_data** | **str** | 图片的Base64 Data URI，必须包含MIME类型头。例如：&#x60;data:image/png;base64,...&#x60; | 

## Example

```python
from uapi.models.post_image_frombase64_request import PostImageFrombase64Request

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageFrombase64Request from a JSON string
post_image_frombase64_request_instance = PostImageFrombase64Request.from_json(json)
# print the JSON string representation of the object
print(PostImageFrombase64Request.to_json())

# convert the object into a dict
post_image_frombase64_request_dict = post_image_frombase64_request_instance.to_dict()
# create an instance of PostImageFrombase64Request from a dict
post_image_frombase64_request_from_dict = PostImageFrombase64Request.from_dict(post_image_frombase64_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


