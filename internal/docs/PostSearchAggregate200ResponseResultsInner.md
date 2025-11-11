# PostSearchAggregate200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | 结果标题 | [optional] 
**url** | **str** | 结果链接 | [optional] 
**snippet** | **str** | 结果摘要/描述 | [optional] 
**domain** | **str** | 来源域名 | [optional] 
**source** | **str** | 搜索引擎标识 | [optional] 
**position** | **int** | 原始排名位置 | [optional] 
**score** | **float** | 综合得分 (0-1，经过机器学习排序) | [optional] 
**publish_time** | **datetime** | 发布时间 (ISO 8601 格式) | [optional] 
**author** | **str** | 作者信息 | [optional] 

## Example

```python
from uapi.models.post_search_aggregate200_response_results_inner import PostSearchAggregate200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate200ResponseResultsInner from a JSON string
post_search_aggregate200_response_results_inner_instance = PostSearchAggregate200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate200ResponseResultsInner.to_json())

# convert the object into a dict
post_search_aggregate200_response_results_inner_dict = post_search_aggregate200_response_results_inner_instance.to_dict()
# create an instance of PostSearchAggregate200ResponseResultsInner from a dict
post_search_aggregate200_response_results_inner_from_dict = PostSearchAggregate200ResponseResultsInner.from_dict(post_search_aggregate200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


