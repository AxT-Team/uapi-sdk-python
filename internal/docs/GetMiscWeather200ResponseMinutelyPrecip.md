# GetMiscWeather200ResponseMinutelyPrecip

分钟级降水预报（minutely=true 时返回，仅国内城市可用，精确到2分钟）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | 降水描述 | [optional] 
**update_time** | **str** | 更新时间 | [optional] 
**data** | [**List[GetMiscWeather200ResponseMinutelyPrecipDataInner]**](GetMiscWeather200ResponseMinutelyPrecipDataInner.md) | 精确到2分钟的数据点 | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_minutely_precip import GetMiscWeather200ResponseMinutelyPrecip

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseMinutelyPrecip from a JSON string
get_misc_weather200_response_minutely_precip_instance = GetMiscWeather200ResponseMinutelyPrecip.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseMinutelyPrecip.to_json())

# convert the object into a dict
get_misc_weather200_response_minutely_precip_dict = get_misc_weather200_response_minutely_precip_instance.to_dict()
# create an instance of GetMiscWeather200ResponseMinutelyPrecip from a dict
get_misc_weather200_response_minutely_precip_from_dict = GetMiscWeather200ResponseMinutelyPrecip.from_dict(get_misc_weather200_response_minutely_precip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


