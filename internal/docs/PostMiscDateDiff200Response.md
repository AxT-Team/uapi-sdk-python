# PostMiscDateDiff200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | 总天数 | [optional] 
**hours** | **int** | 总小时数 | [optional] 
**minutes** | **int** | 总分钟数 | [optional] 
**seconds** | **int** | 总秒数 | [optional] 
**weeks** | **int** | 总周数 | [optional] 
**human_readable** | **str** | 人性化显示格式 | [optional] 

## Example

```python
from uapi.models.post_misc_date_diff200_response import PostMiscDateDiff200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostMiscDateDiff200Response from a JSON string
post_misc_date_diff200_response_instance = PostMiscDateDiff200Response.from_json(json)
# print the JSON string representation of the object
print(PostMiscDateDiff200Response.to_json())

# convert the object into a dict
post_misc_date_diff200_response_dict = post_misc_date_diff200_response_instance.to_dict()
# create an instance of PostMiscDateDiff200Response from a dict
post_misc_date_diff200_response_from_dict = PostMiscDateDiff200Response.from_dict(post_misc_date_diff200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


