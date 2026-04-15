# FormatJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**market** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**headline** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**copyright** | **str** |  | [optional] 
**copyright_link** | **str** |  | [optional] 
**quiz_id** | **str** |  | [optional] 
**trivia** | [**FormatJsonTrivia**](FormatJsonTrivia.md) |  | [optional] 
**resolution** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**image_url_4k** | **str** |  | [optional] 
**image_url_1080** | **str** |  | [optional] 
**fetched_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from uapi.models.format_json import FormatJson

# TODO update the JSON string below
json = "{}"
# create an instance of FormatJson from a JSON string
format_json_instance = FormatJson.from_json(json)
# print the JSON string representation of the object
print(FormatJson.to_json())

# convert the object into a dict
format_json_dict = format_json_instance.to_dict()
# create an instance of FormatJson from a dict
format_json_from_dict = FormatJson.from_dict(format_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


