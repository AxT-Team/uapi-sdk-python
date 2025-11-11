# GetMiscTrackingCarriers200ResponseDataCarriersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 快递公司编码，用于API调用时的carrier_code参数 | [optional] 
**name** | **str** | 快递公司中文名称，用于界面显示 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_carriers200_response_data_carriers_inner import GetMiscTrackingCarriers200ResponseDataCarriersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingCarriers200ResponseDataCarriersInner from a JSON string
get_misc_tracking_carriers200_response_data_carriers_inner_instance = GetMiscTrackingCarriers200ResponseDataCarriersInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingCarriers200ResponseDataCarriersInner.to_json())

# convert the object into a dict
get_misc_tracking_carriers200_response_data_carriers_inner_dict = get_misc_tracking_carriers200_response_data_carriers_inner_instance.to_dict()
# create an instance of GetMiscTrackingCarriers200ResponseDataCarriersInner from a dict
get_misc_tracking_carriers200_response_data_carriers_inner_from_dict = GetMiscTrackingCarriers200ResponseDataCarriersInner.from_dict(get_misc_tracking_carriers200_response_data_carriers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


