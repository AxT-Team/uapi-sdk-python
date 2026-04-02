# GetMiscTrackingCarriers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carriers** | [**List[GetMiscTrackingCarriers200ResponseCarriersInner]**](GetMiscTrackingCarriers200ResponseCarriersInner.md) | 快递公司列表 | [optional] 
**total** | **int** | 支持的快递公司总数 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_carriers200_response import GetMiscTrackingCarriers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingCarriers200Response from a JSON string
get_misc_tracking_carriers200_response_instance = GetMiscTrackingCarriers200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingCarriers200Response.to_json())

# convert the object into a dict
get_misc_tracking_carriers200_response_dict = get_misc_tracking_carriers200_response_instance.to_dict()
# create an instance of GetMiscTrackingCarriers200Response from a dict
get_misc_tracking_carriers200_response_from_dict = GetMiscTrackingCarriers200Response.from_dict(get_misc_tracking_carriers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


