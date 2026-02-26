# GetMiscWeather503Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_weather503_response import GetMiscWeather503Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscWeather503Response from a JSON string
get_misc_weather503_response_instance = GetMiscWeather503Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscWeather503Response.to_json())

# convert the object into a dict
get_misc_weather503_response_dict = get_misc_weather503_response_instance.to_dict()
# create an instance of GetMiscWeather503Response from a dict
get_misc_weather503_response_from_dict = GetMiscWeather503Response.from_dict(get_misc_weather503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


