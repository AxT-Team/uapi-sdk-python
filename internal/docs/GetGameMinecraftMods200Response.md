# GetGameMinecraftMods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**query** | **str** |  | [optional] 
**results** | [**List[GetGameMinecraftMods200ResponseResultsInner]**](GetGameMinecraftMods200ResponseResultsInner.md) |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_mods200_response import GetGameMinecraftMods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftMods200Response from a JSON string
get_game_minecraft_mods200_response_instance = GetGameMinecraftMods200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftMods200Response.to_json())

# convert the object into a dict
get_game_minecraft_mods200_response_dict = get_game_minecraft_mods200_response_instance.to_dict()
# create an instance of GetGameMinecraftMods200Response from a dict
get_game_minecraft_mods200_response_from_dict = GetGameMinecraftMods200Response.from_dict(get_game_minecraft_mods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


