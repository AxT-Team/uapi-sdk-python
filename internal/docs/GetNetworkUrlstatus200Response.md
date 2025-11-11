# GetNetworkUrlstatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**status** | **int** | HTTP响应状态码 | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_network_urlstatus200_response import GetNetworkUrlstatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkUrlstatus200Response from a JSON string
get_network_urlstatus200_response_instance = GetNetworkUrlstatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkUrlstatus200Response.to_json())

# convert the object into a dict
get_network_urlstatus200_response_dict = get_network_urlstatus200_response_instance.to_dict()
# create an instance of GetNetworkUrlstatus200Response from a dict
get_network_urlstatus200_response_from_dict = GetNetworkUrlstatus200Response.from_dict(get_network_urlstatus200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


