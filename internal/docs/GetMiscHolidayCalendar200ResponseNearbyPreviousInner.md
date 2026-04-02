# GetMiscHolidayCalendar200ResponseNearbyPreviousInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 聚合日期。 | [optional] 
**events** | [**List[GetMiscHolidayCalendar200ResponseNearbyPreviousInnerEventsInner]**](GetMiscHolidayCalendar200ResponseNearbyPreviousInnerEventsInner.md) | 该日期上的节日事件列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_nearby_previous_inner import GetMiscHolidayCalendar200ResponseNearbyPreviousInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseNearbyPreviousInner from a JSON string
get_misc_holiday_calendar200_response_nearby_previous_inner_instance = GetMiscHolidayCalendar200ResponseNearbyPreviousInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseNearbyPreviousInner.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_nearby_previous_inner_dict = get_misc_holiday_calendar200_response_nearby_previous_inner_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseNearbyPreviousInner from a dict
get_misc_holiday_calendar200_response_nearby_previous_inner_from_dict = GetMiscHolidayCalendar200ResponseNearbyPreviousInner.from_dict(get_misc_holiday_calendar200_response_nearby_previous_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


