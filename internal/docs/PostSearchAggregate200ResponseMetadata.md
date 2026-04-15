# PostSearchAggregate200ResponseMetadata

本次请求的处理元数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_params** | [**PostSearchAggregate200ResponseMetadataRequestParams**](PostSearchAggregate200ResponseMetadataRequestParams.md) |  | [optional] 
**dedupe_removed** | **int** | 去重后移除的结果数 | [optional] 
**rerank_applied** | **bool** | 是否执行了排序重排 | [optional] 
**content_fetched** | **int** | 额外抓取正文的结果数 | [optional] 

## Example

```python
from uapi.models.post_search_aggregate200_response_metadata import PostSearchAggregate200ResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate200ResponseMetadata from a JSON string
post_search_aggregate200_response_metadata_instance = PostSearchAggregate200ResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate200ResponseMetadata.to_json())

# convert the object into a dict
post_search_aggregate200_response_metadata_dict = post_search_aggregate200_response_metadata_instance.to_dict()
# create an instance of PostSearchAggregate200ResponseMetadata from a dict
post_search_aggregate200_response_metadata_from_dict = PostSearchAggregate200ResponseMetadata.from_dict(post_search_aggregate200_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


