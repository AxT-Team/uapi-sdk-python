# GetMiscWeatherHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adcode** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**days** | [**List[GetMiscWeatherHistory200ResponseDaysInner]**](GetMiscWeatherHistory200ResponseDaysInner.md) |  | [optional] 
**end_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather_history200_response import GetMiscWeatherHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeatherHistory200Response from a JSON string
get_misc_weather_history200_response_instance = GetMiscWeatherHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeatherHistory200Response.to_json())

# convert the object into a dict
get_misc_weather_history200_response_dict = get_misc_weather_history200_response_instance.to_dict()
# create an instance of GetMiscWeatherHistory200Response from a dict
get_misc_weather_history200_response_from_dict = GetMiscWeatherHistory200Response.from_dict(get_misc_weather_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


