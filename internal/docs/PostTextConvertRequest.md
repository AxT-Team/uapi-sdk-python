# PostTextConvertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 待转换的文本内容 | 
**var_from** | **str** | 源格式类型 | 
**to** | **str** | 目标格式类型 | 
**options** | **Dict[str, object]** | 可选参数（预留，当前未使用） | [optional] 

## Example

```python
from uapi.models.post_text_convert_request import PostTextConvertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextConvertRequest from a JSON string
post_text_convert_request_instance = PostTextConvertRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextConvertRequest.to_json())

# convert the object into a dict
post_text_convert_request_dict = post_text_convert_request_instance.to_dict()
# create an instance of PostTextConvertRequest from a dict
post_text_convert_request_from_dict = PostTextConvertRequest.from_dict(post_text_convert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


