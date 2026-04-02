# PostAiTranslate200ResponseData

翻译结果的详细信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translated_text** | **str** |  | [optional] 

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


