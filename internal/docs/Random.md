# Random


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
from uapi.models.random import Random

# TODO update the JSON string below
json = "{}"
# create an instance of Random from a JSON string
random_instance = Random.from_json(json)
# print the JSON string representation of the object
print(Random.to_json())

# convert the object into a dict
random_dict = random_instance.to_dict()
# create an instance of Random from a dict
random_from_dict = Random.from_dict(random_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


