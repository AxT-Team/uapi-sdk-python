# PostTextAnalyze400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_text_analyze400_response import PostTextAnalyze400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAnalyze400Response from a JSON string
post_text_analyze400_response_instance = PostTextAnalyze400Response.from_json(json)
# print the JSON string representation of the object
print(PostTextAnalyze400Response.to_json())

# convert the object into a dict
post_text_analyze400_response_dict = post_text_analyze400_response_instance.to_dict()
# create an instance of PostTextAnalyze400Response from a dict
post_text_analyze400_response_from_dict = PostTextAnalyze400Response.from_dict(post_text_analyze400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


