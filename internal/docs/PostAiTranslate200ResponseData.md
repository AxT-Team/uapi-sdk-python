# PostAiTranslate200ResponseData

单个翻译的详细结果，仅在单个翻译时返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_text** | **str** |  | [optional] 
**translated_text** | **str** |  | [optional] 
**detected_lang** | **str** |  | [optional] 
**confidence_score** | **float** |  | [optional] 
**alternatives** | **List[str]** |  | [optional] 
**explanation** | [**PostAiTranslate200ResponseDataExplanation**](PostAiTranslate200ResponseDataExplanation.md) |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate200_response_data import PostAiTranslate200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate200ResponseData from a JSON string
post_ai_translate200_response_data_instance = PostAiTranslate200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate200ResponseData.to_json())

# convert the object into a dict
post_ai_translate200_response_data_dict = post_ai_translate200_response_data_instance.to_dict()
# create an instance of PostAiTranslate200ResponseData from a dict
post_ai_translate200_response_data_from_dict = PostAiTranslate200ResponseData.from_dict(post_ai_translate200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


