# PostClipzyStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compressed_data** | **str** | 必需：经过加密和 LZString 压缩后的 Base64 字符串。请参考文档首页的JS代码示例。 | 
**ttl** | **float** | 可选：片段的留存时间（秒）。正数表示秒数（最大约30天），-1 表示永久存储。默认为 3600。 | [optional] 

## Example

```python
from uapi.models.post_clipzy_store_request import PostClipzyStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClipzyStoreRequest from a JSON string
post_clipzy_store_request_instance = PostClipzyStoreRequest.from_json(json)
# print the JSON string representation of the object
print(PostClipzyStoreRequest.to_json())

# convert the object into a dict
post_clipzy_store_request_dict = post_clipzy_store_request_instance.to_dict()
# create an instance of PostClipzyStoreRequest from a dict
post_clipzy_store_request_from_dict = PostClipzyStoreRequest.from_dict(post_clipzy_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


