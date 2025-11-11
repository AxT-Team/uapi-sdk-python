# GetWebparseExtractimages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**images** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_webparse_extractimages200_response import GetWebparseExtractimages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebparseExtractimages200Response from a JSON string
get_webparse_extractimages200_response_instance = GetWebparseExtractimages200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebparseExtractimages200Response.to_json())

# convert the object into a dict
get_webparse_extractimages200_response_dict = get_webparse_extractimages200_response_instance.to_dict()
# create an instance of GetWebparseExtractimages200Response from a dict
get_webparse_extractimages200_response_from_dict = GetWebparseExtractimages200Response.from_dict(get_webparse_extractimages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


