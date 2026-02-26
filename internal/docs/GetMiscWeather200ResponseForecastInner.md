# GetMiscWeather200ResponseForecastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 日期 YYYY-MM-DD | [optional] 
**week** | **str** | 星期几（&#x60;lang&#x3D;en&#x60; 时返回英文星期） | [optional] 
**temp_max** | **float** | 最高温度 °C | [optional] 
**temp_min** | **float** | 最低温度 °C | [optional] 
**weather_day** | **str** | 白天天气（&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**weather_night** | **str** | 夜间天气（&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**wind_dir_day** | **str** | 白天风向（可选，&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**wind_dir_night** | **str** | 夜间风向（可选，&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**wind_scale_day** | **str** | 白天风力（可选，&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**wind_scale_night** | **str** | 夜间风力（可选，&#x60;lang&#x3D;en&#x60; 时返回英文） | [optional] 
**wind_speed_day** | **float** | 白天风速 km/h（可选） | [optional] 
**humidity** | **float** | 湿度 %（可选） | [optional] 
**precip** | **float** | 降水量 mm（可选） | [optional] 
**visibility** | **float** | 能见度 km（可选） | [optional] 
**uv_index** | **float** | 紫外线指数（可选） | [optional] 
**sunrise** | **str** | 日出时间 HH:MM（可选） | [optional] 
**sunset** | **str** | 日落时间 HH:MM（可选） | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_forecast_inner import GetMiscWeather200ResponseForecastInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseForecastInner from a JSON string
get_misc_weather200_response_forecast_inner_instance = GetMiscWeather200ResponseForecastInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseForecastInner.to_json())

# convert the object into a dict
get_misc_weather200_response_forecast_inner_dict = get_misc_weather200_response_forecast_inner_instance.to_dict()
# create an instance of GetMiscWeather200ResponseForecastInner from a dict
get_misc_weather200_response_forecast_inner_from_dict = GetMiscWeather200ResponseForecastInner.from_dict(get_misc_weather200_response_forecast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


