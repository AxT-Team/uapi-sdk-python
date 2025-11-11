# GetImageQrcode500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_image_qrcode500_response import GetImageQrcode500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageQrcode500Response from a JSON string
get_image_qrcode500_response_instance = GetImageQrcode500Response.from_json(json)
# print the JSON string representation of the object
print(GetImageQrcode500Response.to_json())

# convert the object into a dict
get_image_qrcode500_response_dict = get_image_qrcode500_response_instance.to_dict()
# create an instance of GetImageQrcode500Response from a dict
get_image_qrcode500_response_from_dict = GetImageQrcode500Response.from_dict(get_image_qrcode500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


