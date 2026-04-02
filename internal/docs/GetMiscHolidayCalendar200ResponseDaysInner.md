# GetMiscHolidayCalendar200ResponseDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 公历日期（YYYY-MM-DD）。 | [optional] 
**year** | **int** | 公历年份。 | [optional] 
**month** | **int** | 公历月份。 | [optional] 
**day** | **int** | 公历日期（天）。 | [optional] 
**weekday_cn** | **str** | 中文星期，如星期三。 | [optional] 
**is_weekend** | **bool** | 是否为周末。 | [optional] 
**is_workday** | **bool** | 是否为工作日（含法定调休上班日）。 | [optional] 
**is_rest_day** | **bool** | 是否为休息日。 | [optional] 
**is_holiday** | **bool** | 当天是否存在节日、节气或法定事件。 | [optional] 
**legal_holiday_name** | **str** | 法定节假日名称，无则为空或不返回。 | [optional] 
**legal_holiday_type** | **str** | 法定假日类型：rest 或 workday_adjust。 | [optional] 
**solar_festival** | **str** | 公历节日名称。有值时返回。 | [optional] 
**lunar_festival** | **str** | 农历节日名称。有值时返回。 | [optional] 
**solar_term** | **str** | 节气名称。有值时返回。 | [optional] 
**lunar_year** | **int** | 农历年份（数字）。 | [optional] 
**lunar_month** | **int** | 农历月份（数字）。 | [optional] 
**lunar_day** | **int** | 农历日期（数字）。 | [optional] 
**lunar_month_name** | **str** | 农历月份中文名称。 | [optional] 
**lunar_day_name** | **str** | 农历日期中文名称。 | [optional] 
**ganzhi_year** | **str** | 干支年。 | [optional] 
**ganzhi_month** | **str** | 干支月。 | [optional] 
**ganzhi_day** | **str** | 干支日。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_days_inner import GetMiscHolidayCalendar200ResponseDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseDaysInner from a JSON string
get_misc_holiday_calendar200_response_days_inner_instance = GetMiscHolidayCalendar200ResponseDaysInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseDaysInner.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_days_inner_dict = get_misc_holiday_calendar200_response_days_inner_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseDaysInner from a dict
get_misc_holiday_calendar200_response_days_inner_from_dict = GetMiscHolidayCalendar200ResponseDaysInner.from_dict(get_misc_holiday_calendar200_response_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


