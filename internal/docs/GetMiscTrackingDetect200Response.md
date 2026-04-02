# GetMiscTrackingDetect200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | 查询的快递单号 | [optional] 
**carrier_code** | **str** | 识别出的快递公司编码 | [optional] 
**carrier_name** | **str** | 识别出的快递公司名称 | [optional] 
**alternatives** | [**List[GetMiscTrackingDetect200ResponseAlternativesInner]**](GetMiscTrackingDetect200ResponseAlternativesInner.md) | 其他可能的快递公司列表。如果没有备选项，会返回空数组。 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_detect200_response import GetMiscTrackingDetect200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingDetect200Response from a JSON string
get_misc_tracking_detect200_response_instance = GetMiscTrackingDetect200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingDetect200Response.to_json())

# convert the object into a dict
get_misc_tracking_detect200_response_dict = get_misc_tracking_detect200_response_instance.to_dict()
# create an instance of GetMiscTrackingDetect200Response from a dict
get_misc_tracking_detect200_response_from_dict = GetMiscTrackingDetect200Response.from_dict(get_misc_tracking_detect200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


