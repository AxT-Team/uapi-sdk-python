# PostSearchAggregate200ResponseMetadataRequestParams

服务端实际生效的请求参数回显

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 实际执行的搜索词 | [optional] 
**limit** | **int** | 实际生效的返回条数 | [optional] 
**page** | **int** | 实际生效的页码 | [optional] 
**timeout_ms** | **int** | 实际生效的超时时间（毫秒） | [optional] 
**sort** | **str** | 实际生效的排序方式 | [optional] 

## Example

```python
from uapi.models.post_search_aggregate200_response_metadata_request_params import PostSearchAggregate200ResponseMetadataRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostSearchAggregate200ResponseMetadataRequestParams from a JSON string
post_search_aggregate200_response_metadata_request_params_instance = PostSearchAggregate200ResponseMetadataRequestParams.from_json(json)
# print the JSON string representation of the object
print(PostSearchAggregate200ResponseMetadataRequestParams.to_json())

# convert the object into a dict
post_search_aggregate200_response_metadata_request_params_dict = post_search_aggregate200_response_metadata_request_params_instance.to_dict()
# create an instance of PostSearchAggregate200ResponseMetadataRequestParams from a dict
post_search_aggregate200_response_metadata_request_params_from_dict = PostSearchAggregate200ResponseMetadataRequestParams.from_dict(post_search_aggregate200_response_metadata_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


