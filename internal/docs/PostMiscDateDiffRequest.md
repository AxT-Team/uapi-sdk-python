# PostMiscDateDiffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | 开始日期，支持多种格式自动识别 | 
**end_date** | **str** | 结束日期，支持多种格式自动识别 | 
**format** | **str** | 日期格式（可选），如DD-MM-YYYY。不指定则自动识别 | [optional] 

## Example

```python
from uapi.models.post_misc_date_diff_request import PostMiscDateDiffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMiscDateDiffRequest from a JSON string
post_misc_date_diff_request_instance = PostMiscDateDiffRequest.from_json(json)
# print the JSON string representation of the object
print(PostMiscDateDiffRequest.to_json())

# convert the object into a dict
post_misc_date_diff_request_dict = post_misc_date_diff_request_instance.to_dict()
# create an instance of PostMiscDateDiffRequest from a dict
post_misc_date_diff_request_from_dict = PostMiscDateDiffRequest.from_dict(post_misc_date_diff_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


