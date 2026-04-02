# GetSocialBilibiliVideoinfo200ResponseDimension

视频分辨率信息。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | 视频宽度。 | [optional] 
**height** | **float** | 视频高度。 | [optional] 
**rotate** | **float** | 旋转角度。 | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_videoinfo200_response_dimension import GetSocialBilibiliVideoinfo200ResponseDimension

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliVideoinfo200ResponseDimension from a JSON string
get_social_bilibili_videoinfo200_response_dimension_instance = GetSocialBilibiliVideoinfo200ResponseDimension.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliVideoinfo200ResponseDimension.to_json())

# convert the object into a dict
get_social_bilibili_videoinfo200_response_dimension_dict = get_social_bilibili_videoinfo200_response_dimension_instance.to_dict()
# create an instance of GetSocialBilibiliVideoinfo200ResponseDimension from a dict
get_social_bilibili_videoinfo200_response_dimension_from_dict = GetSocialBilibiliVideoinfo200ResponseDimension.from_dict(get_social_bilibili_videoinfo200_response_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


