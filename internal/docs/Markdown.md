# Markdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.markdown import Markdown

# TODO update the JSON string below
json = "{}"
# create an instance of Markdown from a JSON string
markdown_instance = Markdown.from_json(json)
# print the JSON string representation of the object
print(Markdown.to_json())

# convert the object into a dict
markdown_dict = markdown_instance.to_dict()
# create an instance of Markdown from a dict
markdown_from_dict = Markdown.from_dict(markdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


