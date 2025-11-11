# GetSaying200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 随机获取到的名言或诗词内容。 | [optional] 

## Example

```python
from uapi.models.get_saying200_response import GetSaying200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSaying200Response from a JSON string
get_saying200_response_instance = GetSaying200Response.from_json(json)
# print the JSON string representation of the object
print(GetSaying200Response.to_json())

# convert the object into a dict
get_saying200_response_dict = get_saying200_response_instance.to_dict()
# create an instance of GetSaying200Response from a dict
get_saying200_response_from_dict = GetSaying200Response.from_dict(get_saying200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


