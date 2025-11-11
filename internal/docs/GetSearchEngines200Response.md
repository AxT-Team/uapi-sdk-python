# GetSearchEngines200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | [**GetSearchEngines200ResponseEngine**](GetSearchEngines200ResponseEngine.md) |  | [optional] 
**limits** | [**GetSearchEngines200ResponseLimits**](GetSearchEngines200ResponseLimits.md) |  | [optional] 
**supported_parameters** | **List[str]** | 支持的所有参数说明列表 | [optional] 

## Example

```python
from uapi.models.get_search_engines200_response import GetSearchEngines200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchEngines200Response from a JSON string
get_search_engines200_response_instance = GetSearchEngines200Response.from_json(json)
# print the JSON string representation of the object
print(GetSearchEngines200Response.to_json())

# convert the object into a dict
get_search_engines200_response_dict = get_search_engines200_response_instance.to_dict()
# create an instance of GetSearchEngines200Response from a dict
get_search_engines200_response_from_dict = GetSearchEngines200Response.from_dict(get_search_engines200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


