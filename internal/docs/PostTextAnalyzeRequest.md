# PostTextAnalyzeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from uapi.models.post_text_analyze_request import PostTextAnalyzeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextAnalyzeRequest from a JSON string
post_text_analyze_request_instance = PostTextAnalyzeRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextAnalyzeRequest.to_json())

# convert the object into a dict
post_text_analyze_request_dict = post_text_analyze_request_instance.to_dict()
# create an instance of PostTextAnalyzeRequest from a dict
post_text_analyze_request_from_dict = PostTextAnalyzeRequest.from_dict(post_text_analyze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


