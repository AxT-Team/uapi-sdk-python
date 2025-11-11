# GetWebTomarkdownAsyncStatus200ResponseAnyOf3


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
**error** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_web_tomarkdown_async_status200_response_any_of3 import GetWebTomarkdownAsyncStatus200ResponseAnyOf3

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf3 from a JSON string
get_web_tomarkdown_async_status200_response_any_of3_instance = GetWebTomarkdownAsyncStatus200ResponseAnyOf3.from_json(json)
# print the JSON string representation of the object
print(GetWebTomarkdownAsyncStatus200ResponseAnyOf3.to_json())

# convert the object into a dict
get_web_tomarkdown_async_status200_response_any_of3_dict = get_web_tomarkdown_async_status200_response_any_of3_instance.to_dict()
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf3 from a dict
get_web_tomarkdown_async_status200_response_any_of3_from_dict = GetWebTomarkdownAsyncStatus200ResponseAnyOf3.from_dict(get_web_tomarkdown_async_status200_response_any_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


