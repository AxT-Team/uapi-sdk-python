# GetGameMinecraftMods200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**downloads** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_mods200_response_results_inner import GetGameMinecraftMods200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftMods200ResponseResultsInner from a JSON string
get_game_minecraft_mods200_response_results_inner_instance = GetGameMinecraftMods200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftMods200ResponseResultsInner.to_json())

# convert the object into a dict
get_game_minecraft_mods200_response_results_inner_dict = get_game_minecraft_mods200_response_results_inner_instance.to_dict()
# create an instance of GetGameMinecraftMods200ResponseResultsInner from a dict
get_game_minecraft_mods200_response_results_inner_from_dict = GetGameMinecraftMods200ResponseResultsInner.from_dict(get_game_minecraft_mods200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


