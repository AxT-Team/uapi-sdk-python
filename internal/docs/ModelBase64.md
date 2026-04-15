# ModelBase64


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.model_base64 import ModelBase64

# TODO update the JSON string below
json = "{}"
# create an instance of ModelBase64 from a JSON string
model_base64_instance = ModelBase64.from_json(json)
# print the JSON string representation of the object
print(ModelBase64.to_json())

# convert the object into a dict
model_base64_dict = model_base64_instance.to_dict()
# create an instance of ModelBase64 from a dict
model_base64_from_dict = ModelBase64.from_dict(model_base64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


