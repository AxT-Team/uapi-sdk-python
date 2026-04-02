# GetSocialBilibiliVideoinfo200ResponseRights

视频权限开关（0 或 1）。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bp** | **float** | 是否可以承包/付费（老字段）。 | [optional] 
**elec** | **float** | 是否允许付费充电。 | [optional] 
**download** | **float** | 是否允许缓存/下载。 | [optional] 
**movie** | **float** | 是否为电影。 | [optional] 
**pay** | **float** | 是否需要付费观看。 | [optional] 
**hd5** | **float** | 高码率相关老字段。 | [optional] 
**no_reprint** | **float** | 是否禁止转载（1 表示禁止）。 | [optional] 
**autoplay** | **float** | 是否允许自动播放。 | [optional] 
**ugc_pay** | **float** | 是否为 UGC 付费内容。 | [optional] 
**is_cooperation** | **float** | 是否为合作视频。 | [optional] 
**ugc_pay_preview** | **float** | 是否允许付费内容试看。 | [optional] 
**no_background** | **float** | 背景相关控制字段。 | [optional] 
**clean_mode** | **float** | 是否为纯净模式。 | [optional] 
**is_stein_gate** | **float** | 互动剧情相关字段。 | [optional] 
**is_360** | **float** | 是否为 360° 全景视频。 | [optional] 
**no_share** | **float** | 是否禁止分享（1 表示禁止）。 | [optional] 
**arc_pay** | **float** | 是否为付费视频。 | [optional] 
**free_watch** | **float** | 付费视频是否允许免费试看。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_rights import GetSocialBilibiliVideoinfo200ResponseRights

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseRights from a JSON string
get_social_bilibili_videoinfo200_response_rights_instance = GetSocialBilibiliVideoinfo200ResponseRights.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseRights.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_rights_dict = get_social_bilibili_videoinfo200_response_rights_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseRights from a dict
get_social_bilibili_videoinfo200_response_rights_from_dict = GetSocialBilibiliVideoinfo200ResponseRights.from_dict(get_social_bilibili_videoinfo200_response_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


