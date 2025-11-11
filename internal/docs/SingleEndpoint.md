# SingleEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from uapi.models.single_endpoint import SingleEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of SingleEndpoint from a JSON string
single_endpoint_instance = SingleEndpoint.from_json(json)
# print the JSON string representation of the object
print(SingleEndpoint.to_json())

# convert the object into a dict
single_endpoint_dict = single_endpoint_instance.to_dict()
# create an instance of SingleEndpoint from a dict
single_endpoint_from_dict = SingleEndpoint.from_dict(single_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


