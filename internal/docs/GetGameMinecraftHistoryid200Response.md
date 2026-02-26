# GetGameMinecraftHistoryid200Response

响应结构根据查询参数不同而变化

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 【name 查询时返回】查询的用户名。 | [optional] 
**count** | **int** | 【name 查询时返回】匹配到的用户数量，为 0 时表示未找到。 | [optional] 
**results** | [**List[GetGameMinecraftHistoryid200ResponseResultsInner]**](GetGameMinecraftHistoryid200ResponseResultsInner.md) | 【name 查询时返回】匹配用户列表，包含当前用户名或曾用名匹配的所有玩家。 | [optional] 
**id** | **str** | 【uuid 查询时返回】玩家当前的用户名。 | [optional] 
**uuid** | **str** | 【uuid 查询时返回】被查询玩家的UUID（带连字符格式）。 | [optional] 
**name_num** | **int** | 【uuid 查询时返回】历史名称的总数（包含当前名称）。 | [optional] 
**history** | [**List[GetGameMinecraftHistoryid200ResponseHistoryInner]**](GetGameMinecraftHistoryid200ResponseHistoryInner.md) | 【uuid 查询时返回】包含所有历史用户名的数组，按时间倒序排列。 | [optional] 

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


