# GetNetworkIcp200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**msg** | **str** |  | [optional] 
**nature_name** | **str** | 主办单位的性质 (企业/个人) | [optional] 
**service_licence** | **str** | ICP备案号 | [optional] 
**unit_name** | **str** | 主办单位名称 | [optional] 

## Example

```python
from uapi.models.get_network_icp200_response import GetNetworkIcp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkIcp200Response from a JSON string
get_network_icp200_response_instance = GetNetworkIcp200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkIcp200Response.to_json())

# convert the object into a dict
get_network_icp200_response_dict = get_network_icp200_response_instance.to_dict()
# create an instance of GetNetworkIcp200Response from a dict
get_network_icp200_response_from_dict = GetNetworkIcp200Response.from_dict(get_network_icp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


