# GetDailyWord200ResponseWordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | **str** |  | [optional] 
**examples** | [**List[GetDailyWord200ResponseWordsInnerExamplesInner]**](GetDailyWord200ResponseWordsInnerExamplesInner.md) |  | [optional] 
**phonetic** | **str** |  | [optional] 
**word** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_daily_word200_response_words_inner import GetDailyWord200ResponseWordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyWord200ResponseWordsInner from a JSON string
get_daily_word200_response_words_inner_instance = GetDailyWord200ResponseWordsInner.from_json(json)
# print the JSON string representation of the object
print(GetDailyWord200ResponseWordsInner.to_json())

# convert the object into a dict
get_daily_word200_response_words_inner_dict = get_daily_word200_response_words_inner_instance.to_dict()
# create an instance of GetDailyWord200ResponseWordsInner from a dict
get_daily_word200_response_words_inner_from_dict = GetDailyWord200ResponseWordsInner.from_dict(get_daily_word200_response_words_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


