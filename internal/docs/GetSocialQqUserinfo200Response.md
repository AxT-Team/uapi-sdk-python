# GetSocialQqUserinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | 年龄 | [optional] 
**avatar_url** | **str** | 头像URL | [optional] 
**big_club_level** | **int** | QQ大会员等级 | [optional] 
**email** | **str** | QQ邮箱 | [optional] 
**green_diamond_level** | **int** | 绿钻等级（可选） | [optional] 
**is_big_club** | **bool** | 是否为QQ大会员用户 | [optional] 
**is_svip** | **bool** | 是否为SVIP用户 | [optional] 
**is_vip** | **bool** | 是否为VIP用户 | [optional] 
**is_years_vip** | **bool** | 是否为年费VIP用户 | [optional] 
**last_updated** | **str** | 最后更新时间（ISO 8601格式） | [optional] 
**location** | **str** | 地理位置（省市） | [optional] 
**long_nick** | **str** | 个性签名 | [optional] 
**lover_vip_level** | **int** | 情侣/恋人类会员等级（可选） | [optional] 
**nickname** | **str** | 用户昵称 | [optional] 
**privilege_icons** | [**GetSocialQqUserinfo200ResponsePrivilegeIcons**](GetSocialQqUserinfo200ResponsePrivilegeIcons.md) |  | [optional] 
**qid** | **str** | QQ个性域名 | [optional] 
**qq** | **str** | QQ号 | [optional] 
**qq_level** | **int** | QQ等级。用户隐藏时返回 null | [optional] 
**reg_time** | **str** | 注册时间（ISO 8601格式） | [optional] 
**sex** | **str** | 性别 | [optional] 
**video_vip_level** | **int** | 腾讯影视会员等级（可选） | [optional] 
**vip_level** | **int** | VIP等级 | [optional] 
**vip_status** | **int** | 会员开通状态 | [optional] 
**vip_type** | **int** | 会员类型 | [optional] 
**yellow_diamond_level** | **int** | 黄钻等级（可选） | [optional] 

## Example

```python
from uapi.models.get_social_qq_userinfo200_response import GetSocialQqUserinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialQqUserinfo200Response from a JSON string
get_social_qq_userinfo200_response_instance = GetSocialQqUserinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialQqUserinfo200Response.to_json())

# convert the object into a dict
get_social_qq_userinfo200_response_dict = get_social_qq_userinfo200_response_instance.to_dict()
# create an instance of GetSocialQqUserinfo200Response from a dict
get_social_qq_userinfo200_response_from_dict = GetSocialQqUserinfo200Response.from_dict(get_social_qq_userinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


