# GetImageTobase64200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** | 转换后的完整Base64 Data URI，可以直接在CSS或HTML中使用。 | [optional] 
**code** | **int** | 状态码，200代表成功。 | [optional] 
**msg** | **str** | 操作结果描述。 | [optional] 

## Example

```python
from uapi.models.get_image_tobase64200_response import GetImageTobase64200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageTobase64200Response from a JSON string
get_image_tobase64200_response_instance = GetImageTobase64200Response.from_json(json)
# print the JSON string representation of the object
print(GetImageTobase64200Response.to_json())

# convert the object into a dict
get_image_tobase64200_response_dict = get_image_tobase64200_response_instance.to_dict()
# create an instance of GetImageTobase64200Response from a dict
get_image_tobase64200_response_from_dict = GetImageTobase64200Response.from_dict(get_image_tobase64200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


