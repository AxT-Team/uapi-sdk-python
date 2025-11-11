# GetMiscRandomnumber200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **List[float]** | 生成的随机数列表。 | [optional] 

## Example

```python
from uapi.models.get_misc_randomnumber200_response import GetMiscRandomnumber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscRandomnumber200Response from a JSON string
get_misc_randomnumber200_response_instance = GetMiscRandomnumber200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscRandomnumber200Response.to_json())

# convert the object into a dict
get_misc_randomnumber200_response_dict = get_misc_randomnumber200_response_instance.to_dict()
# create an instance of GetMiscRandomnumber200Response from a dict
get_misc_randomnumber200_response_from_dict = GetMiscRandomnumber200Response.from_dict(get_misc_randomnumber200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


