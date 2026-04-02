# GetSocialBilibiliVideoinfo200ResponseStat

视频的核心数据统计。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **float** | AV 号。 | [optional] 
**view** | **float** | 播放数。 | [optional] 
**danmaku** | **float** | 弹幕数。 | [optional] 
**reply** | **float** | 评论数。 | [optional] 
**favorite** | **float** | 收藏数。 | [optional] 
**coin** | **float** | 投币数。 | [optional] 
**share** | **float** | 分享数。 | [optional] 
**like** | **float** | 获赞数。 | [optional] 
**now_rank** | **float** | 当前全站/分区排名。 | [optional] 
**his_rank** | **float** | 历史排名。 | [optional] 
**dislike** | **float** | 点踩量（通常为 0）。 | [optional] 
**evaluation** | **str** | 评分/评估文案，通常为空。 | [optional] 
**vt** | **float** | 视频类型相关历史字段。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_stat import GetSocialBilibiliVideoinfo200ResponseStat

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseStat from a JSON string
get_social_bilibili_videoinfo200_response_stat_instance = GetSocialBilibiliVideoinfo200ResponseStat.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseStat.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_stat_dict = get_social_bilibili_videoinfo200_response_stat_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseStat from a dict
get_social_bilibili_videoinfo200_response_stat_from_dict = GetSocialBilibiliVideoinfo200ResponseStat.from_dict(get_social_bilibili_videoinfo200_response_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


