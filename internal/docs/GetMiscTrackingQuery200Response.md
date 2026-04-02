# GetMiscTrackingQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | 快递单号 | [optional] 
**carrier_code** | **str** | 快递公司编码 | [optional] 
**carrier_name** | **str** | 快递公司名称 | [optional] 
**track_count** | **int** | 物流轨迹数量 | [optional] 
**tracks** | [**List[GetMiscTrackingQuery200ResponseTracksInner]**](GetMiscTrackingQuery200ResponseTracksInner.md) | 物流轨迹列表，按时间倒序排列 | [optional] 

## Example

```python
from uapi.models.get_misc_tracking_query200_response import GetMiscTrackingQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscTrackingQuery200Response from a JSON string
get_misc_tracking_query200_response_instance = GetMiscTrackingQuery200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscTrackingQuery200Response.to_json())

# convert the object into a dict
get_misc_tracking_query200_response_dict = get_misc_tracking_query200_response_instance.to_dict()
# create an instance of GetMiscTrackingQuery200Response from a dict
get_misc_tracking_query200_response_from_dict = GetMiscTrackingQuery200Response.from_dict(get_misc_tracking_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


