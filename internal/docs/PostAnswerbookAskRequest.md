# PostAnswerbookAskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | 你想要提问的问题 | 

## Example

```python
from uapi.models.post_answerbook_ask_request import PostAnswerbookAskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerbookAskRequest from a JSON string
post_answerbook_ask_request_instance = PostAnswerbookAskRequest.from_json(json)
# print the JSON string representation of the object
print(PostAnswerbookAskRequest.to_json())

# convert the object into a dict
post_answerbook_ask_request_dict = post_answerbook_ask_request_instance.to_dict()
# create an instance of PostAnswerbookAskRequest from a dict
post_answerbook_ask_request_from_dict = PostAnswerbookAskRequest.from_dict(post_answerbook_ask_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


