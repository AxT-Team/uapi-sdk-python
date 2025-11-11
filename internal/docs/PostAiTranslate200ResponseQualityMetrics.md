# PostAiTranslate200ResponseQualityMetrics

翻译质量指标，仅在单个翻译时返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fluency_score** | **float** |  | [optional] 
**accuracy_score** | **float** |  | [optional] 
**completeness_score** | **float** |  | [optional] 
**total_score** | **float** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response_quality_metrics import PostAiTranslate200ResponseQualityMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200ResponseQualityMetrics from a JSON string
post_ai_translate200_response_quality_metrics_instance = PostAiTranslate200ResponseQualityMetrics.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200ResponseQualityMetrics.to_json())

# convert the object into a dict
post_ai_translate200_response_quality_metrics_dict = post_ai_translate200_response_quality_metrics_instance.to_dict()
# create an instance of PostAiTranslate200ResponseQualityMetrics from a dict
post_ai_translate200_response_quality_metrics_from_dict = PostAiTranslate200ResponseQualityMetrics.from_dict(post_ai_translate200_response_quality_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


