# GetMiscLunartime200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 业务状态码，200 表示成功。 | [optional] 
**message** | **str** | 状态描述。 | [optional] 
**data** | [**GetMiscLunartime200ResponseData**](GetMiscLunartime200ResponseData.md) |  | [optional] 

## Example

```python
from uapi.models.get_misc_lunartime200_response import GetMiscLunartime200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscLunartime200Response from a JSON string
get_misc_lunartime200_response_instance = GetMiscLunartime200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscLunartime200Response.to_json())

# convert the object into a dict
get_misc_lunartime200_response_dict = get_misc_lunartime200_response_instance.to_dict()
# create an instance of GetMiscLunartime200Response from a dict
get_misc_lunartime200_response_from_dict = GetMiscLunartime200Response.from_dict(get_misc_lunartime200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


