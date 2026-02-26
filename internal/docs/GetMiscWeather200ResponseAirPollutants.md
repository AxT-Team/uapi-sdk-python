# GetMiscWeather200ResponseAirPollutants

空气污染物分项数据（extended=true 时返回，部分数据源可能不返回）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pm25** | **float** | PM2.5 μg/m³ | [optional] 
**pm10** | **float** | PM10 μg/m³ | [optional] 
**o3** | **float** | 臭氧 μg/m³ | [optional] 
**no2** | **float** | 二氧化氮 μg/m³ | [optional] 
**so2** | **float** | 二氧化硫 μg/m³ | [optional] 
**co** | **float** | 一氧化碳 mg/m³ | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_air_pollutants import GetMiscWeather200ResponseAirPollutants

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseAirPollutants from a JSON string
get_misc_weather200_response_air_pollutants_instance = GetMiscWeather200ResponseAirPollutants.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseAirPollutants.to_json())

# convert the object into a dict
get_misc_weather200_response_air_pollutants_dict = get_misc_weather200_response_air_pollutants_instance.to_dict()
# create an instance of GetMiscWeather200ResponseAirPollutants from a dict
get_misc_weather200_response_air_pollutants_from_dict = GetMiscWeather200ResponseAirPollutants.from_dict(get_misc_weather200_response_air_pollutants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


