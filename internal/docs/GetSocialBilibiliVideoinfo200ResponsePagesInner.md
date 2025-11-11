# GetSocialBilibiliVideoinfo200ResponsePagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **float** | 分P的唯一标识CID，用于获取弹幕等。 | [optional] 
**page** | **float** | 分P的序号，从1开始。 | [optional] 
**part** | **str** | 分P的标题。对于单P视频，通常是视频主标题。 | [optional] 
**duration** | **float** | 该分P的持续时间，单位为秒。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_pages_inner import GetSocialBilibiliVideoinfo200ResponsePagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponsePagesInner from a JSON string
get_social_bilibili_videoinfo200_response_pages_inner_instance = GetSocialBilibiliVideoinfo200ResponsePagesInner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponsePagesInner.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_pages_inner_dict = get_social_bilibili_videoinfo200_response_pages_inner_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponsePagesInner from a dict
get_social_bilibili_videoinfo200_response_pages_inner_from_dict = GetSocialBilibiliVideoinfo200ResponsePagesInner.from_dict(get_social_bilibili_videoinfo200_response_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


