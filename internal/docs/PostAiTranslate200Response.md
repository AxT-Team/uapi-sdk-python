# PostAiTranslate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**is_batch** | **bool** | 标识是否为批量翻译请求。 | [optional] 
**data** | [**PostAiTranslate200ResponseData**](PostAiTranslate200ResponseData.md) |  | [optional] 
**batch_data** | [**List[PostAiTranslate200ResponseBatchDataInner]**](PostAiTranslate200ResponseBatchDataInner.md) | 批量翻译结果列表，仅在批量翻译时返回。 | [optional] 
**batch_summary** | [**PostAiTranslate200ResponseBatchSummary**](PostAiTranslate200ResponseBatchSummary.md) |  | [optional] 
**performance** | [**PostAiTranslate200ResponsePerformance**](PostAiTranslate200ResponsePerformance.md) |  | [optional] 
**quality_metrics** | [**PostAiTranslate200ResponseQualityMetrics**](PostAiTranslate200ResponseQualityMetrics.md) |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response import PostAiTranslate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200Response from a JSON string
post_ai_translate200_response_instance = PostAiTranslate200Response.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200Response.to_json())

# convert the object into a dict
post_ai_translate200_response_dict = post_ai_translate200_response_instance.to_dict()
# create an instance of PostAiTranslate200Response from a dict
post_ai_translate200_response_from_dict = PostAiTranslate200Response.from_dict(post_ai_translate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


