# GetHistoryProgrammerToday200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**events** | [**List[GetHistoryProgrammerToday200ResponseEventsInner]**](GetHistoryProgrammerToday200ResponseEventsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_history_programmer_today200_response import GetHistoryProgrammerToday200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoryProgrammerToday200Response from a JSON string
get_history_programmer_today200_response_instance = GetHistoryProgrammerToday200Response.from_json(json)
# print the JSON string representation of the object
print(GetHistoryProgrammerToday200Response.to_json())

# convert the object into a dict
get_history_programmer_today200_response_dict = get_history_programmer_today200_response_instance.to_dict()
# create an instance of GetHistoryProgrammerToday200Response from a dict
get_history_programmer_today200_response_from_dict = GetHistoryProgrammerToday200Response.from_dict(get_history_programmer_today200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


