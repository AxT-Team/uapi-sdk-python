# GetNetworkUrlstatus200ResponseOneOf1

当目标 URL 不可达或请求失败（如 DNS 失败、超时、连接失败）时，`status` 为 `0`。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | 目标不可达或请求失败时固定为 0。 | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_urlstatus200_response_one_of1 import GetNetworkUrlstatus200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkUrlstatus200ResponseOneOf1 from a JSON string
get_network_urlstatus200_response_one_of1_instance = GetNetworkUrlstatus200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(GetNetworkUrlstatus200ResponseOneOf1.to_json())

# convert the object into a dict
get_network_urlstatus200_response_one_of1_dict = get_network_urlstatus200_response_one_of1_instance.to_dict()
# create an instance of GetNetworkUrlstatus200ResponseOneOf1 from a dict
get_network_urlstatus200_response_one_of1_from_dict = GetNetworkUrlstatus200ResponseOneOf1.from_dict(get_network_urlstatus200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


