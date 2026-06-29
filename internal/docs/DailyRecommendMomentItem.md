# DailyRecommendMomentItem

语录本体。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | 作者或说话者。 | [optional] 
**authorinfo** | [**RandomAuthorinfo**](RandomAuthorinfo.md) |  | [optional] 
**category** | **str** | 语录分类。 | [optional] 
**content** | **str** | 语录正文。 | [optional] 
**content_length** | **int** | 正文字数。 | [optional] 
**corpus** | **str** | 所属语料库标识。 | [optional] 
**created_at** | **str** | 语料入库时间戳（秒），部分语料返回。 | [optional] 
**matched_tags** | **List[str]** | 命中的标签，部分模式返回。 | [optional] 
**source** | **str** | 语录出处或来源。 | [optional] 
**uuid** | **str** | 语录唯一标识。 | [optional] 

## Example

```python
from uapi.models.daily_recommend_moment_item import DailyRecommendMomentItem

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRecommendMomentItem from a JSON string
daily_recommend_moment_item_instance = DailyRecommendMomentItem.from_json(json)
# print the JSON string representation of the object
print(DailyRecommendMomentItem.to_json())

# convert the object into a dict
daily_recommend_moment_item_dict = daily_recommend_moment_item_instance.to_dict()
# create an instance of DailyRecommendMomentItem from a dict
daily_recommend_moment_item_from_dict = DailyRecommendMomentItem.from_dict(daily_recommend_moment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


