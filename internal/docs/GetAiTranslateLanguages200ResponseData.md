# GetAiTranslateLanguages200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languages** | [**List[GetAiTranslateLanguages200ResponseDataLanguagesInner]**](GetAiTranslateLanguages200ResponseDataLanguagesInner.md) |  | [optional] 
**styles** | [**List[GetAiTranslateLanguages200ResponseDataStylesInner]**](GetAiTranslateLanguages200ResponseDataStylesInner.md) |  | [optional] 
**contexts** | [**List[GetAiTranslateLanguages200ResponseDataContextsInner]**](GetAiTranslateLanguages200ResponseDataContextsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_ai_translate_languages200_response_data import GetAiTranslateLanguages200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiTranslateLanguages200ResponseData from a JSON string
get_ai_translate_languages200_response_data_instance = GetAiTranslateLanguages200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAiTranslateLanguages200ResponseData.to_json())

# convert the object into a dict
get_ai_translate_languages200_response_data_dict = get_ai_translate_languages200_response_data_instance.to_dict()
# create an instance of GetAiTranslateLanguages200ResponseData from a dict
get_ai_translate_languages200_response_data_from_dict = GetAiTranslateLanguages200ResponseData.from_dict(get_ai_translate_languages200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


