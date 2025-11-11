# PostImageSpeechlessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_text** | **str** | 表情包上方的文字内容。你们怎么不说话了，是不是都在偷偷 _______ | [optional] 
**bottom_text** | **str** | 表情包下方的文字内容。求求你_______ | [optional] 

## Example

```python
from uapi.models.post_image_speechless_request import PostImageSpeechlessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageSpeechlessRequest from a JSON string
post_image_speechless_request_instance = PostImageSpeechlessRequest.from_json(json)
# print the JSON string representation of the object
print(PostImageSpeechlessRequest.to_json())

# convert the object into a dict
post_image_speechless_request_dict = post_image_speechless_request_instance.to_dict()
# create an instance of PostImageSpeechlessRequest from a dict
post_image_speechless_request_from_dict = PostImageSpeechlessRequest.from_dict(post_image_speechless_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


