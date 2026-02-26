# PostImageNsfw200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nsfw_score** | **float** | NSFW 内容的置信度分数，范围 0-1，越高表示越可能是敏感内容。 | [optional] 
**normal_score** | **float** | 正常内容的置信度分数，范围 0-1。 | [optional] 
**is_nsfw** | **bool** | 是否判定为 NSFW 内容。 | [optional] 
**label** | **str** | 内容标签，&#39;nsfw&#39; 或 &#39;normal&#39;。 | [optional] 
**suggestion** | **str** | 处理建议：&#39;pass&#39;（通过）、&#39;review&#39;（人工复核）、&#39;block&#39;（拦截）。 | [optional] 
**risk_level** | **str** | 风险等级：&#39;low&#39;、&#39;medium&#39;、&#39;high&#39;。 | [optional] 
**confidence** | **float** | 模型对当前判断的置信度。 | [optional] 
**inference_time_ms** | **float** | 模型推理耗时，单位毫秒。 | [optional] 

## Example

```python
from uapi.models.post_image_nsfw200_response import PostImageNsfw200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageNsfw200Response from a JSON string
post_image_nsfw200_response_instance = PostImageNsfw200Response.from_json(json)
# print the JSON string representation of the object
print(PostImageNsfw200Response.to_json())

# convert the object into a dict
post_image_nsfw200_response_dict = post_image_nsfw200_response_instance.to_dict()
# create an instance of PostImageNsfw200Response from a dict
post_image_nsfw200_response_from_dict = PostImageNsfw200Response.from_dict(post_image_nsfw200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


