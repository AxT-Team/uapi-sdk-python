# GetSocialBilibiliReplies200ResponseRepliesInnerMember

发表评论的用户信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uname** | **str** | 用户昵称。 | [optional] 
**sex** | **str** | 用户性别。 | [optional] 
**avatar** | **str** | 用户头像的URL。 | [optional] 
**level_info** | [**GetSocialBilibiliReplies200ResponseRepliesInnerMemberLevelInfo**](GetSocialBilibiliReplies200ResponseRepliesInnerMemberLevelInfo.md) |  | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_replies200_response_replies_inner_member import GetSocialBilibiliReplies200ResponseRepliesInnerMember

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliReplies200ResponseRepliesInnerMember from a JSON string
get_social_bilibili_replies200_response_replies_inner_member_instance = GetSocialBilibiliReplies200ResponseRepliesInnerMember.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliReplies200ResponseRepliesInnerMember.to_json())

# convert the object into a dict
get_social_bilibili_replies200_response_replies_inner_member_dict = get_social_bilibili_replies200_response_replies_inner_member_instance.to_dict()
# create an instance of GetSocialBilibiliReplies200ResponseRepliesInnerMember from a dict
get_social_bilibili_replies200_response_replies_inner_member_from_dict = GetSocialBilibiliReplies200ResponseRepliesInnerMember.from_dict(get_social_bilibili_replies200_response_replies_inner_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


