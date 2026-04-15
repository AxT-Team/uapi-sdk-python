# GetImageBingDailyHistory200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**market** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**headline** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**copyright** | **str** |  | [optional] 
**copyright_link** | **str** |  | [optional] 
**quiz_id** | **str** |  | [optional] 
**trivia** | [**FormatJsonTrivia**](FormatJsonTrivia.md) |  | [optional] 
**resolution** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**image_url_4k** | **str** |  | [optional] 
**image_url_1080** | **str** |  | [optional] 
**fetched_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_image_bing_daily_history200_response_items_inner import GetImageBingDailyHistory200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetImageBingDailyHistory200ResponseItemsInner from a JSON string
get_image_bing_daily_history200_response_items_inner_instance = GetImageBingDailyHistory200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(GetImageBingDailyHistory200ResponseItemsInner.to_json())

# convert the object into a dict
get_image_bing_daily_history200_response_items_inner_dict = get_image_bing_daily_history200_response_items_inner_instance.to_dict()
# create an instance of GetImageBingDailyHistory200ResponseItemsInner from a dict
get_image_bing_daily_history200_response_items_inner_from_dict = GetImageBingDailyHistory200ResponseItemsInner.from_dict(get_image_bing_daily_history200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


