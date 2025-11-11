# GetWebTomarkdownAsyncStatus200ResponseAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_web_tomarkdown_async_status200_response_any_of import GetWebTomarkdownAsyncStatus200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf from a JSON string
get_web_tomarkdown_async_status200_response_any_of_instance = GetWebTomarkdownAsyncStatus200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print(GetWebTomarkdownAsyncStatus200ResponseAnyOf.to_json())

# convert the object into a dict
get_web_tomarkdown_async_status200_response_any_of_dict = get_web_tomarkdown_async_status200_response_any_of_instance.to_dict()
# create an instance of GetWebTomarkdownAsyncStatus200ResponseAnyOf from a dict
get_web_tomarkdown_async_status200_response_any_of_from_dict = GetWebTomarkdownAsyncStatus200ResponseAnyOf.from_dict(get_web_tomarkdown_async_status200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


