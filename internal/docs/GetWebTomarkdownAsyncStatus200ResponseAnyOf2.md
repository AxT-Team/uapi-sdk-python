# GetWebTomarkdownAsyncStatus200ResponseAnyOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**result** | [**GetWebTomarkdownAsyncStatus200ResponseAnyOf2Result**](GetWebTomarkdownAsyncStatus200ResponseAnyOf2Result.md) |  | [optional] 

## Example

```python
from uapi.models.get_web_tomarkdown_async_status200_response_any_of2 import GetWebTomarkdownAsyncStatus200ResponseAnyOf2

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf2 from a JSON string
get_web_tomarkdown_async_status200_response_any_of2_instance = GetWebTomarkdownAsyncStatus200ResponseAnyOf2.from_json(json)
# print the JSON string representation of the object
print(GetWebTomarkdownAsyncStatus200ResponseAnyOf2.to_json())

# convert the object into a dict
get_web_tomarkdown_async_status200_response_any_of2_dict = get_web_tomarkdown_async_status200_response_any_of2_instance.to_dict()
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf2 from a dict
get_web_tomarkdown_async_status200_response_any_of2_from_dict = GetWebTomarkdownAsyncStatus200ResponseAnyOf2.from_dict(get_web_tomarkdown_async_status200_response_any_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


