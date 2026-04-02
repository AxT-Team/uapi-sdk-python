# GetSocialBilibiliVideoinfo200ResponseHonorReply

视频荣誉信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**honor** | [**List[GetSocialBilibiliVideoinfo200ResponseHonorReplyHonorInner]**](GetSocialBilibiliVideoinfo200ResponseHonorReplyHonorInner.md) | 荣誉列表。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_honor_reply import GetSocialBilibiliVideoinfo200ResponseHonorReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseHonorReply from a JSON string
get_social_bilibili_videoinfo200_response_honor_reply_instance = GetSocialBilibiliVideoinfo200ResponseHonorReply.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseHonorReply.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_honor_reply_dict = get_social_bilibili_videoinfo200_response_honor_reply_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseHonorReply from a dict
get_social_bilibili_videoinfo200_response_honor_reply_from_dict = GetSocialBilibiliVideoinfo200ResponseHonorReply.from_dict(get_social_bilibili_videoinfo200_response_honor_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


