# GetSocialBilibiliVideoinfo200ResponseOwner

视频UP主信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mid** | **float** | UP主的UID。 | [optional] 
**name** | **str** | UP主昵称。 | [optional] 
**face** | **str** | UP主头像的URL。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_owner import GetSocialBilibiliVideoinfo200ResponseOwner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseOwner from a JSON string
get_social_bilibili_videoinfo200_response_owner_instance = GetSocialBilibiliVideoinfo200ResponseOwner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseOwner.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_owner_dict = get_social_bilibili_videoinfo200_response_owner_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseOwner from a dict
get_social_bilibili_videoinfo200_response_owner_from_dict = GetSocialBilibiliVideoinfo200ResponseOwner.from_dict(get_social_bilibili_videoinfo200_response_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


