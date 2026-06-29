# GetSayingRandom200Response


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
**current_time** | **str** | 仅 moment 模式返回，服务器当前时间，ISO 8601 格式。 | [optional] 
**var_date** | **str** | 仅 daily 模式返回，对应日期，格式 YYYY-MM-DD。 | [optional] 
**item** | [**DailyRecommendMomentItem**](DailyRecommendMomentItem.md) |  | [optional] 
**mode** | **str** | 当前运行模式。 | [optional] 
**scene** | [**DailyRecommendMomentScene**](DailyRecommendMomentScene.md) |  | [optional] 
**seed** | **str** | 当次结果的确定性种子。 | [optional] 
**time_segment** | **str** | 仅 moment 模式返回，命中的时段标识。 | [optional] 

## Example

```python
from uapi.models.get_saying_random200_response import GetSayingRandom200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSayingRandom200Response from a JSON string
get_saying_random200_response_instance = GetSayingRandom200Response.from_json(json)
# print the JSON string representation of the object
print(GetSayingRandom200Response.to_json())

# convert the object into a dict
get_saying_random200_response_dict = get_saying_random200_response_instance.to_dict()
# create an instance of GetSayingRandom200Response from a dict
get_saying_random200_response_from_dict = GetSayingRandom200Response.from_dict(get_saying_random200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


