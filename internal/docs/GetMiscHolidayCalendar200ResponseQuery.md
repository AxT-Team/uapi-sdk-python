# GetMiscHolidayCalendar200ResponseQuery

请求参数回显。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 日视图查询参数。date 模式下为 YYYY-MM-DD，其余模式下为空字符串。 | [optional] 
**holiday_type** | **str** | 节日筛选类型。 | [optional] 
**include_nearby** | **bool** | 是否开启前后最近节日查询。 | [optional] 
**exclude_past** | **bool** | 是否过滤今天之前已经过去的节日。 | [optional] 
**month** | **str** | 月视图查询参数。month 模式下为 YYYY-MM，其余模式下为空字符串。 | [optional] 
**nearby_limit** | **int** | 前后最近节日返回数量上限。 | [optional] 
**timezone** | **str** | 实际生效的时区。 | [optional] 
**year** | **str** | 年视图查询参数。year 模式下为 YYYY，其余模式下为空字符串。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar200_response_query import GetMiscHolidayCalendar200ResponseQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar200ResponseQuery from a JSON string
get_misc_holiday_calendar200_response_query_instance = GetMiscHolidayCalendar200ResponseQuery.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar200ResponseQuery.to_json())

# convert the object into a dict
get_misc_holiday_calendar200_response_query_dict = get_misc_holiday_calendar200_response_query_instance.to_dict()
# create an instance of GetMiscHolidayCalendar200ResponseQuery from a dict
get_misc_holiday_calendar200_response_query_from_dict = GetMiscHolidayCalendar200ResponseQuery.from_dict(get_misc_holiday_calendar200_response_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


