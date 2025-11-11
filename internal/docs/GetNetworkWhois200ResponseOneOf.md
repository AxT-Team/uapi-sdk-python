# GetNetworkWhois200ResponseOneOf

### 文本格式响应 当 `format=text` 或未指定时，`whois` 字段包含原始的WHOIS查询文本。这保留了最完整的信息，适合需要自行解析或展示原始数据的场景。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**whois** | **str** | **WHOIS原始文本**  返回未经处理的原始WHOIS查询结果文本。 | [optional] 

## Example

```python
from uapi.models.get_network_whois200_response_one_of import GetNetworkWhois200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkWhois200ResponseOneOf from a JSON string
get_network_whois200_response_one_of_instance = GetNetworkWhois200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetNetworkWhois200ResponseOneOf.to_json())

# convert the object into a dict
get_network_whois200_response_one_of_dict = get_network_whois200_response_one_of_instance.to_dict()
# create an instance of GetNetworkWhois200ResponseOneOf from a dict
get_network_whois200_response_one_of_from_dict = GetNetworkWhois200ResponseOneOf.from_dict(get_network_whois200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


