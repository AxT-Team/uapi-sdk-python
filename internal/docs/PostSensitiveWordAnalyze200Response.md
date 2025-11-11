# PostSensitiveWordAnalyze200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PostSensitiveWordAnalyze200ResponseResultsInner]**](PostSensitiveWordAnalyze200ResponseResultsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from uapi.models.post_sensitive_word_analyze200_response import PostSensitiveWordAnalyze200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSensitiveWordAnalyze200Response from a JSON string
post_sensitive_word_analyze200_response_instance = PostSensitiveWordAnalyze200Response.from_json(json)
# print the JSON string representation of the object
print(PostSensitiveWordAnalyze200Response.to_json())

# convert the object into a dict
post_sensitive_word_analyze200_response_dict = post_sensitive_word_analyze200_response_instance.to_dict()
# create an instance of PostSensitiveWordAnalyze200Response from a dict
post_sensitive_word_analyze200_response_from_dict = PostSensitiveWordAnalyze200Response.from_dict(post_sensitive_word_analyze200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


