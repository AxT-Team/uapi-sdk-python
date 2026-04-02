# GetSocialBilibiliVideoinfo200ResponseDescV2Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_text** | **str** | 简介文本。 | [optional] 
**type** | **float** | 片段类型。 | [optional] 
**biz_id** | **float** | 业务 ID，被关联对象的 ID。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_desc_v2_inner import GetSocialBilibiliVideoinfo200ResponseDescV2Inner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseDescV2Inner from a JSON string
get_social_bilibili_videoinfo200_response_desc_v2_inner_instance = GetSocialBilibiliVideoinfo200ResponseDescV2Inner.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseDescV2Inner.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_desc_v2_inner_dict = get_social_bilibili_videoinfo200_response_desc_v2_inner_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseDescV2Inner from a dict
get_social_bilibili_videoinfo200_response_desc_v2_inner_from_dict = GetSocialBilibiliVideoinfo200ResponseDescV2Inner.from_dict(get_social_bilibili_videoinfo200_response_desc_v2_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


