# GetHistoryProgrammer200ResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**importance** | **int** |  | [optional] 
**relevance_score** | **float** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_history_programmer200_response_events_inner import GetHistoryProgrammer200ResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoryProgrammer200ResponseEventsInner from a JSON string
get_history_programmer200_response_events_inner_instance = GetHistoryProgrammer200ResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(GetHistoryProgrammer200ResponseEventsInner.to_json())

# convert the object into a dict
get_history_programmer200_response_events_inner_dict = get_history_programmer200_response_events_inner_instance.to_dict()
# create an instance of GetHistoryProgrammer200ResponseEventsInner from a dict
get_history_programmer200_response_events_inner_from_dict = GetHistoryProgrammer200ResponseEventsInner.from_dict(get_history_programmer200_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


