# PostSensitiveWordAnalyzeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | 要分析的关键词列表，单次最多100个，每个关键词最长50字符。 | 

## Example

```python
from uapi.models.post_sensitive_word_analyze_request import PostSensitiveWordAnalyzeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSensitiveWordAnalyzeRequest from a JSON string
post_sensitive_word_analyze_request_instance = PostSensitiveWordAnalyzeRequest.from_json(json)
# print the JSON string representation of the object
print(PostSensitiveWordAnalyzeRequest.to_json())

# convert the object into a dict
post_sensitive_word_analyze_request_dict = post_sensitive_word_analyze_request_instance.to_dict()
# create an instance of PostSensitiveWordAnalyzeRequest from a dict
post_sensitive_word_analyze_request_from_dict = PostSensitiveWordAnalyzeRequest.from_dict(post_sensitive_word_analyze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


