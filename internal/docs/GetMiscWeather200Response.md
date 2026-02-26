# GetMiscWeather200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**province** | **str** | 省份 | [optional] 
**city** | **str** | 城市名 | [optional] 
**adcode** | **str** | 行政区划代码（部分数据源可能为空） | [optional] 
**weather** | **str** | 天气状况描述。默认返回中文，传 &#x60;lang&#x3D;en&#x60; 时返回英文。非固定枚举。 | [optional] 
**temperature** | **float** | 当前温度 °C | [optional] 
**wind_direction** | **str** | 风向 | [optional] 
**wind_power** | **str** | 风力等级 | [optional] 
**humidity** | **float** | 相对湿度 % | [optional] 
**report_time** | **str** | 数据更新时间 | [optional] 
**feels_like** | **float** | 体感温度 °C（extended&#x3D;true 时返回） | [optional] 
**visibility** | **float** | 能见度 km（extended&#x3D;true 时返回） | [optional] 
**pressure** | **float** | 气压 hPa（extended&#x3D;true 时返回） | [optional] 
**uv** | **float** | 紫外线指数（extended&#x3D;true 时返回） | [optional] 
**precipitation** | **float** | 当前降水量 mm（extended&#x3D;true 时返回） | [optional] 
**cloud** | **float** | 云量 %（extended&#x3D;true 时返回） | [optional] 
**aqi** | **float** | 空气质量指数 0-500（extended&#x3D;true 时返回） | [optional] 
**aqi_level** | **float** | AQI 等级 1-6（extended&#x3D;true 时返回） | [optional] 
**aqi_category** | **str** | AQI 等级描述（优/良/轻度污染/中度污染/重度污染/严重污染）（extended&#x3D;true 时返回） | [optional] 
**aqi_primary** | **str** | 主要污染物（如 PM2.5、PM10、O3 等）（extended&#x3D;true 时返回） | [optional] 
**air_pollutants** | [**GetMiscWeather200ResponseAirPollutants**](GetMiscWeather200ResponseAirPollutants.md) |  | [optional] 
**temp_max** | **float** | 当天最高温 °C（forecast&#x3D;true 时返回） | [optional] 
**temp_min** | **float** | 当天最低温 °C（forecast&#x3D;true 时返回） | [optional] 
**forecast** | [**List[GetMiscWeather200ResponseForecastInner]**](GetMiscWeather200ResponseForecastInner.md) | 多天天气预报，最多7天（forecast&#x3D;true 时返回） | [optional] 
**hourly_forecast** | [**List[GetMiscWeather200ResponseHourlyForecastInner]**](GetMiscWeather200ResponseHourlyForecastInner.md) | 逐小时预报，最多24小时（hourly&#x3D;true 时返回） | [optional] 
**minutely_precip** | [**GetMiscWeather200ResponseMinutelyPrecip**](GetMiscWeather200ResponseMinutelyPrecip.md) |  | [optional] 
**life_indices** | [**GetMiscWeather200ResponseLifeIndices**](GetMiscWeather200ResponseLifeIndices.md) |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response import GetMiscWeather200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200Response from a JSON string
get_misc_weather200_response_instance = GetMiscWeather200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200Response.to_json())

# convert the object into a dict
get_misc_weather200_response_dict = get_misc_weather200_response_instance.to_dict()
# create an instance of GetMiscWeather200Response from a dict
get_misc_weather200_response_from_dict = GetMiscWeather200Response.from_dict(get_misc_weather200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


