# FormatJsonTriviaOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.format_json_trivia_options_inner import FormatJsonTriviaOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FormatJsonTriviaOptionsInner from a JSON string
format_json_trivia_options_inner_instance = FormatJsonTriviaOptionsInner.from_json(json)
# print the JSON string representation of the object
print(FormatJsonTriviaOptionsInner.to_json())

# convert the object into a dict
format_json_trivia_options_inner_dict = format_json_trivia_options_inner_instance.to_dict()
# create an instance of FormatJsonTriviaOptionsInner from a dict
format_json_trivia_options_inner_from_dict = FormatJsonTriviaOptionsInner.from_dict(format_json_trivia_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


