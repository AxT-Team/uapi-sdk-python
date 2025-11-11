# PostWebTomarkdownAsync400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **int** |  | [optional] 

## Example

```python
from uapi.models.post_web_tomarkdown_async400_response import PostWebTomarkdownAsync400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebTomarkdownAsync400Response from a JSON string
post_web_tomarkdown_async400_response_instance = PostWebTomarkdownAsync400Response.from_json(json)
# print the JSON string representation of the object
print(PostWebTomarkdownAsync400Response.to_json())

# convert the object into a dict
post_web_tomarkdown_async400_response_dict = post_web_tomarkdown_async400_response_instance.to_dict()
# create an instance of PostWebTomarkdownAsync400Response from a dict
post_web_tomarkdown_async400_response_from_dict = PostWebTomarkdownAsync400Response.from_dict(post_web_tomarkdown_async400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


