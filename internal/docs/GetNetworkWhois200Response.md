# GetNetworkWhois200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**whois** | **object** | ### 结构化WHOIS信息  返回经过解析的JSON对象，包含以下主要部分：  - **域名信息**: 包含域名ID、注册状态、DNS服务器等 - **注册商信息**: 注册服务商的详细信息 - **注册人信息**: 域名所有者的相关信息（可能因隐私保护而部分隐藏） - **重要日期**: 包括注册日期、更新日期和到期日期 | [optional] 

## Example

```python
from uapi.models.get_network_whois200_response import GetNetworkWhois200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkWhois200Response from a JSON string
get_network_whois200_response_instance = GetNetworkWhois200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkWhois200Response.to_json())

# convert the object into a dict
get_network_whois200_response_dict = get_network_whois200_response_instance.to_dict()
# create an instance of GetNetworkWhois200Response from a dict
get_network_whois200_response_from_dict = GetNetworkWhois200Response.from_dict(get_network_whois200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


