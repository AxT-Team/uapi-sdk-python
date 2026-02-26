# GetMiscWeather200ResponseMinutelyPrecipDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | 预报时间 ISO8601 | [optional] 
**precip** | **float** | 5分钟累计降水量 mm | [optional] 
**type** | **str** | 降水类型：rain / snow | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_minutely_precip_data_inner import GetMiscWeather200ResponseMinutelyPrecipDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseMinutelyPrecipDataInner from a JSON string
get_misc_weather200_response_minutely_precip_data_inner_instance = GetMiscWeather200ResponseMinutelyPrecipDataInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseMinutelyPrecipDataInner.to_json())

# convert the object into a dict
get_misc_weather200_response_minutely_precip_data_inner_dict = get_misc_weather200_response_minutely_precip_data_inner_instance.to_dict()
# create an instance of GetMiscWeather200ResponseMinutelyPrecipDataInner from a dict
get_misc_weather200_response_minutely_precip_data_inner_from_dict = GetMiscWeather200ResponseMinutelyPrecipDataInner.from_dict(get_misc_weather200_response_minutely_precip_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


