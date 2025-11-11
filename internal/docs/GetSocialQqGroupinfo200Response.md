# GetSocialQqGroupinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | 群号 | [optional] 
**group_name** | **str** | 群名称 | [optional] 
**avatar_url** | **str** | 群头像URL（标准尺寸100x100） | [optional] 
**description** | **str** | 群描述/简介 | [optional] 
**tag** | **str** | 群标签 | [optional] 
**join_url** | **str** | 加群链接（QR码URL） | [optional] 
**last_updated** | **str** | 最后更新时间（ISO 8601格式） | [optional] 

## Example

```python
from uapi.models.get_social_qq_groupinfo200_response import GetSocialQqGroupinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialQqGroupinfo200Response from a JSON string
get_social_qq_groupinfo200_response_instance = GetSocialQqGroupinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetSocialQqGroupinfo200Response.to_json())

# convert the object into a dict
get_social_qq_groupinfo200_response_dict = get_social_qq_groupinfo200_response_instance.to_dict()
# create an instance of GetSocialQqGroupinfo200Response from a dict
get_social_qq_groupinfo200_response_from_dict = GetSocialQqGroupinfo200Response.from_dict(get_social_qq_groupinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


