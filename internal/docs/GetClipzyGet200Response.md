# GetClipzyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compressed_data** | **str** | 加密并使用 LZString 压缩后的 Base64 数据。 | [optional] 

## Example

```python
from uapi.models.get_clipzy_get200_response import GetClipzyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClipzyGet200Response from a JSON string
get_clipzy_get200_response_instance = GetClipzyGet200Response.from_json(json)
# print the JSON string representation of the object
print(GetClipzyGet200Response.to_json())

# convert the object into a dict
get_clipzy_get200_response_dict = get_clipzy_get200_response_instance.to_dict()
# create an instance of GetClipzyGet200Response from a dict
get_clipzy_get200_response_from_dict = GetClipzyGet200Response.from_dict(get_clipzy_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


