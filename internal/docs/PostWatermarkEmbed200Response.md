# PostWatermarkEmbed200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_chars** | **int** | 在当前图片和配置下，能够嵌入的最大字符数。 | [optional] 
**embed_ms** | **float** | 处理耗时（毫秒）。 | [optional] 
**format** | **str** | 实际输出的图片格式。 | [optional] 
**image_base64** | **str** | 处理完成后的图片 Base64 编码。 | [optional] 
**image_name** | **str** | 原始图片文件名（若请求中包含则返回）。 | [optional] 
**payload** | **str** | 实际嵌入的标识内容。 | [optional] 

## Example

```python
from uapi.models.post_watermark_embed200_response import PostWatermarkEmbed200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWatermarkEmbed200Response from a JSON string
post_watermark_embed200_response_instance = PostWatermarkEmbed200Response.from_json(json)
# print the JSON string representation of the object
print(PostWatermarkEmbed200Response.to_json())

# convert the object into a dict
post_watermark_embed200_response_dict = post_watermark_embed200_response_instance.to_dict()
# create an instance of PostWatermarkEmbed200Response from a dict
post_watermark_embed200_response_from_dict = PostWatermarkEmbed200Response.from_dict(post_watermark_embed200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


