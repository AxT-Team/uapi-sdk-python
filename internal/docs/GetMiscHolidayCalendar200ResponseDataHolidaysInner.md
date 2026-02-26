# GetMiscHolidayCalendar200ResponseDataHolidaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 事件日期（YYYY-MM-DD）。 | [optional] 
**name** | **str** | 事件名称。 | [optional] 
**type** | **str** | 事件类型。 | [optional] 
**is_workday** | **bool** | 仅 legal_workday_adjust 场景有意义。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_data_holidays_inner import GetMiscHolidayCalendar200ResponseDataHolidaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseDataHolidaysInner from a JSON string
get_misc_holiday_calendar200_response_data_holidays_inner_instance = GetMiscHolidayCalendar200ResponseDataHolidaysInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseDataHolidaysInner.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_data_holidays_inner_dict = get_misc_holiday_calendar200_response_data_holidays_inner_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseDataHolidaysInner from a dict
get_misc_holiday_calendar200_response_data_holidays_inner_from_dict = GetMiscHolidayCalendar200ResponseDataHolidaysInner.from_dict(get_misc_holiday_calendar200_response_data_holidays_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


