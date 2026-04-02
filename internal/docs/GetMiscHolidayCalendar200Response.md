# GetMiscHolidayCalendar200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | 查询模式：day、month、year。 | [optional] 
**query** | [**GetMiscHolidayCalendar200ResponseQuery**](GetMiscHolidayCalendar200ResponseQuery.md) |  | [optional] 
**summary** | [**GetMiscHolidayCalendar200ResponseSummary**](GetMiscHolidayCalendar200ResponseSummary.md) |  | [optional] 
**days** | [**List[GetMiscHolidayCalendar200ResponseDaysInner]**](GetMiscHolidayCalendar200ResponseDaysInner.md) | 日期明细列表。 | [optional] 
**holidays** | [**List[GetMiscHolidayCalendar200ResponseHolidaysInner]**](GetMiscHolidayCalendar200ResponseHolidaysInner.md) | 节日事件列表。 | [optional] 
**nearby** | [**GetMiscHolidayCalendar200ResponseNearby**](GetMiscHolidayCalendar200ResponseNearby.md) |  | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response import GetMiscHolidayCalendar200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200Response from a JSON string
get_misc_holiday_calendar200_response_instance = GetMiscHolidayCalendar200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200Response.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_dict = get_misc_holiday_calendar200_response_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200Response from a dict
get_misc_holiday_calendar200_response_from_dict = GetMiscHolidayCalendar200Response.from_dict(get_misc_holiday_calendar200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


