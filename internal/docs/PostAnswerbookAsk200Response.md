# PostAnswerbookAsk200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**question** | **str** |  | [optional] 
**answer** | **str** |  | [optional] 

## Example

```python
from uapi.models.post_answerbook_ask200_response import PostAnswerbookAsk200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnswerbookAsk200Response from a JSON string
post_answerbook_ask200_response_instance = PostAnswerbookAsk200Response.from_json(json)
# print the JSON string representation of the object
print(PostAnswerbookAsk200Response.to_json())

# convert the object into a dict
post_answerbook_ask200_response_dict = post_answerbook_ask200_response_instance.to_dict()
# create an instance of PostAnswerbookAsk200Response from a dict
post_answerbook_ask200_response_from_dict = PostAnswerbookAsk200Response.from_dict(post_answerbook_ask200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


