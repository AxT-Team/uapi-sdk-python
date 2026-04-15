# GetNetworkWhois200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whois** | **object** | 结构化 WHOIS 信息，返回经过解析的 JSON 对象，通常包含域名信息、注册商信息、注册人信息以及注册日期、更新时间、到期时间等字段。 有些字段会因域名注册局和隐私保护设置而有所不同噢。 | [optional] 

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


