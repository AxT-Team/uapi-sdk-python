# GetNetworkPingmyip200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_ip** | **str** | 当前客户端的公网 IP 地址。 | [optional] 
**ping_successful** | **bool** | 是否成功完成对当前客户端 IP 的 Ping。 | [optional] 
**message** | **str** | 操作结果说明。成功时通常会附带平均延迟信息。 | [optional] 

## Example

```python
from uapi.models.get_network_pingmyip200_response import GetNetworkPingmyip200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkPingmyip200Response from a JSON string
get_network_pingmyip200_response_instance = GetNetworkPingmyip200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkPingmyip200Response.to_json())

# convert the object into a dict
get_network_pingmyip200_response_dict = get_network_pingmyip200_response_instance.to_dict()
# create an instance of GetNetworkPingmyip200Response from a dict
get_network_pingmyip200_response_from_dict = GetNetworkPingmyip200Response.from_dict(get_network_pingmyip200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


