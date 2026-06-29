# GetDictionaryLookup200ResponseEntrySynonymsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meaning** | **str** |  | [optional] 
**part_of_speech** | **str** |  | [optional] 
**words** | **List[str]** |  | [optional] 

## Example

```python
from uapi.models.get_dictionary_lookup200_response_entry_synonyms_inner import GetDictionaryLookup200ResponseEntrySynonymsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictionaryLookup200ResponseEntrySynonymsInner from a JSON string
get_dictionary_lookup200_response_entry_synonyms_inner_instance = GetDictionaryLookup200ResponseEntrySynonymsInner.from_json(json)
# print the JSON string representation of the object
print(GetDictionaryLookup200ResponseEntrySynonymsInner.to_json())

# convert the object into a dict
get_dictionary_lookup200_response_entry_synonyms_inner_dict = get_dictionary_lookup200_response_entry_synonyms_inner_instance.to_dict()
# create an instance of GetDictionaryLookup200ResponseEntrySynonymsInner from a dict
get_dictionary_lookup200_response_entry_synonyms_inner_from_dict = GetDictionaryLookup200ResponseEntrySynonymsInner.from_dict(get_dictionary_lookup200_response_entry_synonyms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


