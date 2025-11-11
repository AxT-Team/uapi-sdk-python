# GetSocialBilibiliLiveroom200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **float** | 主播的用户ID (mid)。 | [optional] 
**room_id** | **float** | 直播间的真实房间号（长号）。 | [optional] 
**short_id** | **float** | 直播间的短号（靓号）。如果没有设置，则为0。 | [optional] 
**attention** | **float** | 主播的粉丝数（关注数量）。 | [optional] 
**online** | **float** | 直播间当前的人气值。注意这不是真实在线人数。 | [optional] 
**live_status** | **float** | 直播状态。0:未开播, 1:直播中, 2:轮播中。 | [optional] 
**area_id** | **float** | 分区ID。 | [optional] 
**parent_area_name** | **str** | 父分区名称。 | [optional] 
**area_name** | **str** | 子分区名称。 | [optional] 
**background** | **str** | 直播间背景图的URL。 | [optional] 
**title** | **str** | 当前直播间的标题。 | [optional] 
**user_cover** | **str** | 用户设置的直播间封面URL。 | [optional] 
**description** | **str** | 直播间公告或描述，支持换行符。 | [optional] 
**live_time** | **str** | 本次直播开始的时间，格式为 &#x60;YYYY-MM-DD HH:mm:ss&#x60;。如果未开播，则为空字符串。 | [optional] 
**tags** | **str** | 直播间设置的标签，以逗号分隔。 | [optional] 
**hot_words** | **List[str]** | 直播间热词列表，通常用于弹幕互动。 | [optional] 
**new_pendants** | **object** | 主播佩戴的头像框、大航海等级等信息，结构可能比较复杂。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_liveroom200_response import GetSocialBilibiliLiveroom200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliLiveroom200Response from a JSON string
get_social_bilibili_liveroom200_response_instance = GetSocialBilibiliLiveroom200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliLiveroom200Response.to_json())

# convert the object into a dict
get_social_bilibili_liveroom200_response_dict = get_social_bilibili_liveroom200_response_instance.to_dict()
# create an instance of GetSocialBilibiliLiveroom200Response from a dict
get_social_bilibili_liveroom200_response_from_dict = GetSocialBilibiliLiveroom200Response.from_dict(get_social_bilibili_liveroom200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


