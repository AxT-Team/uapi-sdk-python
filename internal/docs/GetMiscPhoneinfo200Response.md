# GetMiscPhoneinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**sp** | **str** | 运营商 (Service Provider) 名称。 | [optional] 

## Example

```python
from uapi.models.get_misc_phoneinfo200_response import GetMiscPhoneinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscPhoneinfo200Response from a JSON string
get_misc_phoneinfo200_response_instance = GetMiscPhoneinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscPhoneinfo200Response.to_json())

# convert the object into a dict
get_misc_phoneinfo200_response_dict = get_misc_phoneinfo200_response_instance.to_dict()
# create an instance of GetMiscPhoneinfo200Response from a dict
get_misc_phoneinfo200_response_from_dict = GetMiscPhoneinfo200Response.from_dict(get_misc_phoneinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


