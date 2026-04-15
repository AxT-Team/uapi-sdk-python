# PostImageOcr200ResponseWordsResultInnerLocation

当前文字片段的矩形坐标。只有在 `need_location=true` 时才会返回。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **float** |  | [optional] 
**top** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 

## Example

```python
from uapi.models.post_image_ocr200_response_words_result_inner_location import PostImageOcr200ResponseWordsResultInnerLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PostImageOcr200ResponseWordsResultInnerLocation from a JSON string
post_image_ocr200_response_words_result_inner_location_instance = PostImageOcr200ResponseWordsResultInnerLocation.from_json(json)
# print the JSON string representation of the object
print(PostImageOcr200ResponseWordsResultInnerLocation.to_json())

# convert the object into a dict
post_image_ocr200_response_words_result_inner_location_dict = post_image_ocr200_response_words_result_inner_location_instance.to_dict()
# create an instance of PostImageOcr200ResponseWordsResultInnerLocation from a dict
post_image_ocr200_response_words_result_inner_location_from_dict = PostImageOcr200ResponseWordsResultInnerLocation.from_dict(post_image_ocr200_response_words_result_inner_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


