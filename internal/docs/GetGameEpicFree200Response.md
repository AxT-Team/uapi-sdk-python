# GetGameEpicFree200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表成功。 | [optional] 
**data** | [**List[GetGameEpicFree200ResponseDataInner]**](GetGameEpicFree200ResponseDataInner.md) | 免费游戏列表数组。 | [optional] 

## Example

```python
from uapi.models.get_game_epic_free200_response import GetGameEpicFree200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameEpicFree200Response from a JSON string
get_game_epic_free200_response_instance = GetGameEpicFree200Response.from_json(json)
# print the JSON string representation of the object
print(GetGameEpicFree200Response.to_json())

# convert the object into a dict
get_game_epic_free200_response_dict = get_game_epic_free200_response_instance.to_dict()
# create an instance of GetGameEpicFree200Response from a dict
get_game_epic_free200_response_from_dict = GetGameEpicFree200Response.from_dict(get_game_epic_free200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


