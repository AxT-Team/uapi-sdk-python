# GetGameMinecraftHistoryid200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表成功。 | [optional] 
**history** | [**List[GetGameMinecraftHistoryid200ResponseHistoryInner]**](GetGameMinecraftHistoryid200ResponseHistoryInner.md) | 一个包含所有历史用户名的数组，按时间倒序排列。 | [optional] 
**id** | **str** | 玩家当前的用户名。 | [optional] 
**name_num** | **int** | 历史名称的总数（包含当前名称）。 | [optional] 
**uuid** | **str** | 被查询玩家的32位无破折号UUID。 | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_historyid200_response import GetGameMinecraftHistoryid200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftHistoryid200Response from a JSON string
get_game_minecraft_historyid200_response_instance = GetGameMinecraftHistoryid200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftHistoryid200Response.to_json())

# convert the object into a dict
get_game_minecraft_historyid200_response_dict = get_game_minecraft_historyid200_response_instance.to_dict()
# create an instance of GetGameMinecraftHistoryid200Response from a dict
get_game_minecraft_historyid200_response_from_dict = GetGameMinecraftHistoryid200Response.from_dict(get_game_minecraft_historyid200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


