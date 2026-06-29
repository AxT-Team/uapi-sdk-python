# GetDailyWord200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**lang** | **str** |  | [optional] 
**words** | [**List[GetDailyWord200ResponseWordsInner]**](GetDailyWord200ResponseWordsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_daily_word200_response import GetDailyWord200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyWord200Response from a JSON string
get_daily_word200_response_instance = GetDailyWord200Response.from_json(json)
# print the JSON string representation of the object
print(GetDailyWord200Response.to_json())

# convert the object into a dict
get_daily_word200_response_dict = get_daily_word200_response_instance.to_dict()
# create an instance of GetDailyWord200Response from a dict
get_daily_word200_response_from_dict = GetDailyWord200Response.from_dict(get_daily_word200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


