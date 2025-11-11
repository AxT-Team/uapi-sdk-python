# PostAiTranslate401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate401_response import PostAiTranslate401Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate401Response from a JSON string
post_ai_translate401_response_instance = PostAiTranslate401Response.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate401Response.to_json())

# convert the object into a dict
post_ai_translate401_response_dict = post_ai_translate401_response_instance.to_dict()
# create an instance of PostAiTranslate401Response from a dict
post_ai_translate401_response_from_dict = PostAiTranslate401Response.from_dict(post_ai_translate401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


