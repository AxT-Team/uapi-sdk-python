# FormatJsonTrivia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**options** | [**List[FormatJsonTriviaOptionsInner]**](FormatJsonTriviaOptionsInner.md) |  | [optional] 

## Example

```python
from uapi.models.format_json_trivia import FormatJsonTrivia

# TODO update the JSON string below
json = "{}"
# create an instance of FormatJsonTrivia from a JSON string
format_json_trivia_instance = FormatJsonTrivia.from_json(json)
# print the JSON string representation of the object
print(FormatJsonTrivia.to_json())

# convert the object into a dict
format_json_trivia_dict = format_json_trivia_instance.to_dict()
# create an instance of FormatJsonTrivia from a dict
format_json_trivia_from_dict = FormatJsonTrivia.from_dict(format_json_trivia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


