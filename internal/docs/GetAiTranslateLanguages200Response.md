# GetAiTranslateLanguages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**GetAiTranslateLanguages200ResponseData**](GetAiTranslateLanguages200ResponseData.md) |  | [optional] 
**performance** | [**GetAiTranslateLanguages200ResponsePerformance**](GetAiTranslateLanguages200ResponsePerformance.md) |  | [optional] 

## Example

```python
from uapi.models.get_ai_translate_languages200_response import GetAiTranslateLanguages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiTranslateLanguages200Response from a JSON string
get_ai_translate_languages200_response_instance = GetAiTranslateLanguages200Response.from_json(json)
# print the JSON string representation of the object
print(GetAiTranslateLanguages200Response.to_json())

# convert the object into a dict
get_ai_translate_languages200_response_dict = get_ai_translate_languages200_response_instance.to_dict()
# create an instance of GetAiTranslateLanguages200Response from a dict
get_ai_translate_languages200_response_from_dict = GetAiTranslateLanguages200Response.from_dict(get_ai_translate_languages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


