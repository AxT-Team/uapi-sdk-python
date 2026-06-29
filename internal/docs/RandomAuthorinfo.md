# RandomAuthorinfo

作者扩展信息，部分语料返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bio** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from uapi.models.random_authorinfo import RandomAuthorinfo

# TODO update the JSON string below
json = "{}"
# create an instance of RandomAuthorinfo from a JSON string
random_authorinfo_instance = RandomAuthorinfo.from_json(json)
# print the JSON string representation of the object
print(RandomAuthorinfo.to_json())

# convert the object into a dict
random_authorinfo_dict = random_authorinfo_instance.to_dict()
# create an instance of RandomAuthorinfo from a dict
random_authorinfo_from_dict = RandomAuthorinfo.from_dict(random_authorinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


