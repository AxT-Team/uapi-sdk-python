# GetMiscHolidayCalendar200ResponseDataSummary

统计摘要。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_days** | **int** | 查询范围内总天数。 | [optional] 
**weekend_days** | **int** | 查询范围内周末天数。 | [optional] 
**workdays** | **int** | 查询范围内工作日天数（含法定调休上班）。 | [optional] 
**rest_days** | **int** | 查询范围内休息日天数（含周末和法定休假）。 | [optional] 
**holiday_events** | **int** | 按 holiday_type 过滤后的节日事件总数。 | [optional] 
**legal_rest_days** | **int** | 法定休假日天数。 | [optional] 
**legal_workdays** | **int** | 法定调休上班天数。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_data_summary import GetMiscHolidayCalendar200ResponseDataSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseDataSummary from a JSON string
get_misc_holiday_calendar200_response_data_summary_instance = GetMiscHolidayCalendar200ResponseDataSummary.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseDataSummary.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_data_summary_dict = get_misc_holiday_calendar200_response_data_summary_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseDataSummary from a dict
get_misc_holiday_calendar200_response_data_summary_from_dict = GetMiscHolidayCalendar200ResponseDataSummary.from_dict(get_misc_holiday_calendar200_response_data_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


