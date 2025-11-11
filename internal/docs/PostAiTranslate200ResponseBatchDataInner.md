# PostAiTranslate200ResponseBatchDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_text** | **str** |  | [optional] 
**translated_text** | **str** |  | [optional] 
**confidence_score** | **float** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response_batch_data_inner import PostAiTranslate200ResponseBatchDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200ResponseBatchDataInner from a JSON string
post_ai_translate200_response_batch_data_inner_instance = PostAiTranslate200ResponseBatchDataInner.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200ResponseBatchDataInner.to_json())

# convert the object into a dict
post_ai_translate200_response_batch_data_inner_dict = post_ai_translate200_response_batch_data_inner_instance.to_dict()
# create an instance of PostAiTranslate200ResponseBatchDataInner from a dict
post_ai_translate200_response_batch_data_inner_from_dict = PostAiTranslate200ResponseBatchDataInner.from_dict(post_ai_translate200_response_batch_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


