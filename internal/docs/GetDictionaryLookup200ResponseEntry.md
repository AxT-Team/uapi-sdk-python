# GetDictionaryLookup200ResponseEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | [**List[GetDictionaryLookup200ResponseEntryDefinitionsInner]**](GetDictionaryLookup200ResponseEntryDefinitionsInner.md) |  | [optional] 
**english_definitions** | [**List[GetDictionaryLookup200ResponseEntryEnglishDefinitionsInner]**](GetDictionaryLookup200ResponseEntryEnglishDefinitionsInner.md) |  | [optional] 
**exam_tags** | **List[str]** |  | [optional] 
**examples** | [**List[GetDictionaryLookup200ResponseEntryExamplesInner]**](GetDictionaryLookup200ResponseEntryExamplesInner.md) |  | [optional] 
**language** | **str** |  | [optional] 
**phonetics** | [**GetDictionaryLookup200ResponseEntryPhonetics**](GetDictionaryLookup200ResponseEntryPhonetics.md) |  | [optional] 
**phrases** | [**List[GetDictionaryLookup200ResponseEntryPhrasesInner]**](GetDictionaryLookup200ResponseEntryPhrasesInner.md) |  | [optional] 
**synonyms** | [**List[GetDictionaryLookup200ResponseEntrySynonymsInner]**](GetDictionaryLookup200ResponseEntrySynonymsInner.md) |  | [optional] 
**word** | **str** |  | [optional] 
**word_forms** | [**List[GetDictionaryLookup200ResponseEntryWordFormsInner]**](GetDictionaryLookup200ResponseEntryWordFormsInner.md) |  | [optional] 

## Example

```python
from uapi.models.get_dictionary_lookup200_response_entry import GetDictionaryLookup200ResponseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictionaryLookup200ResponseEntry from a JSON string
get_dictionary_lookup200_response_entry_instance = GetDictionaryLookup200ResponseEntry.from_json(json)
# print the JSON string representation of the object
print(GetDictionaryLookup200ResponseEntry.to_json())

# convert the object into a dict
get_dictionary_lookup200_response_entry_dict = get_dictionary_lookup200_response_entry_instance.to_dict()
# create an instance of GetDictionaryLookup200ResponseEntry from a dict
get_dictionary_lookup200_response_entry_from_dict = GetDictionaryLookup200ResponseEntry.from_dict(get_dictionary_lookup200_response_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


