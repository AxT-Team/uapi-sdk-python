# PostImageNsfw400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_image_nsfw400_response import PostImageNsfw400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageNsfw400Response from a JSON string
post_image_nsfw400_response_instance = PostImageNsfw400Response.from_json(json)
# print the JSON string representation of the object
print(PostImageNsfw400Response.to_json())

# convert the object into a dict
post_image_nsfw400_response_dict = post_image_nsfw400_response_instance.to_dict()
# create an instance of PostImageNsfw400Response from a dict
post_image_nsfw400_response_from_dict = PostImageNsfw400Response.from_dict(post_image_nsfw400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


