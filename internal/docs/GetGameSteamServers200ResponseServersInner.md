# GetGameSteamServers200ResponseServersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**map** | **str** |  | [optional] 
**max_players** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**online** | **bool** |  | [optional] 
**players** | **int** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from uapi.models.get_game_steam_servers200_response_servers_inner import GetGameSteamServers200ResponseServersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSteamServers200ResponseServersInner from a JSON string
get_game_steam_servers200_response_servers_inner_instance = GetGameSteamServers200ResponseServersInner.from_json(json)
# print the JSON string representation of the object
print(GetGameSteamServers200ResponseServersInner.to_json())

# convert the object into a dict
get_game_steam_servers200_response_servers_inner_dict = get_game_steam_servers200_response_servers_inner_instance.to_dict()
# create an instance of GetGameSteamServers200ResponseServersInner from a dict
get_game_steam_servers200_response_servers_inner_from_dict = GetGameSteamServers200ResponseServersInner.from_dict(get_game_steam_servers200_response_servers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


