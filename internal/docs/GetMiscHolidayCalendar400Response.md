# GetMiscHolidayCalendar400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 业务状态码，400 表示请求参数错误。 | [optional] 
**message** | **str** | 具体错误原因提示。 | [optional] 

## Example

```python
from uapi.models.get_misc_holiday_calendar400_response import GetMiscHolidayCalendar400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscHolidayCalendar400Response from a JSON string
get_misc_holiday_calendar400_response_instance = GetMiscHolidayCalendar400Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscHolidayCalendar400Response.to_json())

# convert the object into a dict
get_misc_holiday_calendar400_response_dict = get_misc_holiday_calendar400_response_instance.to_dict()
# create an instance of GetMiscHolidayCalendar400Response from a dict
get_misc_holiday_calendar400_response_from_dict = GetMiscHolidayCalendar400Response.from_dict(get_misc_holiday_calendar400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


