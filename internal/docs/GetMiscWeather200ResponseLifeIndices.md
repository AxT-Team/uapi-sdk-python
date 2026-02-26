# GetMiscWeather200ResponseLifeIndices

18项生活指数（indices=true 时返回），每项包含 level（等级名称）、brief（简短描述）、advice（详细建议）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clothing** | [**GetMiscWeather200ResponseLifeIndicesClothing**](GetMiscWeather200ResponseLifeIndicesClothing.md) |  | [optional] 
**uv** | [**GetMiscWeather200ResponseLifeIndicesUv**](GetMiscWeather200ResponseLifeIndicesUv.md) |  | [optional] 
**car_wash** | [**GetMiscWeather200ResponseLifeIndicesCarWash**](GetMiscWeather200ResponseLifeIndicesCarWash.md) |  | [optional] 
**drying** | [**GetMiscWeather200ResponseLifeIndicesDrying**](GetMiscWeather200ResponseLifeIndicesDrying.md) |  | [optional] 
**air_conditioner** | [**GetMiscWeather200ResponseLifeIndicesAirConditioner**](GetMiscWeather200ResponseLifeIndicesAirConditioner.md) |  | [optional] 
**cold_risk** | [**GetMiscWeather200ResponseLifeIndicesColdRisk**](GetMiscWeather200ResponseLifeIndicesColdRisk.md) |  | [optional] 
**exercise** | [**GetMiscWeather200ResponseLifeIndicesExercise**](GetMiscWeather200ResponseLifeIndicesExercise.md) |  | [optional] 
**comfort** | [**GetMiscWeather200ResponseLifeIndicesComfort**](GetMiscWeather200ResponseLifeIndicesComfort.md) |  | [optional] 
**travel** | [**GetMiscWeather200ResponseLifeIndicesTravel**](GetMiscWeather200ResponseLifeIndicesTravel.md) |  | [optional] 
**fishing** | [**GetMiscWeather200ResponseLifeIndicesFishing**](GetMiscWeather200ResponseLifeIndicesFishing.md) |  | [optional] 
**allergy** | [**GetMiscWeather200ResponseLifeIndicesAllergy**](GetMiscWeather200ResponseLifeIndicesAllergy.md) |  | [optional] 
**sunscreen** | [**GetMiscWeather200ResponseLifeIndicesSunscreen**](GetMiscWeather200ResponseLifeIndicesSunscreen.md) |  | [optional] 
**mood** | [**GetMiscWeather200ResponseLifeIndicesMood**](GetMiscWeather200ResponseLifeIndicesMood.md) |  | [optional] 
**beer** | [**GetMiscWeather200ResponseLifeIndicesBeer**](GetMiscWeather200ResponseLifeIndicesBeer.md) |  | [optional] 
**umbrella** | [**GetMiscWeather200ResponseLifeIndicesUmbrella**](GetMiscWeather200ResponseLifeIndicesUmbrella.md) |  | [optional] 
**traffic** | [**GetMiscWeather200ResponseLifeIndicesTraffic**](GetMiscWeather200ResponseLifeIndicesTraffic.md) |  | [optional] 
**air_purifier** | [**GetMiscWeather200ResponseLifeIndicesAirPurifier**](GetMiscWeather200ResponseLifeIndicesAirPurifier.md) |  | [optional] 
**pollen** | [**GetMiscWeather200ResponseLifeIndicesPollen**](GetMiscWeather200ResponseLifeIndicesPollen.md) |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather200_response_life_indices import GetMiscWeather200ResponseLifeIndices

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather200ResponseLifeIndices from a JSON string
get_misc_weather200_response_life_indices_instance = GetMiscWeather200ResponseLifeIndices.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather200ResponseLifeIndices.to_json())

# convert the object into a dict
get_misc_weather200_response_life_indices_dict = get_misc_weather200_response_life_indices_instance.to_dict()
# create an instance of GetMiscWeather200ResponseLifeIndices from a dict
get_misc_weather200_response_life_indices_from_dict = GetMiscWeather200ResponseLifeIndices.from_dict(get_misc_weather200_response_life_indices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


