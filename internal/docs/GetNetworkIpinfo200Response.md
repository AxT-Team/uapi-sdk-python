# GetNetworkIpinfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | 查询的IP地址 | [optional] 
**region** | **str** | 地理位置，格式：国家 省份 城市 | [optional] 
**isp** | **str** | 运营商名称 | [optional] 
**llc** | **str** | 归属机构 | [optional] 
**asn** | **str** | 自治系统编号 | [optional] 
**latitude** | **float** | 纬度 | [optional] 
**longitude** | **float** | 经度 | [optional] 
**beginip** | **str** | IP段起始地址（标准查询） | [optional] 
**endip** | **str** | IP段结束地址（标准查询） | [optional] 
**district** | **str** | 行政区（商业查询） | [optional] 

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


