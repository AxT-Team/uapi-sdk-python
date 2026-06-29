# PostWatermarkProducerCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | **str** | 解析出的证件绑定方式。 | [optional] 
**code** | **str** | 标准的 27 位服务提供者编码。 | [optional] 
**identifier** | **str** | 剔除补位后的主体证件原始明文。 | [optional] 
**model_code** | **str** | 解析出的模型/应用码（启用扩展时存在）。 | [optional] 
**service_extension** | **bool** | 编码中是否启用了服务扩展段。 | [optional] 
**service_type** | **str** | 解析出的服务角色类型（启用扩展时存在）。 | [optional] 
**subject_code** | **str** | 包含补位逻辑在内的 18 位主体特征段。 | [optional] 
**subject_type** | **str** | 解析出的主体类型。 | [optional] 
**valid** | **bool** | 该编码是否合规合法。 | [optional] 

## Example

```python
from uapi.models.post_watermark_producer_code200_response import PostWatermarkProducerCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostWatermarkProducerCode200Response from a JSON string
post_watermark_producer_code200_response_instance = PostWatermarkProducerCode200Response.from_json(json)
# print the JSON string representation of the object
print(PostWatermarkProducerCode200Response.to_json())

# convert the object into a dict
post_watermark_producer_code200_response_dict = post_watermark_producer_code200_response_instance.to_dict()
# create an instance of PostWatermarkProducerCode200Response from a dict
post_watermark_producer_code200_response_from_dict = PostWatermarkProducerCode200Response.from_dict(post_watermark_producer_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


