# GetNetworkUrlstatus200ResponseOneOf

当目标 URL 可访问时，`status` 为目标返回的 HTTP 状态码（如 `200`）。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | 目标URL实际返回的HTTP状态码。 | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_urlstatus200_response_one_of import GetNetworkUrlstatus200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkUrlstatus200ResponseOneOf from a JSON string
get_network_urlstatus200_response_one_of_instance = GetNetworkUrlstatus200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetNetworkUrlstatus200ResponseOneOf.to_json())

# convert the object into a dict
get_network_urlstatus200_response_one_of_dict = get_network_urlstatus200_response_one_of_instance.to_dict()
# create an instance of GetNetworkUrlstatus200ResponseOneOf from a dict
get_network_urlstatus200_response_one_of_from_dict = GetNetworkUrlstatus200ResponseOneOf.from_dict(get_network_urlstatus200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


