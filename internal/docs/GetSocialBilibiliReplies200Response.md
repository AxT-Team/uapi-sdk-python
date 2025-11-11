# GetSocialBilibiliReplies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**GetSocialBilibiliReplies200ResponsePage**](GetSocialBilibiliReplies200ResponsePage.md) |  | [optional] 
**hots** | **List[object]** | 热门评论列表。结构与 &#x60;replies&#x60; 中的对象一致。如果当前页是第一页，且有热门评论，则此数组非空。 | [optional] 
**replies** | [**List[GetSocialBilibiliReplies200ResponseRepliesInner]**](GetSocialBilibiliReplies200ResponseRepliesInner.md) | 当前页的评论列表。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_replies200_response import GetSocialBilibiliReplies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliReplies200Response from a JSON string
get_social_bilibili_replies200_response_instance = GetSocialBilibiliReplies200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliReplies200Response.to_json())

# convert the object into a dict
get_social_bilibili_replies200_response_dict = get_social_bilibili_replies200_response_instance.to_dict()
# create an instance of GetSocialBilibiliReplies200Response from a dict
get_social_bilibili_replies200_response_from_dict = GetSocialBilibiliReplies200Response.from_dict(get_social_bilibili_replies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


