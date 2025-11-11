# GetWebparseMetadata200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**favicon_url** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**published_time** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**generator** | **str** |  | [optional] 
**open_graph** | **object** |  | [optional] 

## Example

```python
from uapi.models.get_webparse_metadata200_response import GetWebparseMetadata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebparseMetadata200Response from a JSON string
get_webparse_metadata200_response_instance = GetWebparseMetadata200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebparseMetadata200Response.to_json())

# convert the object into a dict
get_webparse_metadata200_response_dict = get_webparse_metadata200_response_instance.to_dict()
# create an instance of GetWebparseMetadata200Response from a dict
get_webparse_metadata200_response_from_dict = GetWebparseMetadata200Response.from_dict(get_webparse_metadata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


