# PostSearchAggregate401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from uapi.models.post_search_aggregate401_response import PostSearchAggregate401Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate401Response from a JSON string
post_search_aggregate401_response_instance = PostSearchAggregate401Response.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate401Response.to_json())

# convert the object into a dict
post_search_aggregate401_response_dict = post_search_aggregate401_response_instance.to_dict()
# create an instance of PostSearchAggregate401Response from a dict
post_search_aggregate401_response_from_dict = PostSearchAggregate401Response.from_dict(post_search_aggregate401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


