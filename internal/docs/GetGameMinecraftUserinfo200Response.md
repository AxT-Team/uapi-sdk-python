# GetGameMinecraftUserinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表成功。 | [optional] 
**skin_url** | **str** | 玩家当前使用的皮肤图片URL。 | [optional] 
**username** | **str** | 玩家当前的准确用户名（注意大小写可能与输入不同）。 | [optional] 
**uuid** | **str** | 玩家的32位无破折号UUID。 | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_userinfo200_response import GetGameMinecraftUserinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftUserinfo200Response from a JSON string
get_game_minecraft_userinfo200_response_instance = GetGameMinecraftUserinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftUserinfo200Response.to_json())

# convert the object into a dict
get_game_minecraft_userinfo200_response_dict = get_game_minecraft_userinfo200_response_instance.to_dict()
# create an instance of GetGameMinecraftUserinfo200Response from a dict
get_game_minecraft_userinfo200_response_from_dict = GetGameMinecraftUserinfo200Response.from_dict(get_game_minecraft_userinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


