# PostConvertJson200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表操作成功。 | [optional] 
**content** | **str** | 格式化后的JSON字符串，带有标准缩进和换行。 | [optional] 

## Example

```python
from uapi.models.post_convert_json200_response import PostConvertJson200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostConvertJson200Response from a JSON string
post_convert_json200_response_instance = PostConvertJson200Response.from_json(json)
# print the JSON string representation of the object
print(PostConvertJson200Response.to_json())

# convert the object into a dict
post_convert_json200_response_dict = post_convert_json200_response_instance.to_dict()
# create an instance of PostConvertJson200Response from a dict
post_convert_json200_response_from_dict = PostConvertJson200Response.from_dict(post_convert_json200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


