# GetGameMinecraftServerstatus200ResponseOnlinePlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 玩家名称。 | [optional] 
**uuid** | **str** | 玩家的 UUID。部分服务器可能不返回这个字段。 | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_serverstatus200_response_online_players_inner import GetGameMinecraftServerstatus200ResponseOnlinePlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftServerstatus200ResponseOnlinePlayersInner from a JSON string
get_game_minecraft_serverstatus200_response_online_players_inner_instance = GetGameMinecraftServerstatus200ResponseOnlinePlayersInner.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftServerstatus200ResponseOnlinePlayersInner.to_json())

# convert the object into a dict
get_game_minecraft_serverstatus200_response_online_players_inner_dict = get_game_minecraft_serverstatus200_response_online_players_inner_instance.to_dict()
# create an instance of GetGameMinecraftServerstatus200ResponseOnlinePlayersInner from a dict
get_game_minecraft_serverstatus200_response_online_players_inner_from_dict = GetGameMinecraftServerstatus200ResponseOnlinePlayersInner.from_dict(get_game_minecraft_serverstatus200_response_online_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


