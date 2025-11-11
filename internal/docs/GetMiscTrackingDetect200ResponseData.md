# GetMiscTrackingDetect200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | 查询的快递单号 | [optional] 
**carrier_code** | **str** | 最可能的快递公司编码 | [optional] 
**carrier_name** | **str** | 最可能的快递公司名称 | [optional] 
**alternatives** | [**List[GetMiscTrackingDetect200ResponseDataAlternativesInner]**](GetMiscTrackingDetect200ResponseDataAlternativesInner.md) | 其他可能的快递公司列表（如果存在） | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_detect200_response_data import GetMiscTrackingDetect200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingDetect200ResponseData from a JSON string
get_misc_tracking_detect200_response_data_instance = GetMiscTrackingDetect200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingDetect200ResponseData.to_json())

# convert the object into a dict
get_misc_tracking_detect200_response_data_dict = get_misc_tracking_detect200_response_data_instance.to_dict()
# create an instance of GetMiscTrackingDetect200ResponseData from a dict
get_misc_tracking_detect200_response_data_from_dict = GetMiscTrackingDetect200ResponseData.from_dict(get_misc_tracking_detect200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


