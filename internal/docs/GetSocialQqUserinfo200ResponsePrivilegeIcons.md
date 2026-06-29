# GetSocialQqUserinfo200ResponsePrivilegeIcons

部分特权图标状态

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**big_club** | **bool** | QQ大会员图标是否点亮 | [optional] 
**svip** | **bool** | SVIP图标是否点亮 | [optional] 
**vip** | **bool** | VIP图标是否点亮 | [optional] 
**years_vip** | **bool** | 年费VIP图标是否点亮 | [optional] 

## Example

```python
from uapi.models.get_social_qq_userinfo200_response_privilege_icons import GetSocialQqUserinfo200ResponsePrivilegeIcons

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialQqUserinfo200ResponsePrivilegeIcons from a JSON string
get_social_qq_userinfo200_response_privilege_icons_instance = GetSocialQqUserinfo200ResponsePrivilegeIcons.from_json(json)
# print the JSON string representation of the object
print(GetSocialQqUserinfo200ResponsePrivilegeIcons.to_json())

# convert the object into a dict
get_social_qq_userinfo200_response_privilege_icons_dict = get_social_qq_userinfo200_response_privilege_icons_instance.to_dict()
# create an instance of GetSocialQqUserinfo200ResponsePrivilegeIcons from a dict
get_social_qq_userinfo200_response_privilege_icons_from_dict = GetSocialQqUserinfo200ResponsePrivilegeIcons.from_dict(get_social_qq_userinfo200_response_privilege_icons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


