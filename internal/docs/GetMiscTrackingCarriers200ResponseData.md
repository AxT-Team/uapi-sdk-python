# GetMiscTrackingCarriers200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | 支持的快递公司总数 | [optional] 
**carriers** | [**List[GetMiscTrackingCarriers200ResponseDataCarriersInner]**](GetMiscTrackingCarriers200ResponseDataCarriersInner.md) | 快递公司列表 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_carriers200_response_data import GetMiscTrackingCarriers200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingCarriers200ResponseData from a JSON string
get_misc_tracking_carriers200_response_data_instance = GetMiscTrackingCarriers200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingCarriers200ResponseData.to_json())

# convert the object into a dict
get_misc_tracking_carriers200_response_data_dict = get_misc_tracking_carriers200_response_data_instance.to_dict()
# create an instance of GetMiscTrackingCarriers200ResponseData from a dict
get_misc_tracking_carriers200_response_data_from_dict = GetMiscTrackingCarriers200ResponseData.from_dict(get_misc_tracking_carriers200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


