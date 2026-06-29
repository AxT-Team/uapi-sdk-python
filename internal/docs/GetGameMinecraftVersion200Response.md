# GetGameMinecraftVersion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest** | [**GetGameMinecraftVersion200ResponseLatest**](GetGameMinecraftVersion200ResponseLatest.md) |  | [optional] 
**versions** | [**List[GetGameMinecraftVersion200ResponseVersionsInner]**](GetGameMinecraftVersion200ResponseVersionsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_game_minecraft_version200_response import GetGameMinecraftVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameMinecraftVersion200Response from a JSON string
get_game_minecraft_version200_response_instance = GetGameMinecraftVersion200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameMinecraftVersion200Response.to_json())

# convert the object into a dict
get_game_minecraft_version200_response_dict = get_game_minecraft_version200_response_instance.to_dict()
# create an instance of GetGameMinecraftVersion200Response from a dict
get_game_minecraft_version200_response_from_dict = GetGameMinecraftVersion200Response.from_dict(get_game_minecraft_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


