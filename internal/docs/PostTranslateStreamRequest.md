# PostTranslateStreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 待翻译的文本内容 | 
**to_lang** | **str** | 目标语言，支持：中文、英文 | 
**from_lang** | **str** | 源语言，支持：中文、英文、auto（自动检测）。默认为auto | [optional] [default to 'auto']
**tone** | **str** | 语气参数，可选 | [optional] 

## Example

```python
from uapi.models.post_translate_stream_request import PostTranslateStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateStreamRequest from a JSON string
post_translate_stream_request_instance = PostTranslateStreamRequest.from_json(json)
# print the JSON string representation of the object
print(PostTranslateStreamRequest.to_json())

# convert the object into a dict
post_translate_stream_request_dict = post_translate_stream_request_instance.to_dict()
# create an instance of PostTranslateStreamRequest from a dict
post_translate_stream_request_from_dict = PostTranslateStreamRequest.from_dict(post_translate_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


