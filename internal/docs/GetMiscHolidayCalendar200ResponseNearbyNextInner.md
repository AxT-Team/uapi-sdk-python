# GetMiscHolidayCalendar200ResponseNearbyNextInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 聚合日期。 | [optional] 
**events** | [**List[GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner]**](GetMiscHolidayCalendar200ResponseNearbyNextInnerEventsInner.md) | 该日期上的节日事件列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_nearby_next_inner import GetMiscHolidayCalendar200ResponseNearbyNextInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseNearbyNextInner from a JSON string
get_misc_holiday_calendar200_response_nearby_next_inner_instance = GetMiscHolidayCalendar200ResponseNearbyNextInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseNearbyNextInner.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_nearby_next_inner_dict = get_misc_holiday_calendar200_response_nearby_next_inner_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseNearbyNextInner from a dict
get_misc_holiday_calendar200_response_nearby_next_inner_from_dict = GetMiscHolidayCalendar200ResponseNearbyNextInner.from_dict(get_misc_holiday_calendar200_response_nearby_next_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


