# GetSaying500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_saying500_response import GetSaying500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSaying500Response from a JSON string
get_saying500_response_instance = GetSaying500Response.from_json(json)
# print the JSON string representation of the object
print(GetSaying500Response.to_json())

# convert the object into a dict
get_saying500_response_dict = get_saying500_response_instance.to_dict()
# create an instance of GetSaying500Response from a dict
get_saying500_response_from_dict = GetSaying500Response.from_dict(get_saying500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


