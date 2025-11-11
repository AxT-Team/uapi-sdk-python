# PostSearchAggregate400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from uapi.models.post_search_aggregate400_response import PostSearchAggregate400Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate400Response from a JSON string
post_search_aggregate400_response_instance = PostSearchAggregate400Response.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate400Response.to_json())

# convert the object into a dict
post_search_aggregate400_response_dict = post_search_aggregate400_response_instance.to_dict()
# create an instance of PostSearchAggregate400Response from a dict
post_search_aggregate400_response_from_dict = PostSearchAggregate400Response.from_dict(post_search_aggregate400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


