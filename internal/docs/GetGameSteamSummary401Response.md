# GetGameSteamSummary401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_game_steam_summary401_response import GetGameSteamSummary401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSteamSummary401Response from a JSON string
get_game_steam_summary401_response_instance = GetGameSteamSummary401Response.from_json(json)
# print the JSON string representation of the object
print(GetGameSteamSummary401Response.to_json())

# convert the object into a dict
get_game_steam_summary401_response_dict = get_game_steam_summary401_response_instance.to_dict()
# create an instance of GetGameSteamSummary401Response from a dict
get_game_steam_summary401_response_from_dict = GetGameSteamSummary401Response.from_dict(get_game_steam_summary401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


