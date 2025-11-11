# GetRandomString500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_random_string500_response import GetRandomString500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRandomString500Response from a JSON string
get_random_string500_response_instance = GetRandomString500Response.from_json(json)
# print the JSON string representation of the object
print(GetRandomString500Response.to_json())

# convert the object into a dict
get_random_string500_response_dict = get_random_string500_response_instance.to_dict()
# create an instance of GetRandomString500Response from a dict
get_random_string500_response_from_dict = GetRandomString500Response.from_dict(get_random_string500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


