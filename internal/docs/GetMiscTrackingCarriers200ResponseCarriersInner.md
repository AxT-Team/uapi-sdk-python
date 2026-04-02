# GetMiscTrackingCarriers200ResponseCarriersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 快递公司编码，用于 API 调用时的 carrier_code 参数 | [optional] 
**name** | **str** | 快递公司中文名称，用于界面显示 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_carriers200_response_carriers_inner import GetMiscTrackingCarriers200ResponseCarriersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingCarriers200ResponseCarriersInner from a JSON string
get_misc_tracking_carriers200_response_carriers_inner_instance = GetMiscTrackingCarriers200ResponseCarriersInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingCarriers200ResponseCarriersInner.to_json())

# convert the object into a dict
get_misc_tracking_carriers200_response_carriers_inner_dict = get_misc_tracking_carriers200_response_carriers_inner_instance.to_dict()
# create an instance of GetMiscTrackingCarriers200ResponseCarriersInner from a dict
get_misc_tracking_carriers200_response_carriers_inner_from_dict = GetMiscTrackingCarriers200ResponseCarriersInner.from_dict(get_misc_tracking_carriers200_response_carriers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


