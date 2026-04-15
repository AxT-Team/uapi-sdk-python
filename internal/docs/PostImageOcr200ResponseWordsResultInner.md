# PostImageOcr200ResponseWordsResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**words** | **str** | 当前文字片段的识别结果。 | [optional] 
**location** | [**PostImageOcr200ResponseWordsResultInnerLocation**](PostImageOcr200ResponseWordsResultInnerLocation.md) |  | [optional] 
**vertexes_location** | [**List[PostImageOcr200ResponseWordsResultInnerVertexesLocationInner]**](PostImageOcr200ResponseWordsResultInnerVertexesLocationInner.md) | 当前文字片段的顶点坐标列表。只有在 &#x60;need_location&#x3D;true&#x60; 时才会返回。 | [optional] 
**score** | **float** | 当前文字片段的置信度。部分结果会返回。 | [optional] 

## Example

```python
from uapi.models.post_image_ocr200_response_words_result_inner import PostImageOcr200ResponseWordsResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageOcr200ResponseWordsResultInner from a JSON string
post_image_ocr200_response_words_result_inner_instance = PostImageOcr200ResponseWordsResultInner.from_json(json)
# print the JSON string representation of the object
print(PostImageOcr200ResponseWordsResultInner.to_json())

# convert the object into a dict
post_image_ocr200_response_words_result_inner_dict = post_image_ocr200_response_words_result_inner_instance.to_dict()
# create an instance of PostImageOcr200ResponseWordsResultInner from a dict
post_image_ocr200_response_words_result_inner_from_dict = PostImageOcr200ResponseWordsResultInner.from_dict(post_image_ocr200_response_words_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


