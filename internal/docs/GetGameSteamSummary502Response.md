# GetGameSteamSummary502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_game_steam_summary502_response import GetGameSteamSummary502Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSteamSummary502Response from a JSON string
get_game_steam_summary502_response_instance = GetGameSteamSummary502Response.from_json(json)
# print the JSON string representation of the object
print(GetGameSteamSummary502Response.to_json())

# convert the object into a dict
get_game_steam_summary502_response_dict = get_game_steam_summary502_response_instance.to_dict()
# create an instance of GetGameSteamSummary502Response from a dict
get_game_steam_summary502_response_from_dict = GetGameSteamSummary502Response.from_dict(get_game_steam_summary502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


