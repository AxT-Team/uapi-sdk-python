# GetGameMinecraftUserinfo400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_userinfo400_response import GetGameMinecraftUserinfo400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftUserinfo400Response from a JSON string
get_game_minecraft_userinfo400_response_instance = GetGameMinecraftUserinfo400Response.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftUserinfo400Response.to_json())

# convert the object into a dict
get_game_minecraft_userinfo400_response_dict = get_game_minecraft_userinfo400_response_instance.to_dict()
# create an instance of GetGameMinecraftUserinfo400Response from a dict
get_game_minecraft_userinfo400_response_from_dict = GetGameMinecraftUserinfo400Response.from_dict(get_game_minecraft_userinfo400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


