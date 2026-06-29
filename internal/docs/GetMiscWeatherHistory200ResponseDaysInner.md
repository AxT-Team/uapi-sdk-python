# GetMiscWeatherHistory200ResponseDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**rain** | **float** |  | [optional] 
**rained** | **bool** |  | [optional] 
**temp_max** | **float** |  | [optional] 
**temp_min** | **float** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather_history200_response_days_inner import GetMiscWeatherHistory200ResponseDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeatherHistory200ResponseDaysInner from a JSON string
get_misc_weather_history200_response_days_inner_instance = GetMiscWeatherHistory200ResponseDaysInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeatherHistory200ResponseDaysInner.to_json())

# convert the object into a dict
get_misc_weather_history200_response_days_inner_dict = get_misc_weather_history200_response_days_inner_instance.to_dict()
# create an instance of GetMiscWeatherHistory200ResponseDaysInner from a dict
get_misc_weather_history200_response_days_inner_from_dict = GetMiscWeatherHistory200ResponseDaysInner.from_dict(get_misc_weather_history200_response_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


