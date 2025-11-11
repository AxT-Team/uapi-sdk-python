# GetSocialBilibiliReplies200ResponsePage

分页信息概览。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num** | **float** | 当前所在的页码。 | [optional] 
**size** | **float** | 每页的项数。 | [optional] 
**count** | **float** | 根评论（即直接评论视频的评论）的总数。 | [optional] 
**acount** | **float** | 评论区总评论数，包含了所有的楼中楼回复。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_replies200_response_page import GetSocialBilibiliReplies200ResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliReplies200ResponsePage from a JSON string
get_social_bilibili_replies200_response_page_instance = GetSocialBilibiliReplies200ResponsePage.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliReplies200ResponsePage.to_json())

# convert the object into a dict
get_social_bilibili_replies200_response_page_dict = get_social_bilibili_replies200_response_page_instance.to_dict()
# create an instance of GetSocialBilibiliReplies200ResponsePage from a dict
get_social_bilibili_replies200_response_page_from_dict = GetSocialBilibiliReplies200ResponsePage.from_dict(get_social_bilibili_replies200_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


