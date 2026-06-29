# PostWatermarkDecode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **float** | 检测结果的置信度，取值范围 0-1。 | [optional] 
**decode_ms** | **float** | 解析耗时（毫秒）。 | [optional] 
**payload** | **str** | 还原出来的标识内容（仅在 present&#x3D;true 时返回）。 | [optional] 
**present** | **bool** | 是否在图片中检测到隐形水印。 | [optional] 

## Example

```python
from uapi.models.post_watermark_decode200_response import PostWatermarkDecode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWatermarkDecode200Response from a JSON string
post_watermark_decode200_response_instance = PostWatermarkDecode200Response.from_json(json)
# print the JSON string representation of the object
print(PostWatermarkDecode200Response.to_json())

# convert the object into a dict
post_watermark_decode200_response_dict = post_watermark_decode200_response_instance.to_dict()
# create an instance of PostWatermarkDecode200Response from a dict
post_watermark_decode200_response_from_dict = PostWatermarkDecode200Response.from_dict(post_watermark_decode200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


