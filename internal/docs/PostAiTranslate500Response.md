# PostAiTranslate500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**is_batch** | **bool** |  | [optional] 

## Example

```python
from uapi.models.post_ai_translate500_response import PostAiTranslate500Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAiTranslate500Response from a JSON string
post_ai_translate500_response_instance = PostAiTranslate500Response.from_json(json)
# print the JSON string representation of the object
print(PostAiTranslate500Response.to_json())

# convert the object into a dict
post_ai_translate500_response_dict = post_ai_translate500_response_instance.to_dict()
# create an instance of PostAiTranslate500Response from a dict
post_ai_translate500_response_from_dict = PostAiTranslate500Response.from_dict(post_ai_translate500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


