# PostTranslateStream400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | 错误描述 | [optional] 
**code** | **str** | 错误码 | [optional] 

## Example

```python
from uapi.models.post_translate_stream400_response import PostTranslateStream400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTranslateStream400Response from a JSON string
post_translate_stream400_response_instance = PostTranslateStream400Response.from_json(json)
# print the JSON string representation of the object
print(PostTranslateStream400Response.to_json())

# convert the object into a dict
post_translate_stream400_response_dict = post_translate_stream400_response_instance.to_dict()
# create an instance of PostTranslateStream400Response from a dict
post_translate_stream400_response_from_dict = PostTranslateStream400Response.from_dict(post_translate_stream400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


