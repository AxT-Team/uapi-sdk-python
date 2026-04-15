# GetImageBingDailyHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** |  | [optional] 
**items** | [**List[GetImageBingDailyHistory200ResponseItemsInner]**](GetImageBingDailyHistory200ResponseItemsInner.md) |  | [optional] 
**pagination** | [**GetImageBingDailyHistory200ResponsePagination**](GetImageBingDailyHistory200ResponsePagination.md) |  | [optional] 

## Example

```python
from uapi.models.get_image_bing_daily_history200_response import GetImageBingDailyHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageBingDailyHistory200Response from a JSON string
get_image_bing_daily_history200_response_instance = GetImageBingDailyHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetImageBingDailyHistory200Response.to_json())

# convert the object into a dict
get_image_bing_daily_history200_response_dict = get_image_bing_daily_history200_response_instance.to_dict()
# create an instance of GetImageBingDailyHistory200Response from a dict
get_image_bing_daily_history200_response_from_dict = GetImageBingDailyHistory200Response.from_dict(get_image_bing_daily_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


