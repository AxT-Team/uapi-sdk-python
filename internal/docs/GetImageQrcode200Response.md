# GetImageQrcode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | 图片的URL。当&#x60;format&#x3D;json_url&#x60;时是临时公网URL；当&#x60;format&#x3D;json&#x60;时是Base64 Data URI。 | [optional] 

## Example

```python
from uapi.models.get_image_qrcode200_response import GetImageQrcode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageQrcode200Response from a JSON string
get_image_qrcode200_response_instance = GetImageQrcode200Response.from_json(json)
# print the JSON string representation of the object
print(GetImageQrcode200Response.to_json())

# convert the object into a dict
get_image_qrcode200_response_dict = get_image_qrcode200_response_instance.to_dict()
# create an instance of GetImageQrcode200Response from a dict
get_image_qrcode200_response_from_dict = GetImageQrcode200Response.from_dict(get_image_qrcode200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


