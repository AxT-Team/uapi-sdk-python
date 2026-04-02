# GetSocialBilibiliVideoinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bvid** | **str** | 稿件的BV号。 | [optional] 
**aid** | **float** | 稿件的AV号。 | [optional] 
**videos** | **float** | 稿件分P总数。如果是单P视频，则为1。 | [optional] 
**tid** | **float** | 视频所属的子分区 ID。 | [optional] 
**tname** | **str** | 视频所属的子分区名称。 | [optional] 
**copyright** | **float** | 视频类型。1代表原创，2代表转载。 | [optional] 
**pic** | **str** | 稿件封面图片的URL。这是一个可以直接在网页上展示的链接。 | [optional] 
**title** | **str** | 稿件的标题。 | [optional] 
**pubdate** | **float** | 稿件发布时间的Unix时间戳（秒）。 | [optional] 
**ctime** | **float** | 用户投稿时间的Unix时间戳（秒）。 | [optional] 
**desc** | **str** | 视频简介。可能会包含HTML换行符。 | [optional] 
**desc_v2** | [**List[GetSocialBilibiliVideoinfo200ResponseDescV2Inner]**](GetSocialBilibiliVideoinfo200ResponseDescV2Inner.md) | 结构化简介片段。 | [optional] 
**state** | **float** | 视频状态码。 | [optional] 
**duration** | **float** | 稿件总时长（所有分P累加），单位为秒。 | [optional] 
**rights** | [**GetSocialBilibiliVideoinfo200ResponseRights**](GetSocialBilibiliVideoinfo200ResponseRights.md) |  | [optional] 
**owner** | [**GetSocialBilibiliVideoinfo200ResponseOwner**](GetSocialBilibiliVideoinfo200ResponseOwner.md) |  | [optional] 
**stat** | [**GetSocialBilibiliVideoinfo200ResponseStat**](GetSocialBilibiliVideoinfo200ResponseStat.md) |  | [optional] 
**dynamic** | **str** | 投稿时附带的动态文字。 | [optional] 
**cid** | **float** | 主分P的 CID（弹幕 ID）。 | [optional] 
**dimension** | [**GetSocialBilibiliVideoinfo200ResponseDimension**](GetSocialBilibiliVideoinfo200ResponseDimension.md) |  | [optional] 
**no_cache** | **bool** | 不缓存标记。 | [optional] 
**pages** | [**List[GetSocialBilibiliVideoinfo200ResponsePagesInner]**](GetSocialBilibiliVideoinfo200ResponsePagesInner.md) | 视频分P列表。即使是单P视频，该数组也包含一个元素。 | [optional] 
**subtitle** | [**GetSocialBilibiliVideoinfo200ResponseSubtitle**](GetSocialBilibiliVideoinfo200ResponseSubtitle.md) |  | [optional] 
**staff** | [**List[GetSocialBilibiliVideoinfo200ResponseStaffInner]**](GetSocialBilibiliVideoinfo200ResponseStaffInner.md) | 联合投稿成员列表。 | [optional] 
**ugc_season** | [**GetSocialBilibiliVideoinfo200ResponseUgcSeason**](GetSocialBilibiliVideoinfo200ResponseUgcSeason.md) |  | [optional] 
**is_chargeable_season** | **bool** | 是否为付费合集。 | [optional] 
**is_story** | **bool** | 是否为剧情类视频。 | [optional] 
**honor_reply** | [**GetSocialBilibiliVideoinfo200ResponseHonorReply**](GetSocialBilibiliVideoinfo200ResponseHonorReply.md) |  | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response import GetSocialBilibiliVideoinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200Response from a JSON string
get_social_bilibili_videoinfo200_response_instance = GetSocialBilibiliVideoinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200Response.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_dict = get_social_bilibili_videoinfo200_response_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200Response from a dict
get_social_bilibili_videoinfo200_response_from_dict = GetSocialBilibiliVideoinfo200Response.from_dict(get_social_bilibili_videoinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


