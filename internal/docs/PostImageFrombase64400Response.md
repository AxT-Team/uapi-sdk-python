# PostImageFrombase64400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_image_frombase64400_response import PostImageFrombase64400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageFrombase64400Response from a JSON string
post_image_frombase64400_response_instance = PostImageFrombase64400Response.from_json(json)
# print the JSON string representation of the object
print(PostImageFrombase64400Response.to_json())

# convert the object into a dict
post_image_frombase64400_response_dict = post_image_frombase64400_response_instance.to_dict()
# create an instance of PostImageFrombase64400Response from a dict
post_image_frombase64400_response_from_dict = PostImageFrombase64400Response.from_dict(post_image_frombase64400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


