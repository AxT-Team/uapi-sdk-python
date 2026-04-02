# GetMiscHolidayCalendar200ResponseNearby

前后最近节日，仅 include_nearby=true 且 date 模式返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | [**List[GetMiscHolidayCalendar200ResponseNearbyPreviousInner]**](GetMiscHolidayCalendar200ResponseNearbyPreviousInner.md) | 当前查询日期之前最近的节日列表（按时间倒序）。 | [optional] 
**next** | [**List[GetMiscHolidayCalendar200ResponseNearbyNextInner]**](GetMiscHolidayCalendar200ResponseNearbyNextInner.md) | 当前查询日期之后最近的节日列表（按时间正序）。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_nearby import GetMiscHolidayCalendar200ResponseNearby

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseNearby from a JSON string
get_misc_holiday_calendar200_response_nearby_instance = GetMiscHolidayCalendar200ResponseNearby.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseNearby.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_nearby_dict = get_misc_holiday_calendar200_response_nearby_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseNearby from a dict
get_misc_holiday_calendar200_response_nearby_from_dict = GetMiscHolidayCalendar200ResponseNearby.from_dict(get_misc_holiday_calendar200_response_nearby_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


