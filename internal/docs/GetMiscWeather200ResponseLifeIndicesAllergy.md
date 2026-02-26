# GetMiscWeather200ResponseLifeIndicesAllergy

过敏指数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 
**brief** | **str** |  | [optional] 
**advice** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_life_indices_allergy import GetMiscWeather200ResponseLifeIndicesAllergy

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseLifeIndicesAllergy from a JSON string
get_misc_weather200_response_life_indices_allergy_instance = GetMiscWeather200ResponseLifeIndicesAllergy.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseLifeIndicesAllergy.to_json())

# convert the object into a dict
get_misc_weather200_response_life_indices_allergy_dict = get_misc_weather200_response_life_indices_allergy_instance.to_dict()
# create an instance of GetMiscWeather200ResponseLifeIndicesAllergy from a dict
get_misc_weather200_response_life_indices_allergy_from_dict = GetMiscWeather200ResponseLifeIndicesAllergy.from_dict(get_misc_weather200_response_life_indices_allergy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


