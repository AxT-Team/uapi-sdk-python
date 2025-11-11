# PostAiTranslate200ResponsePerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_time_ms** | **int** |  | [optional] 
**cache_hit** | **bool** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response_performance import PostAiTranslate200ResponsePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200ResponsePerformance from a JSON string
post_ai_translate200_response_performance_instance = PostAiTranslate200ResponsePerformance.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200ResponsePerformance.to_json())

# convert the object into a dict
post_ai_translate200_response_performance_dict = post_ai_translate200_response_performance_instance.to_dict()
# create an instance of PostAiTranslate200ResponsePerformance from a dict
post_ai_translate200_response_performance_from_dict = PostAiTranslate200ResponsePerformance.from_dict(post_ai_translate200_response_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


