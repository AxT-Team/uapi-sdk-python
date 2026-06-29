# DailyRecommendMomentScene

仅 recommend 模式返回，命中的场景画像。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from uapi.models.daily_recommend_moment_scene import DailyRecommendMomentScene

# TODO update the JSON string below
json = "{}"
# create an instance of DailyRecommendMomentScene from a JSON string
daily_recommend_moment_scene_instance = DailyRecommendMomentScene.from_json(json)
# print the JSON string representation of the object
print(DailyRecommendMomentScene.to_json())

# convert the object into a dict
daily_recommend_moment_scene_dict = daily_recommend_moment_scene_instance.to_dict()
# create an instance of DailyRecommendMomentScene from a dict
daily_recommend_moment_scene_from_dict = DailyRecommendMomentScene.from_dict(daily_recommend_moment_scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


