# GetGameEpicFree200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 游戏的唯一标识ID。 | [optional] 
**title** | **str** | 游戏的完整标题名称。 | [optional] 
**cover** | **str** | 游戏封面图片的URL地址。 | [optional] 
**original_price** | **float** | 游戏的原价，单位为人民币元。 | [optional] 
**original_price_desc** | **str** | 格式化后的原价描述字符串。 | [optional] 
**description** | **str** | 游戏的简介描述。 | [optional] 
**seller** | **str** | 游戏的发行商或销售商。 | [optional] 
**is_free_now** | **bool** | 当前是否处于免费状态。 | [optional] 
**free_start** | **str** | 免费开始时间的可读字符串格式。 | [optional] 
**free_start_at** | **int** | 免费开始时间的13位毫秒时间戳。 | [optional] 
**free_end** | **str** | 免费结束时间的可读字符串格式。 | [optional] 
**free_end_at** | **int** | 免费结束时间的13位毫秒时间戳。 | [optional] 
**link** | **str** | 游戏在Epic Games商店的详情页链接。 | [optional] 

## Example

```python
from uapi.models.get_game_epic_free200_response_data_inner import GetGameEpicFree200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameEpicFree200ResponseDataInner from a JSON string
get_game_epic_free200_response_data_inner_instance = GetGameEpicFree200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGameEpicFree200ResponseDataInner.to_json())

# convert the object into a dict
get_game_epic_free200_response_data_inner_dict = get_game_epic_free200_response_data_inner_instance.to_dict()
# create an instance of GetGameEpicFree200ResponseDataInner from a dict
get_game_epic_free200_response_data_inner_from_dict = GetGameEpicFree200ResponseDataInner.from_dict(get_game_epic_free200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


