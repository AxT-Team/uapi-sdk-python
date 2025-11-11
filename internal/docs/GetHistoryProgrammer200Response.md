# GetHistoryProgrammer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**events** | [**List[GetHistoryProgrammer200ResponseEventsInner]**](GetHistoryProgrammer200ResponseEventsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_history_programmer200_response import GetHistoryProgrammer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoryProgrammer200Response from a JSON string
get_history_programmer200_response_instance = GetHistoryProgrammer200Response.from_json(json)
# print the JSON string representation of the object
print(GetHistoryProgrammer200Response.to_json())

# convert the object into a dict
get_history_programmer200_response_dict = get_history_programmer200_response_instance.to_dict()
# create an instance of GetHistoryProgrammer200Response from a dict
get_history_programmer200_response_from_dict = GetHistoryProgrammer200Response.from_dict(get_history_programmer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


