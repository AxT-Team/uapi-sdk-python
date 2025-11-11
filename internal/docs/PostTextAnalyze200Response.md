# PostTextAnalyze200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characters** | **int** |  | [optional] 
**lines** | **int** |  | [optional] 
**paragraphs** | **int** |  | [optional] 
**sentences** | **int** |  | [optional] 
**words** | **int** |  | [optional] 

## Example

```python
from uapi.models.post_text_analyze200_response import PostTextAnalyze200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAnalyze200Response from a JSON string
post_text_analyze200_response_instance = PostTextAnalyze200Response.from_json(json)
# print the JSON string representation of the object
print(PostTextAnalyze200Response.to_json())

# convert the object into a dict
post_text_analyze200_response_dict = post_text_analyze200_response_instance.to_dict()
# create an instance of PostTextAnalyze200Response from a dict
post_text_analyze200_response_from_dict = PostTextAnalyze200Response.from_dict(post_text_analyze200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


