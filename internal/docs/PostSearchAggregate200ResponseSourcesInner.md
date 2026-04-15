# PostSearchAggregate200ResponseSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 搜索引擎版本 | [optional] 
**status** | **str** | 本次搜索引擎调用状态 | [optional] 
**result_count** | **int** | 该搜索引擎返回的结果数 | [optional] 
**elapsed_ms** | **int** | 该搜索引擎的耗时（毫秒） | [optional] 
**first_result_host** | **str** | 该搜索源首条结果的域名 | [optional] 

## Example

```python
from uapi.models.post_search_aggregate200_response_sources_inner import PostSearchAggregate200ResponseSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate200ResponseSourcesInner from a JSON string
post_search_aggregate200_response_sources_inner_instance = PostSearchAggregate200ResponseSourcesInner.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate200ResponseSourcesInner.to_json())

# convert the object into a dict
post_search_aggregate200_response_sources_inner_dict = post_search_aggregate200_response_sources_inner_instance.to_dict()
# create an instance of PostSearchAggregate200ResponseSourcesInner from a dict
post_search_aggregate200_response_sources_inner_from_dict = PostSearchAggregate200ResponseSourcesInner.from_dict(post_search_aggregate200_response_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


