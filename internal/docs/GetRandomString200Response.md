# GetRandomString200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_random_string200_response import GetRandomString200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRandomString200Response from a JSON string
get_random_string200_response_instance = GetRandomString200Response.from_json(json)
# print the JSON string representation of the object
print(GetRandomString200Response.to_json())

# convert the object into a dict
get_random_string200_response_dict = get_random_string200_response_instance.to_dict()
# create an instance of GetRandomString200Response from a dict
get_random_string200_response_from_dict = GetRandomString200Response.from_dict(get_random_string200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


