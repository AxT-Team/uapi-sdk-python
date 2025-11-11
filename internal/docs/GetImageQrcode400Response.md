# GetImageQrcode400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_image_qrcode400_response import GetImageQrcode400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageQrcode400Response from a JSON string
get_image_qrcode400_response_instance = GetImageQrcode400Response.from_json(json)
# print the JSON string representation of the object
print(GetImageQrcode400Response.to_json())

# convert the object into a dict
get_image_qrcode400_response_dict = get_image_qrcode400_response_instance.to_dict()
# create an instance of GetImageQrcode400Response from a dict
get_image_qrcode400_response_from_dict = GetImageQrcode400Response.from_dict(get_image_qrcode400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


