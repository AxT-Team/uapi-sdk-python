# GetGameMinecraftHistoryid200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 玩家当前的用户名。 | [optional] 
**uuid** | **str** | 玩家的UUID（带连字符格式）。 | [optional] 
**name_num** | **int** | 历史名称的总数。 | [optional] 
**history** | [**List[GetGameMinecraftHistoryid200ResponseResultsInnerHistoryInner]**](GetGameMinecraftHistoryid200ResponseResultsInnerHistoryInner.md) | 历史用户名数组。 | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_historyid200_response_results_inner import GetGameMinecraftHistoryid200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftHistoryid200ResponseResultsInner from a JSON string
get_game_minecraft_historyid200_response_results_inner_instance = GetGameMinecraftHistoryid200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftHistoryid200ResponseResultsInner.to_json())

# convert the object into a dict
get_game_minecraft_historyid200_response_results_inner_dict = get_game_minecraft_historyid200_response_results_inner_instance.to_dict()
# create an instance of GetGameMinecraftHistoryid200ResponseResultsInner from a dict
get_game_minecraft_historyid200_response_results_inner_from_dict = GetGameMinecraftHistoryid200ResponseResultsInner.from_dict(get_game_minecraft_historyid200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


