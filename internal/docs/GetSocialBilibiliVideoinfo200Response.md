# GetSocialBilibiliVideoinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bvid** | **str** | 稿件的BV号。 | [optional] 
**aid** | **float** | 稿件的AV号。 | [optional] 
**videos** | **float** | 稿件分P总数。如果是单P视频，则为1。 | [optional] 
**tname** | **str** | 视频所属的子分区名称。 | [optional] 
**copyright** | **float** | 视频类型。1代表原创，2代表转载。 | [optional] 
**pic** | **str** | 稿件封面图片的URL。这是一个可以直接在网页上展示的链接。 | [optional] 
**title** | **str** | 稿件的标题。 | [optional] 
**pubdate** | **float** | 稿件发布时间的Unix时间戳（秒）。 | [optional] 
**ctime** | **float** | 用户投稿时间的Unix时间戳（秒）。 | [optional] 
**desc** | **str** | 视频简介。可能会包含HTML换行符。 | [optional] 
**duration** | **float** | 稿件总时长（所有分P累加），单位为秒。 | [optional] 
**owner** | [**GetSocialBilibiliVideoinfo200ResponseOwner**](GetSocialBilibiliVideoinfo200ResponseOwner.md) |  | [optional] 
**stat** | [**GetSocialBilibiliVideoinfo200ResponseStat**](GetSocialBilibiliVideoinfo200ResponseStat.md) |  | [optional] 
**pages** | [**List[GetSocialBilibiliVideoinfo200ResponsePagesInner]**](GetSocialBilibiliVideoinfo200ResponsePagesInner.md) | 视频分P列表。即使是单P视频，该数组也包含一个元素。 | [optional] 

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


