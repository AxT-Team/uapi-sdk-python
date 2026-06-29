# GetMiscTrackingQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | 快递公司编码 | [optional] 
**carrier_name** | **str** | 快递公司名称 | [optional] 
**completed_at** | **str** | 完成时间。仅已完成时返回签收或妥投对应的轨迹时间；未完成时为空字符串。 | [optional] 
**is_completed** | **bool** | 快递是否已完成。仅当状态识别为已签收/已妥投/已完成时为 true。 | [optional] 
**status** | **str** | 快递状态中文名称，例如：待揽收、已揽收、运输中、派送中、已完成、异常、未知。 | [optional] 
**status_code** | **str** | 快递状态编码。可能值：pending、picked_up、in_transit、out_for_delivery、delivered、exception、unknown。 | [optional] 
**track_count** | **int** | 物流轨迹数量 | [optional] 
**tracking_number** | **str** | 快递单号 | [optional] 
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


