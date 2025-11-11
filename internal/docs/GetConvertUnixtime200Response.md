# GetConvertUnixtime200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 状态码，200代表操作成功。 | [optional] 
**datetime** | **str** | 标准格式（YYYY-MM-DD HH:mm:ss）的日期时间字符串。 | [optional] 
**timestamp** | **int** | 转换后的10位秒级Unix时间戳。 | [optional] 

## Example

```python
from uapi.models.get_convert_unixtime200_response import GetConvertUnixtime200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertUnixtime200Response from a JSON string
get_convert_unixtime200_response_instance = GetConvertUnixtime200Response.from_json(json)
# print the JSON string representation of the object
print(GetConvertUnixtime200Response.to_json())

# convert the object into a dict
get_convert_unixtime200_response_dict = get_convert_unixtime200_response_instance.to_dict()
# create an instance of GetConvertUnixtime200Response from a dict
get_convert_unixtime200_response_from_dict = GetConvertUnixtime200Response.from_dict(get_convert_unixtime200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


