# GetSocialBilibiliVideoinfo200ResponseSubtitleListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | 字幕 ID。 | [optional] 
**lan** | **str** | 语言代码。 | [optional] 
**lan_doc** | **str** | 语言名称。 | [optional] 
**is_lock** | **bool** | 是否锁定。 | [optional] 
**author_mid** | **float** | 字幕作者 UID。 | [optional] 
**subtitle_url** | **str** | 字幕文件链接。 | [optional] 
**author** | [**GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor**](GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor.md) |  | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_subtitle_list_inner import GetSocialBilibiliVideoinfo200ResponseSubtitleListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitleListInner from a JSON string
get_social_bilibili_videoinfo200_response_subtitle_list_inner_instance = GetSocialBilibiliVideoinfo200ResponseSubtitleListInner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseSubtitleListInner.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_subtitle_list_inner_dict = get_social_bilibili_videoinfo200_response_subtitle_list_inner_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitleListInner from a dict
get_social_bilibili_videoinfo200_response_subtitle_list_inner_from_dict = GetSocialBilibiliVideoinfo200ResponseSubtitleListInner.from_dict(get_social_bilibili_videoinfo200_response_subtitle_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


