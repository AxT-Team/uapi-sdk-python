# PostImageFrombase64200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表成功。 | [optional] 
**image_url** | **str** | 图片保存后在服务器上的绝对访问URL。 | [optional] 
**msg** | **str** | 操作结果描述。 | [optional] 

## Example

```python
from uapi.models.post_image_frombase64200_response import PostImageFrombase64200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageFrombase64200Response from a JSON string
post_image_frombase64200_response_instance = PostImageFrombase64200Response.from_json(json)
# print the JSON string representation of the object
print(PostImageFrombase64200Response.to_json())

# convert the object into a dict
post_image_frombase64200_response_dict = post_image_frombase64200_response_instance.to_dict()
# create an instance of PostImageFrombase64200Response from a dict
post_image_frombase64200_response_from_dict = PostImageFrombase64200Response.from_dict(post_image_frombase64200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


