# GetDictionaryLookup200ResponseEntryPhonetics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uk** | [**GetDictionaryLookup200ResponseEntryPhoneticsUk**](GetDictionaryLookup200ResponseEntryPhoneticsUk.md) |  | [optional] 
**us** | [**GetDictionaryLookup200ResponseEntryPhoneticsUs**](GetDictionaryLookup200ResponseEntryPhoneticsUs.md) |  | [optional] 

## Example

```python
from uapi.models.get_dictionary_lookup200_response_entry_phonetics import GetDictionaryLookup200ResponseEntryPhonetics

# TODO update the JSON string below
json = "{}"
# create an instance of GetDictionaryLookup200ResponseEntryPhonetics from a JSON string
get_dictionary_lookup200_response_entry_phonetics_instance = GetDictionaryLookup200ResponseEntryPhonetics.from_json(json)
# print the JSON string representation of the object
print(GetDictionaryLookup200ResponseEntryPhonetics.to_json())

# convert the object into a dict
get_dictionary_lookup200_response_entry_phonetics_dict = get_dictionary_lookup200_response_entry_phonetics_instance.to_dict()
# create an instance of GetDictionaryLookup200ResponseEntryPhonetics from a dict
get_dictionary_lookup200_response_entry_phonetics_from_dict = GetDictionaryLookup200ResponseEntryPhonetics.from_dict(get_dictionary_lookup200_response_entry_phonetics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


