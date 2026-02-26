# GetMiscHolidayCalendar200ResponseDataNearby

前后最近节日，仅 include_nearby=true 且 date 模式返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | [**List[GetMiscHolidayCalendar200ResponseDataNearbyPreviousInner]**](GetMiscHolidayCalendar200ResponseDataNearbyPreviousInner.md) | 当前查询日期之前最近的节日列表（按时间倒序）。 | [optional] 
**next** | [**List[GetMiscHolidayCalendar200ResponseDataNearbyNextInner]**](GetMiscHolidayCalendar200ResponseDataNearbyNextInner.md) | 当前查询日期之后最近的节日列表（按时间正序）。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_data_nearby import GetMiscHolidayCalendar200ResponseDataNearby

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseDataNearby from a JSON string
get_misc_holiday_calendar200_response_data_nearby_instance = GetMiscHolidayCalendar200ResponseDataNearby.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseDataNearby.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_data_nearby_dict = get_misc_holiday_calendar200_response_data_nearby_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseDataNearby from a dict
get_misc_holiday_calendar200_response_data_nearby_from_dict = GetMiscHolidayCalendar200ResponseDataNearby.from_dict(get_misc_holiday_calendar200_response_data_nearby_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


