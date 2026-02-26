# GetMiscDistrict200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | 结果总数。 | [optional] 
**results** | [**List[GetMiscDistrict200ResponseResultsInner]**](GetMiscDistrict200ResponseResultsInner.md) | 结果列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_district200_response import GetMiscDistrict200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscDistrict200Response from a JSON string
get_misc_district200_response_instance = GetMiscDistrict200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscDistrict200Response.to_json())

# convert the object into a dict
get_misc_district200_response_dict = get_misc_district200_response_instance.to_dict()
# create an instance of GetMiscDistrict200Response from a dict
get_misc_district200_response_from_dict = GetMiscDistrict200Response.from_dict(get_misc_district200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


