# GetSocialBilibiliVideoinfo200ResponseSubtitle

字幕信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_submit** | **bool** | 是否允许观众投稿字幕。 | [optional] 
**list** | [**List[GetSocialBilibiliVideoinfo200ResponseSubtitleListInner]**](GetSocialBilibiliVideoinfo200ResponseSubtitleListInner.md) | 字幕列表。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_subtitle import GetSocialBilibiliVideoinfo200ResponseSubtitle

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitle from a JSON string
get_social_bilibili_videoinfo200_response_subtitle_instance = GetSocialBilibiliVideoinfo200ResponseSubtitle.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseSubtitle.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_subtitle_dict = get_social_bilibili_videoinfo200_response_subtitle_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitle from a dict
get_social_bilibili_videoinfo200_response_subtitle_from_dict = GetSocialBilibiliVideoinfo200ResponseSubtitle.from_dict(get_social_bilibili_videoinfo200_response_subtitle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


