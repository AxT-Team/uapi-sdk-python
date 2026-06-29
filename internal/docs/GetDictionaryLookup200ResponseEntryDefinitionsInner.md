# GetDictionaryLookup200ResponseEntryDefinitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meaning** | **str** |  | [optional] 
**part_of_speech** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_dictionary_lookup200_response_entry_definitions_inner import GetDictionaryLookup200ResponseEntryDefinitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictionaryLookup200ResponseEntryDefinitionsInner from a JSON string
get_dictionary_lookup200_response_entry_definitions_inner_instance = GetDictionaryLookup200ResponseEntryDefinitionsInner.from_json(json)
# print the JSON string representation of the object
print(GetDictionaryLookup200ResponseEntryDefinitionsInner.to_json())

# convert the object into a dict
get_dictionary_lookup200_response_entry_definitions_inner_dict = get_dictionary_lookup200_response_entry_definitions_inner_instance.to_dict()
# create an instance of GetDictionaryLookup200ResponseEntryDefinitionsInner from a dict
get_dictionary_lookup200_response_entry_definitions_inner_from_dict = GetDictionaryLookup200ResponseEntryDefinitionsInner.from_dict(get_dictionary_lookup200_response_entry_definitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


