# GetMiscWeather200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adcode** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**humidity** | **int** |  | [optional] 
**province** | **str** |  | [optional] 
**report_time** | **str** |  | [optional] 
**temperature** | **int** |  | [optional] 
**weather** | **str** |  | [optional] 
**wind_direction** | **str** |  | [optional] 
**wind_power** | **str** |  | [optional] 

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


