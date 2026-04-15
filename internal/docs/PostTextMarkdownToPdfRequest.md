# PostTextMarkdownToPdfRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 原始 Markdown 字符串，最大不超过 1MB。 | 
**theme** | **str** | PDF 的排版主题。可选 &#x60;github&#x60;、&#x60;minimal&#x60;、&#x60;light&#x60;、&#x60;dark&#x60;，默认是 &#x60;github&#x60;。 | [optional] [default to 'github']
**paper_size** | **str** | PDF 的纸张大小。可选 &#x60;A4&#x60; 或 &#x60;Letter&#x60;，默认是 &#x60;A4&#x60;。 | [optional] [default to 'A4']

## Example

```python
from uapi.models.post_text_markdown_to_pdf_request import PostTextMarkdownToPdfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTextMarkdownToPdfRequest from a JSON string
post_text_markdown_to_pdf_request_instance = PostTextMarkdownToPdfRequest.from_json(json)
# print the JSON string representation of the object
print(PostTextMarkdownToPdfRequest.to_json())

# convert the object into a dict
post_text_markdown_to_pdf_request_dict = post_text_markdown_to_pdf_request_instance.to_dict()
# create an instance of PostTextMarkdownToPdfRequest from a dict
post_text_markdown_to_pdf_request_from_dict = PostTextMarkdownToPdfRequest.from_dict(post_text_markdown_to_pdf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


