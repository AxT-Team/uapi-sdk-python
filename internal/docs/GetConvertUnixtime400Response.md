# GetConvertUnixtime400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 机器可读的错误代码。 | [optional] 
**details** | **object** | 包含错误详情的对象。 | [optional] 
**message** | **str** | 人类可读的错误描述信息。 | [optional] 

## Example

```python
from uapi.models.get_convert_unixtime400_response import GetConvertUnixtime400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConvertUnixtime400Response from a JSON string
get_convert_unixtime400_response_instance = GetConvertUnixtime400Response.from_json(json)
# print the JSON string representation of the object
print(GetConvertUnixtime400Response.to_json())

# convert the object into a dict
get_convert_unixtime400_response_dict = get_convert_unixtime400_response_instance.to_dict()
# create an instance of GetConvertUnixtime400Response from a dict
get_convert_unixtime400_response_from_dict = GetConvertUnixtime400Response.from_dict(get_convert_unixtime400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


