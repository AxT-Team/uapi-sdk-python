# GetSocialBilibiliUserinfo200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**mid** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**sign** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_social_bilibili_userinfo200_response_data import GetSocialBilibiliUserinfo200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSocialBilibiliUserinfo200ResponseData from a JSON string
get_social_bilibili_userinfo200_response_data_instance = GetSocialBilibiliUserinfo200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetSocialBilibiliUserinfo200ResponseData.to_json())

# convert the object into a dict
get_social_bilibili_userinfo200_response_data_dict = get_social_bilibili_userinfo200_response_data_instance.to_dict()
# create an instance of GetSocialBilibiliUserinfo200ResponseData from a dict
get_social_bilibili_userinfo200_response_data_from_dict = GetSocialBilibiliUserinfo200ResponseData.from_dict(get_social_bilibili_userinfo200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


