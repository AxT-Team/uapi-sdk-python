# PostWatermarkProducerCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | **str** | 主体绑定的证件类型。组织需使用统一社会信用代码；个人可选身份证、手机号、护照或网号。 | [optional] 
**code** | **str** | 待校验的 27 位现成编码。填写后接口将直接执行合法性校验。 | [optional] 
**identifier** | **str** | 证件号实际内容。长度需匹配选择的类型（如统一社会信用代码 18 位、手机号 11 位）。 | [optional] 
**model_code** | **str** | 4 位自定义模型或应用码（可选）。未提供时扩展段将默认填充 00000。 | [optional] 
**service_type** | **str** | 服务角色类型（仅在提供模型应用码时一同生效）。 | [optional] 
**subject_type** | **str** | 主体类型是组织还是个人。 | [optional] 

## Example

```python
from uapi.models.post_watermark_producer_code_request import PostWatermarkProducerCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostWatermarkProducerCodeRequest from a JSON string
post_watermark_producer_code_request_instance = PostWatermarkProducerCodeRequest.from_json(json)
# print the JSON string representation of the object
print(PostWatermarkProducerCodeRequest.to_json())

# convert the object into a dict
post_watermark_producer_code_request_dict = post_watermark_producer_code_request_instance.to_dict()
# create an instance of PostWatermarkProducerCodeRequest from a dict
post_watermark_producer_code_request_from_dict = PostWatermarkProducerCodeRequest.from_dict(post_watermark_producer_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


