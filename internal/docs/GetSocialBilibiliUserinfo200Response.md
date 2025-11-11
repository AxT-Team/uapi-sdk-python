# GetSocialBilibiliUserinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**GetSocialBilibiliUserinfo200ResponseData**](GetSocialBilibiliUserinfo200ResponseData.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_userinfo200_response import GetSocialBilibiliUserinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliUserinfo200Response from a JSON string
get_social_bilibili_userinfo200_response_instance = GetSocialBilibiliUserinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliUserinfo200Response.to_json())

# convert the object into a dict
get_social_bilibili_userinfo200_response_dict = get_social_bilibili_userinfo200_response_instance.to_dict()
# create an instance of GetSocialBilibiliUserinfo200Response from a dict
get_social_bilibili_userinfo200_response_from_dict = GetSocialBilibiliUserinfo200Response.from_dict(get_social_bilibili_userinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


