# GetSocialBilibiliReplies200ResponseRepliesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpid** | **float** | 评论的唯一ID (Reply ID)。 | [optional] 
**oid** | **float** | 评论区对象ID，即视频的aid。 | [optional] 
**mid** | **float** | 发表评论的用户的mid。 | [optional] 
**root** | **float** | 根评论的rpid。如果为0，表示这条评论是根评论。 | [optional] 
**parent** | **float** | 回复的父级评论的rpid。如果为0，表示是根评论。 | [optional] 
**count** | **float** | 这条评论下的回复（楼中楼）数量。 | [optional] 
**ctime** | **float** | 评论发送时间的Unix时间戳（秒）。 | [optional] 
**like** | **float** | 该评论获得的点赞数。 | [optional] 
**member** | [**GetSocialBilibiliReplies200ResponseRepliesInnerMember**](GetSocialBilibiliReplies200ResponseRepliesInnerMember.md) |  | [optional] 
**content** | [**GetSocialBilibiliReplies200ResponseRepliesInnerContent**](GetSocialBilibiliReplies200ResponseRepliesInnerContent.md) |  | [optional] 
**replies** | **List[object]** | 楼中楼回复列表。结构与顶层评论对象一致，但通常此数组为空，需要单独请求。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_replies200_response_replies_inner import GetSocialBilibiliReplies200ResponseRepliesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliReplies200ResponseRepliesInner from a JSON string
get_social_bilibili_replies200_response_replies_inner_instance = GetSocialBilibiliReplies200ResponseRepliesInner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliReplies200ResponseRepliesInner.to_json())

# convert the object into a dict
get_social_bilibili_replies200_response_replies_inner_dict = get_social_bilibili_replies200_response_replies_inner_instance.to_dict()
# create an instance of GetSocialBilibiliReplies200ResponseRepliesInner from a dict
get_social_bilibili_replies200_response_replies_inner_from_dict = GetSocialBilibiliReplies200ResponseRepliesInner.from_dict(get_social_bilibili_replies200_response_replies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


