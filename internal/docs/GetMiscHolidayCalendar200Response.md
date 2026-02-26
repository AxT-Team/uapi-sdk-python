# GetMiscHolidayCalendar200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**GetMiscHolidayCalendar200ResponseData**](GetMiscHolidayCalendar200ResponseData.md) |  | [optional] 

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


