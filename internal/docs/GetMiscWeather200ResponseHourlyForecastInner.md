# GetMiscWeather200ResponseHourlyForecastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | 预报时间（ISO8601 或 YYYY-MM-DD HH:MM） | [optional] 
**temperature** | **float** | 温度 °C | [optional] 
**weather** | **str** | 天气状况 | [optional] 
**wind_direction** | **str** | 风向（可选） | [optional] 
**wind_speed** | **float** | 风速 km/h（可选） | [optional] 
**wind_scale** | **str** | 风力等级（可选） | [optional] 
**humidity** | **float** | 湿度 %（可选） | [optional] 
**precip** | **float** | 降水量 mm（可选） | [optional] 
**pressure** | **float** | 气压 hPa（可选） | [optional] 
**cloud** | **float** | 云量 %（可选） | [optional] 
**feels_like** | **float** | 体感温度 °C（可选） | [optional] 
**dew_point** | **float** | 露点温度 °C（可选） | [optional] 
**visibility** | **float** | 能见度 km（可选） | [optional] 
**pop** | **float** | 降水概率 %（可选） | [optional] 
**uv_index** | **float** | 紫外线指数（可选） | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_hourly_forecast_inner import GetMiscWeather200ResponseHourlyForecastInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseHourlyForecastInner from a JSON string
get_misc_weather200_response_hourly_forecast_inner_instance = GetMiscWeather200ResponseHourlyForecastInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseHourlyForecastInner.to_json())

# convert the object into a dict
get_misc_weather200_response_hourly_forecast_inner_dict = get_misc_weather200_response_hourly_forecast_inner_instance.to_dict()
# create an instance of GetMiscWeather200ResponseHourlyForecastInner from a dict
get_misc_weather200_response_hourly_forecast_inner_from_dict = GetMiscWeather200ResponseHourlyForecastInner.from_dict(get_misc_weather200_response_hourly_forecast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


