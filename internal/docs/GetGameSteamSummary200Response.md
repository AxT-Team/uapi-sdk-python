# GetGameSteamSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** | 32x32 像素的小尺寸头像URL。 | [optional] 
**avatarfull** | **str** | 184x184 像素的大尺寸头像URL。 | [optional] 
**avatarmedium** | **str** | 64x64 像素的中等尺寸头像URL。 | [optional] 
**code** | **int** | 状态码，200代表成功。 | [optional] 
**communityvisibilitystate** | **int** | 社区资料的可见性状态: 1&#x3D;私密, 3&#x3D;公开。 | [optional] 
**loccountrycode** | **str** | 用户个人资料中设置的国家代码 (ISO 3166-1)，前提是用户已设置并公开。 | [optional] 
**personaname** | **str** | 玩家的当前昵称。 | [optional] 
**personastate** | **int** | 用户当前的在线状态: 0-离线, 1-在线, 2-忙碌, 3-离开, 4-打盹, 5-想交易, 6-想玩。 | [optional] 
**primaryclanid** | **str** | 玩家设置的主要部落的64位ID。 | [optional] 
**profilestate** | **int** | 如果用户设置了个人资料，则为1。 | [optional] 
**profileurl** | **str** | 用户的Steam社区个人资料页完整URL。 | [optional] 
**realname** | **str** | 用户的真实姓名，前提是用户已设置并公开。 | [optional] 
**steamid** | **str** | 被查询用户的64位SteamID。 | [optional] 
**timecreated** | **int** | 账户创建时的Unix时间戳（秒）。 | [optional] 
**timecreated_str** | **str** | 我们为你格式化好的账户创建时间，更直观。 | [optional] 

## Example

```python
from uapi.models.get_game_steam_summary200_response import GetGameSteamSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSteamSummary200Response from a JSON string
get_game_steam_summary200_response_instance = GetGameSteamSummary200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameSteamSummary200Response.to_json())

# convert the object into a dict
get_game_steam_summary200_response_dict = get_game_steam_summary200_response_instance.to_dict()
# create an instance of GetGameSteamSummary200Response from a dict
get_game_steam_summary200_response_from_dict = GetGameSteamSummary200Response.from_dict(get_game_steam_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


