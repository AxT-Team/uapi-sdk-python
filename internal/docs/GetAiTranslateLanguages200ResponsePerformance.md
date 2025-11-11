# GetAiTranslateLanguages200ResponsePerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast_mode_available** | **bool** |  | [optional] 
**batch_translation_available** | **bool** |  | [optional] 
**max_text_length** | **int** |  | [optional] 
**max_batch_size** | **int** |  | [optional] 
**typical_response_time_ms** | [**GetAiTranslateLanguages200ResponsePerformanceTypicalResponseTimeMs**](GetAiTranslateLanguages200ResponsePerformanceTypicalResponseTimeMs.md) |  | [optional] 

## Example

```python
from uapi.models.get_ai_translate_languages200_response_performance import GetAiTranslateLanguages200ResponsePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiTranslateLanguages200ResponsePerformance from a JSON string
get_ai_translate_languages200_response_performance_instance = GetAiTranslateLanguages200ResponsePerformance.from_json(json)
# print the JSON string representation of the object
print(GetAiTranslateLanguages200ResponsePerformance.to_json())

# convert the object into a dict
get_ai_translate_languages200_response_performance_dict = get_ai_translate_languages200_response_performance_instance.to_dict()
# create an instance of GetAiTranslateLanguages200ResponsePerformance from a dict
get_ai_translate_languages200_response_performance_from_dict = GetAiTranslateLanguages200ResponsePerformance.from_dict(get_ai_translate_languages200_response_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


