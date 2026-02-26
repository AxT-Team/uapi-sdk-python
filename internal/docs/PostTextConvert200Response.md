# PostTextConvert200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | 转换结果 | [optional] 
**var_from** | **str** | 源格式 | [optional] 
**to** | **str** | 目标格式 | [optional] 
**length** | **int** | 结果长度 | [optional] 
**info** | **str** | 额外信息（如哈希不可逆提示） | [optional] 

## Example

```python
from uapi.models.post_text_convert200_response import PostTextConvert200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextConvert200Response from a JSON string
post_text_convert200_response_instance = PostTextConvert200Response.from_json(json)
# print the JSON string representation of the object
print(PostTextConvert200Response.to_json())

# convert the object into a dict
post_text_convert200_response_dict = post_text_convert200_response_instance.to_dict()
# create an instance of PostTextConvert200Response from a dict
post_text_convert200_response_from_dict = PostTextConvert200Response.from_dict(post_text_convert200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


