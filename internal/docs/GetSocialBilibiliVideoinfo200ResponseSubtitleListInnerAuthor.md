# GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor

字幕作者信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mid** | **float** | 作者 UID。 | [optional] 
**name** | **str** | 作者昵称。 | [optional] 
**face** | **str** | 作者头像链接。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_subtitle_list_inner_author import GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor from a JSON string
get_social_bilibili_videoinfo200_response_subtitle_list_inner_author_instance = GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_subtitle_list_inner_author_dict = get_social_bilibili_videoinfo200_response_subtitle_list_inner_author_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor from a dict
get_social_bilibili_videoinfo200_response_subtitle_list_inner_author_from_dict = GetSocialBilibiliVideoinfo200ResponseSubtitleListInnerAuthor.from_dict(get_social_bilibili_videoinfo200_response_subtitle_list_inner_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


