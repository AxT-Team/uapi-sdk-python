# PostSearchAggregateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 搜索查询关键词，支持中英文 | 
**site** | **str** | 限制搜索特定网站，不需要 &#x60;site:&#x60; 前缀 | [optional] 
**filetype** | **str** | 限制文件类型，不需要 &#x60;filetype:&#x60; 前缀。支持 pdf、doc、docx、ppt、pptx、xls、xlsx、txt 等 | [optional] 
**fetch_full** | **bool** | 是否获取页面完整正文（会影响响应时间） | [optional] [default to False]
**timeout_ms** | **int** | 请求超时时间（毫秒），范围 1000-30000 | [optional] [default to 3000]

## Example

```python
from uapi.models.post_search_aggregate_request import PostSearchAggregateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregateRequest from a JSON string
post_search_aggregate_request_instance = PostSearchAggregateRequest.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregateRequest.to_json())

# convert the object into a dict
post_search_aggregate_request_dict = post_search_aggregate_request_instance.to_dict()
# create an instance of PostSearchAggregateRequest from a dict
post_search_aggregate_request_from_dict = PostSearchAggregateRequest.from_dict(post_search_aggregate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


