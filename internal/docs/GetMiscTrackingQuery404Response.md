# GetMiscTrackingQuery404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_query404_response import GetMiscTrackingQuery404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingQuery404Response from a JSON string
get_misc_tracking_query404_response_instance = GetMiscTrackingQuery404Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingQuery404Response.to_json())

# convert the object into a dict
get_misc_tracking_query404_response_dict = get_misc_tracking_query404_response_instance.to_dict()
# create an instance of GetMiscTrackingQuery404Response from a dict
get_misc_tracking_query404_response_from_dict = GetMiscTrackingQuery404Response.from_dict(get_misc_tracking_query404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


