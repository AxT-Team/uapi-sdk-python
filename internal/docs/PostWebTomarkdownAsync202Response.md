# PostWebTomarkdownAsync202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | 任务唯一标识符 | [optional] 
**status** | **str** | 任务状态 | [optional] 
**url** | **str** | 要转换的URL | [optional] 
**created_at** | **str** | 任务创建时间（ISO 8601格式） | [optional] 
**message** | **str** | 提示信息 | [optional] 

## Example

```python
from uapi.models.post_web_tomarkdown_async202_response import PostWebTomarkdownAsync202Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebTomarkdownAsync202Response from a JSON string
post_web_tomarkdown_async202_response_instance = PostWebTomarkdownAsync202Response.from_json(json)
# print the JSON string representation of the object
print(PostWebTomarkdownAsync202Response.to_json())

# convert the object into a dict
post_web_tomarkdown_async202_response_dict = post_web_tomarkdown_async202_response_instance.to_dict()
# create an instance of PostWebTomarkdownAsync202Response from a dict
post_web_tomarkdown_async202_response_from_dict = PostWebTomarkdownAsync202Response.from_dict(post_web_tomarkdown_async202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


