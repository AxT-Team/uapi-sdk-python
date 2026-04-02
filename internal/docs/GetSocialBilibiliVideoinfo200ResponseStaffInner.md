# GetSocialBilibiliVideoinfo200ResponseStaffInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mid** | **float** | 成员 UID。 | [optional] 
**title** | **str** | 成员角色标题。 | [optional] 
**name** | **str** | 成员昵称。 | [optional] 
**face** | **str** | 成员头像链接。 | [optional] 
**follower** | **float** | 成员粉丝数。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_staff_inner import GetSocialBilibiliVideoinfo200ResponseStaffInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseStaffInner from a JSON string
get_social_bilibili_videoinfo200_response_staff_inner_instance = GetSocialBilibiliVideoinfo200ResponseStaffInner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseStaffInner.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_staff_inner_dict = get_social_bilibili_videoinfo200_response_staff_inner_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseStaffInner from a dict
get_social_bilibili_videoinfo200_response_staff_inner_from_dict = GetSocialBilibiliVideoinfo200ResponseStaffInner.from_dict(get_social_bilibili_videoinfo200_response_staff_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


