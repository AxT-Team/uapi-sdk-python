# GetWebTomarkdownAsyncStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**elapsed** | **float** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**result** | [**GetWebTomarkdownAsyncStatus200ResponseAnyOf2Result**](GetWebTomarkdownAsyncStatus200ResponseAnyOf2Result.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_web_tomarkdown_async_status200_response import GetWebTomarkdownAsyncStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebTomarkdownAsyncStatus200Response from a JSON string
get_web_tomarkdown_async_status200_response_instance = GetWebTomarkdownAsyncStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebTomarkdownAsyncStatus200Response.to_json())

# convert the object into a dict
get_web_tomarkdown_async_status200_response_dict = get_web_tomarkdown_async_status200_response_instance.to_dict()
# create an instance of GetWebTomarkdownAsyncStatus200Response from a dict
get_web_tomarkdown_async_status200_response_from_dict = GetWebTomarkdownAsyncStatus200Response.from_dict(get_web_tomarkdown_async_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


