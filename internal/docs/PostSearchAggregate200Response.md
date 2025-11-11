# PostSearchAggregate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 实际执行的搜索查询 | [optional] 
**total_results** | **int** | 搜索结果总数 | [optional] 
**results** | [**List[PostSearchAggregate200ResponseResultsInner]**](PostSearchAggregate200ResponseResultsInner.md) | 搜索结果列表 | [optional] 
**sources** | [**List[PostSearchAggregate200ResponseSourcesInner]**](PostSearchAggregate200ResponseSourcesInner.md) | 各搜索引擎的结果数量统计 | [optional] 
**process_time_ms** | **int** | 处理耗时（毫秒） | [optional] 
**cached** | **bool** | 结果是否来自缓存 | [optional] 

## Example

```python
from uapi.models.post_search_aggregate200_response import PostSearchAggregate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate200Response from a JSON string
post_search_aggregate200_response_instance = PostSearchAggregate200Response.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate200Response.to_json())

# convert the object into a dict
post_search_aggregate200_response_dict = post_search_aggregate200_response_instance.to_dict()
# create an instance of PostSearchAggregate200Response from a dict
post_search_aggregate200_response_from_dict = PostSearchAggregate200Response.from_dict(post_search_aggregate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


