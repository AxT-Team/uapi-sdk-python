# GetMiscWeather200ResponseLifeIndicesComfort

舒适度指数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 
**brief** | **str** |  | [optional] 
**advice** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_life_indices_comfort import GetMiscWeather200ResponseLifeIndicesComfort

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseLifeIndicesComfort from a JSON string
get_misc_weather200_response_life_indices_comfort_instance = GetMiscWeather200ResponseLifeIndicesComfort.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseLifeIndicesComfort.to_json())

# convert the object into a dict
get_misc_weather200_response_life_indices_comfort_dict = get_misc_weather200_response_life_indices_comfort_instance.to_dict()
# create an instance of GetMiscWeather200ResponseLifeIndicesComfort from a dict
get_misc_weather200_response_life_indices_comfort_from_dict = GetMiscWeather200ResponseLifeIndicesComfort.from_dict(get_misc_weather200_response_life_indices_comfort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


