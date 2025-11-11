# GetSocialBilibiliArchives200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | 总稿件数 | [optional] 
**page** | **int** | 当前页码 | [optional] 
**size** | **int** | 每页数量 | [optional] 
**videos** | [**List[GetSocialBilibiliArchives200ResponseVideosInner]**](GetSocialBilibiliArchives200ResponseVideosInner.md) | 视频列表 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_archives200_response import GetSocialBilibiliArchives200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliArchives200Response from a JSON string
get_social_bilibili_archives200_response_instance = GetSocialBilibiliArchives200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliArchives200Response.to_json())

# convert the object into a dict
get_social_bilibili_archives200_response_dict = get_social_bilibili_archives200_response_instance.to_dict()
# create an instance of GetSocialBilibiliArchives200Response from a dict
get_social_bilibili_archives200_response_from_dict = GetSocialBilibiliArchives200Response.from_dict(get_social_bilibili_archives200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


