# GetMiscHolidayCalendar200ResponseDataQuery

请求参数回显。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 日视图查询参数（YYYY-MM-DD）。非日视图时可能为空。 | [optional] 
**month** | **str** | 月视图查询参数（YYYY-MM）。非月视图时可能为空。 | [optional] 
**year** | **str** | 年视图查询参数（YYYY）。非年视图时可能为空。 | [optional] 
**timezone** | **str** | 实际生效的时区。 | [optional] 
**holiday_type** | **str** | 节日筛选类型。 | [optional] 
**include_nearby** | **bool** | 是否开启前后最近节日查询。 | [optional] 
**nearby_limit** | **int** | 前后最近节日返回数量上限。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_data_query import GetMiscHolidayCalendar200ResponseDataQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseDataQuery from a JSON string
get_misc_holiday_calendar200_response_data_query_instance = GetMiscHolidayCalendar200ResponseDataQuery.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseDataQuery.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_data_query_dict = get_misc_holiday_calendar200_response_data_query_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseDataQuery from a dict
get_misc_holiday_calendar200_response_data_query_from_dict = GetMiscHolidayCalendar200ResponseDataQuery.from_dict(get_misc_holiday_calendar200_response_data_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


