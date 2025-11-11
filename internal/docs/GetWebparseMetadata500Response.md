# GetWebparseMetadata500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_webparse_metadata500_response import GetWebparseMetadata500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebparseMetadata500Response from a JSON string
get_webparse_metadata500_response_instance = GetWebparseMetadata500Response.from_json(json)
# print the JSON string representation of the object
print(GetWebparseMetadata500Response.to_json())

# convert the object into a dict
get_webparse_metadata500_response_dict = get_webparse_metadata500_response_instance.to_dict()
# create an instance of GetWebparseMetadata500Response from a dict
get_webparse_metadata500_response_from_dict = GetWebparseMetadata500Response.from_dict(get_webparse_metadata500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


