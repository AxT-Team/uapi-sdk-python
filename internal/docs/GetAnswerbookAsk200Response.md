# GetAnswerbookAsk200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**question** | **str** |  | [optional] 
**answer** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_answerbook_ask200_response import GetAnswerbookAsk200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnswerbookAsk200Response from a JSON string
get_answerbook_ask200_response_instance = GetAnswerbookAsk200Response.from_json(json)
# print the JSON string representation of the object
print(GetAnswerbookAsk200Response.to_json())

# convert the object into a dict
get_answerbook_ask200_response_dict = get_answerbook_ask200_response_instance.to_dict()
# create an instance of GetAnswerbookAsk200Response from a dict
get_answerbook_ask200_response_from_dict = GetAnswerbookAsk200Response.from_dict(get_answerbook_ask200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


