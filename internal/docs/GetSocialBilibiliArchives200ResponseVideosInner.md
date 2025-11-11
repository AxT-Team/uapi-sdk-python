# GetSocialBilibiliArchives200ResponseVideosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aid** | **int** | 视频AID | [optional] 
**bvid** | **str** | BV号 | [optional] 
**title** | **str** | 标题 | [optional] 
**cover** | **str** | 封面URL | [optional] 
**duration** | **int** | 时长(秒) | [optional] 
**play_count** | **int** | 播放量 | [optional] 
**publish_time** | **int** | 发布时间戳 | [optional] 
**create_time** | **int** | 创建时间戳 | [optional] 
**state** | **int** | 视频状态 | [optional] 
**is_ugc_pay** | **int** | 是否付费视频。0&#x3D;免费，1&#x3D;付费 | [optional] 
**is_interactive** | **bool** | 是否为互动视频 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_archives200_response_videos_inner import GetSocialBilibiliArchives200ResponseVideosInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliArchives200ResponseVideosInner from a JSON string
get_social_bilibili_archives200_response_videos_inner_instance = GetSocialBilibiliArchives200ResponseVideosInner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliArchives200ResponseVideosInner.to_json())

# convert the object into a dict
get_social_bilibili_archives200_response_videos_inner_dict = get_social_bilibili_archives200_response_videos_inner_instance.to_dict()
# create an instance of GetSocialBilibiliArchives200ResponseVideosInner from a dict
get_social_bilibili_archives200_response_videos_inner_from_dict = GetSocialBilibiliArchives200ResponseVideosInner.from_dict(get_social_bilibili_archives200_response_videos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


