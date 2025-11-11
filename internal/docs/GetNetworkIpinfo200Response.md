# GetNetworkIpinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **str** | 自治系统编号 (由GeoLite2或商业版提供) | [optional] 
**beginip** | **str** | IP范围起始 (仅在默认查询中提供) | [optional] 
**code** | **int** |  | [optional] 
**endip** | **str** | IP范围结束 (仅在默认查询中提供) | [optional] 
**ip** | **str** |  | [optional] 
**isp** | **str** | 运营商 | [optional] 
**latitude** | **float** |  | [optional] 
**llc** | **str** | 归属 | [optional] 
**longitude** | **float** |  | [optional] 
**region** | **str** | 格式：国家 省份 城市 | [optional] 
**district** | **str** | 行政区 (仅在商业查询中提供) | [optional] 
**area_code** | **str** | 行政区划代码 (仅在商业查询中提供) | [optional] 
**city_code** | **str** | 城市区号 (仅在商业查询中提供) | [optional] 
**zip_code** | **str** | 邮政编码 (仅在商业查询中提供) | [optional] 
**time_zone** | **str** | 时区 (仅在商业查询中提供) | [optional] 
**scenes** | **str** | 应用场景 (仅在商业查询中提供) | [optional] 
**elevation** | **str** | 海拔（米）(仅在商业查询中提供) | [optional] 
**weather_station** | **str** | 气象站代码 (仅在商业查询中提供) | [optional] 

## Example

```python
from uapi.models.get_network_ipinfo200_response import GetNetworkIpinfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkIpinfo200Response from a JSON string
get_network_ipinfo200_response_instance = GetNetworkIpinfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkIpinfo200Response.to_json())

# convert the object into a dict
get_network_ipinfo200_response_dict = get_network_ipinfo200_response_instance.to_dict()
# create an instance of GetNetworkIpinfo200Response from a dict
get_network_ipinfo200_response_from_dict = GetNetworkIpinfo200Response.from_dict(get_network_ipinfo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


