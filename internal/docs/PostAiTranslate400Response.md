# PostAiTranslate400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate400_response import PostAiTranslate400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate400Response from a JSON string
post_ai_translate400_response_instance = PostAiTranslate400Response.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate400Response.to_json())

# convert the object into a dict
post_ai_translate400_response_dict = post_ai_translate400_response_instance.to_dict()
# create an instance of PostAiTranslate400Response from a dict
post_ai_translate400_response_from_dict = PostAiTranslate400Response.from_dict(post_ai_translate400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


