# GetGameMinecraftHistoryid200ResponseHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_to_at** | **str** | 更名为此名称的时间，格式为 &#x60;YYYY/MM/DD HH:mm:ss&#x60;。如果是初始名称，则为 &#x60;Initial&#x60;。 | [optional] 
**name** | **str** | 当时使用的用户名。 | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_historyid200_response_history_inner import GetGameMinecraftHistoryid200ResponseHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftHistoryid200ResponseHistoryInner from a JSON string
get_game_minecraft_historyid200_response_history_inner_instance = GetGameMinecraftHistoryid200ResponseHistoryInner.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftHistoryid200ResponseHistoryInner.to_json())

# convert the object into a dict
get_game_minecraft_historyid200_response_history_inner_dict = get_game_minecraft_historyid200_response_history_inner_instance.to_dict()
# create an instance of GetGameMinecraftHistoryid200ResponseHistoryInner from a dict
get_game_minecraft_historyid200_response_history_inner_from_dict = GetGameMinecraftHistoryid200ResponseHistoryInner.from_dict(get_game_minecraft_historyid200_response_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


