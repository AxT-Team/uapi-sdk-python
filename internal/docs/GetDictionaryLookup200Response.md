# GetDictionaryLookup200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**GetDictionaryLookup200ResponseEntry**](GetDictionaryLookup200ResponseEntry.md) |  | [optional] 
**found** | **bool** |  | [optional] 

## Example

```python
from uapi.models.get_dictionary_lookup200_response import GetDictionaryLookup200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictionaryLookup200Response from a JSON string
get_dictionary_lookup200_response_instance = GetDictionaryLookup200Response.from_json(json)
# print the JSON string representation of the object
print(GetDictionaryLookup200Response.to_json())

# convert the object into a dict
get_dictionary_lookup200_response_dict = get_dictionary_lookup200_response_instance.to_dict()
# create an instance of GetDictionaryLookup200Response from a dict
get_dictionary_lookup200_response_from_dict = GetDictionaryLookup200Response.from_dict(get_dictionary_lookup200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


