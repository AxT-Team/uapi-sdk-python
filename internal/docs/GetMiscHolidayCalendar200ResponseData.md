# GetMiscHolidayCalendar200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | 查询模式：day、month、year。 | [optional] 
**query** | [**GetMiscHolidayCalendar200ResponseDataQuery**](GetMiscHolidayCalendar200ResponseDataQuery.md) |  | [optional] 
**summary** | [**GetMiscHolidayCalendar200ResponseDataSummary**](GetMiscHolidayCalendar200ResponseDataSummary.md) |  | [optional] 
**days** | [**List[GetMiscHolidayCalendar200ResponseDataDaysInner]**](GetMiscHolidayCalendar200ResponseDataDaysInner.md) | 日期明细列表。 | [optional] 
**holidays** | [**List[GetMiscHolidayCalendar200ResponseDataHolidaysInner]**](GetMiscHolidayCalendar200ResponseDataHolidaysInner.md) | 节日事件列表。 | [optional] 
**nearby** | [**GetMiscHolidayCalendar200ResponseDataNearby**](GetMiscHolidayCalendar200ResponseDataNearby.md) |  | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_data import GetMiscHolidayCalendar200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseData from a JSON string
get_misc_holiday_calendar200_response_data_instance = GetMiscHolidayCalendar200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseData.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_data_dict = get_misc_holiday_calendar200_response_data_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseData from a dict
get_misc_holiday_calendar200_response_data_from_dict = GetMiscHolidayCalendar200ResponseData.from_dict(get_misc_holiday_calendar200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


