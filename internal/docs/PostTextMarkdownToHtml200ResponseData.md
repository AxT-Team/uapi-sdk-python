# PostTextMarkdownToHtml200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | 转换后的 HTML 字符串，内容是带样式的 HTML 片段。 | [optional] 

## Example

```python
from uapi.models.post_text_markdown_to_html200_response_data import PostTextMarkdownToHtml200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextMarkdownToHtml200ResponseData from a JSON string
post_text_markdown_to_html200_response_data_instance = PostTextMarkdownToHtml200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PostTextMarkdownToHtml200ResponseData.to_json())

# convert the object into a dict
post_text_markdown_to_html200_response_data_dict = post_text_markdown_to_html200_response_data_instance.to_dict()
# create an instance of PostTextMarkdownToHtml200ResponseData from a dict
post_text_markdown_to_html200_response_data_from_dict = PostTextMarkdownToHtml200ResponseData.from_dict(post_text_markdown_to_html200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


