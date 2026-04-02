# GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 事件日期。 | [optional] 
**name** | **str** | 事件名称。 | [optional] 
**type** | **str** | 事件类型。 | [optional] 
**is_workday** | **bool** | 仅调休上班事件返回。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_nearby_next_inner_events_inner import GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner from a JSON string
get_misc_holiday_calendar200_response_nearby_next_inner_events_inner_instance = GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_nearby_next_inner_events_inner_dict = get_misc_holiday_calendar200_response_nearby_next_inner_events_inner_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner from a dict
get_misc_holiday_calendar200_response_nearby_next_inner_events_inner_from_dict = GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner.from_dict(get_misc_holiday_calendar200_response_nearby_next_inner_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


