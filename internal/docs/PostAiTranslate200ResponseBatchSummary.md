# PostAiTranslate200ResponseBatchSummary

批量翻译汇总信息，仅在批量翻译时返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**success_items** | **int** |  | [optional] 
**failed_items** | **int** |  | [optional] 
**average_quality** | **float** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response_batch_summary import PostAiTranslate200ResponseBatchSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200ResponseBatchSummary from a JSON string
post_ai_translate200_response_batch_summary_instance = PostAiTranslate200ResponseBatchSummary.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200ResponseBatchSummary.to_json())

# convert the object into a dict
post_ai_translate200_response_batch_summary_dict = post_ai_translate200_response_batch_summary_instance.to_dict()
# create an instance of PostAiTranslate200ResponseBatchSummary from a dict
post_ai_translate200_response_batch_summary_from_dict = PostAiTranslate200ResponseBatchSummary.from_dict(post_ai_translate200_response_batch_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


