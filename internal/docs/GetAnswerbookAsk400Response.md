# GetAnswerbookAsk400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_answerbook_ask400_response import GetAnswerbookAsk400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerbookAsk400Response from a JSON string
get_answerbook_ask400_response_instance = GetAnswerbookAsk400Response.from_json(json)
# print the JSON string representation of the object
print(GetAnswerbookAsk400Response.to_json())

# convert the object into a dict
get_answerbook_ask400_response_dict = get_answerbook_ask400_response_instance.to_dict()
# create an instance of GetAnswerbookAsk400Response from a dict
get_answerbook_ask400_response_from_dict = GetAnswerbookAsk400Response.from_dict(get_answerbook_ask400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


