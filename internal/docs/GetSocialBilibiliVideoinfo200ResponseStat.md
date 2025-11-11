# GetSocialBilibiliVideoinfo200ResponseStat

视频的核心数据统计。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **float** | 播放数。 | [optional] 
**danmaku** | **float** | 弹幕数。 | [optional] 
**reply** | **float** | 评论数。 | [optional] 
**favorite** | **float** | 收藏数。 | [optional] 
**coin** | **float** | 投币数。 | [optional] 
**share** | **float** | 分享数。 | [optional] 
**like** | **float** | 获赞数。 | [optional] 

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


