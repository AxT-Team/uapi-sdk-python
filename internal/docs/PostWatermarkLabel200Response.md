# PostWatermarkLabel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **List[str]** | 本次实际注入成功的标识层级，可能包含 &#39;watermark&#39;、&#39;explicit&#39;、&#39;metadata&#39;。 | [optional] 
**capacity_chars** | **int** | 当前配置下的隐形水印最大容量（若开启）。 | [optional] 
**content_producer** | **str** | 成功写入的服务提供者编码。 | [optional] 
**format** | **str** | 实际输出的图片格式。 | [optional] 
**image_base64** | **str** | 处理完成后的图片 Base64 编码。 | [optional] 
**image_name** | **str** | 原始图片文件名（若请求中包含则返回）。 | [optional] 
**watermark_payload** | **str** | 成功嵌入的隐形水印内容（若开启）。 | [optional] 

## Example

```python
from uapi.models.post_watermark_label200_response import PostWatermarkLabel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWatermarkLabel200Response from a JSON string
post_watermark_label200_response_instance = PostWatermarkLabel200Response.from_json(json)
# print the JSON string representation of the object
print(PostWatermarkLabel200Response.to_json())

# convert the object into a dict
post_watermark_label200_response_dict = post_watermark_label200_response_instance.to_dict()
# create an instance of PostWatermarkLabel200Response from a dict
post_watermark_label200_response_from_dict = PostWatermarkLabel200Response.from_dict(post_watermark_label200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


