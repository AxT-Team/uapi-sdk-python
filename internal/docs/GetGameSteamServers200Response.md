# GetGameSteamServers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**query** | **str** |  | [optional] 
**servers** | [**List[GetGameSteamServers200ResponseServersInner]**](GetGameSteamServers200ResponseServersInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_game_steam_servers200_response import GetGameSteamServers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSteamServers200Response from a JSON string
get_game_steam_servers200_response_instance = GetGameSteamServers200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameSteamServers200Response.to_json())

# convert the object into a dict
get_game_steam_servers200_response_dict = get_game_steam_servers200_response_instance.to_dict()
# create an instance of GetGameSteamServers200Response from a dict
get_game_steam_servers200_response_from_dict = GetGameSteamServers200Response.from_dict(get_game_steam_servers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


