# PostTextMarkdownToHtmlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 原始 Markdown 字符串，最大不超过 1MB。 | 
**format** | **str** | 响应格式。传 &#x60;json&#x60; 时返回 JSON 包裹的 HTML 片段；传 &#x60;html&#x60; 时直接返回 &#x60;text/html&#x60;，并且响应内容会自动带完整的网页结构，适合浏览器预览或直接保存为网页文件。默认是 &#x60;json&#x60;。 | [optional] [default to 'json']
**sanitize** | **bool** | 是否开启安全模式，过滤掉用户输入中的风险脚本。默认是 &#x60;true&#x60;。 | [optional] [default to True]

## Example

```python
from uapi.models.post_text_markdown_to_html_request import PostTextMarkdownToHtmlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextMarkdownToHtmlRequest from a JSON string
post_text_markdown_to_html_request_instance = PostTextMarkdownToHtmlRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextMarkdownToHtmlRequest.to_json())

# convert the object into a dict
post_text_markdown_to_html_request_dict = post_text_markdown_to_html_request_instance.to_dict()
# create an instance of PostTextMarkdownToHtmlRequest from a dict
post_text_markdown_to_html_request_from_dict = PostTextMarkdownToHtmlRequest.from_dict(post_text_markdown_to_html_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


