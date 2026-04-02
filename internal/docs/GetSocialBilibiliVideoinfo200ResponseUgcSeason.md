# GetSocialBilibiliVideoinfo200ResponseUgcSeason

合集信息。若视频不属于合集则为 null。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | 合集 ID。 | [optional] 
**title** | **str** | 合集标题。 | [optional] 
**cover** | **str** | 合集封面。 | [optional] 
**mid** | **float** | 合集作者 UID。 | [optional] 
**intro** | **str** | 合集简介。 | [optional] 
**ep_count** | **float** | 合集内视频数量。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_ugc_season import GetSocialBilibiliVideoinfo200ResponseUgcSeason

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseUgcSeason from a JSON string
get_social_bilibili_videoinfo200_response_ugc_season_instance = GetSocialBilibiliVideoinfo200ResponseUgcSeason.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseUgcSeason.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_ugc_season_dict = get_social_bilibili_videoinfo200_response_ugc_season_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseUgcSeason from a dict
get_social_bilibili_videoinfo200_response_ugc_season_from_dict = GetSocialBilibiliVideoinfo200ResponseUgcSeason.from_dict(get_social_bilibili_videoinfo200_response_ugc_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


