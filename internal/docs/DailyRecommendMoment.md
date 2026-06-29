# DailyRecommendMoment

包装对象。外层字段随 mode 不同而不同，语录本体统一放在 item 中。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_time** | **str** | 仅 moment 模式返回，服务器当前时间，ISO 8601 格式。 | [optional] 
**var_date** | **str** | 仅 daily 模式返回，对应日期，格式 YYYY-MM-DD。 | [optional] 
**item** | [**DailyRecommendMomentItem**](DailyRecommendMomentItem.md) |  | [optional] 
**mode** | **str** | 当前运行模式。 | [optional] 
**scene** | [**DailyRecommendMomentScene**](DailyRecommendMomentScene.md) |  | [optional] 
**seed** | **str** | 当次结果的确定性种子。 | [optional] 
**time_segment** | **str** | 仅 moment 模式返回，命中的时段标识。 | [optional] 

## Example

```python
from uapi.models.daily_recommend_moment import DailyRecommendMoment

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRecommendMoment from a JSON string
daily_recommend_moment_instance = DailyRecommendMoment.from_json(json)
# print the JSON string representation of the object
print(DailyRecommendMoment.to_json())

# convert the object into a dict
daily_recommend_moment_dict = daily_recommend_moment_instance.to_dict()
# create an instance of DailyRecommendMoment from a dict
daily_recommend_moment_from_dict = DailyRecommendMoment.from_dict(daily_recommend_moment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


