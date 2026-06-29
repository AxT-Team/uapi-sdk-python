# GetMiscWeather200ResponseAlertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guidance** | **List[str]** | 防御指引列表 | [optional] 
**level** | **str** | 预警级别，如蓝色、黄色、橙色、红色 | [optional] 
**publish_time** | **str** | 预警发布时间 | [optional] 
**publisher** | **str** | 发布单位 | [optional] 
**text** | **str** | 预警正文 | [optional] 
**title** | **str** | 预警标题 | [optional] 
**type** | **str** | 预警类型，如雷电、暴雨 | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_alerts_inner import GetMiscWeather200ResponseAlertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseAlertsInner from a JSON string
get_misc_weather200_response_alerts_inner_instance = GetMiscWeather200ResponseAlertsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseAlertsInner.to_json())

# convert the object into a dict
get_misc_weather200_response_alerts_inner_dict = get_misc_weather200_response_alerts_inner_instance.to_dict()
# create an instance of GetMiscWeather200ResponseAlertsInner from a dict
get_misc_weather200_response_alerts_inner_from_dict = GetMiscWeather200ResponseAlertsInner.from_dict(get_misc_weather200_response_alerts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


