# GetMiscDistrict200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 地区名称。 | [optional] 
**level** | **str** | 行政级别：province / city / district / street。 | [optional] 
**country** | **str** | 国家名称。 | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-2 国家代码。 | [optional] 
**province** | **str** | 省/州（中国数据）或一级行政区（国际数据）。 | [optional] 
**city** | **str** | 市（仅中国数据）。 | [optional] 
**district** | **str** | 区/县（仅中国数据）。 | [optional] 
**street** | **str** | 街道/乡镇（仅中国数据）。 | [optional] 
**adcode** | **str** | 行政区划代码（仅中国数据）。 | [optional] 
**citycode** | **str** | 城市区号（仅中国数据）。 | [optional] 
**center** | [**GetMiscDistrict200ResponseResultsInnerCenter**](GetMiscDistrict200ResponseResultsInnerCenter.md) |  | [optional] 
**population** | **int** | 人口（仅国际城市数据）。 | [optional] 
**timezone** | **str** | 时区（仅国际城市数据），如 Asia/Tokyo。 | [optional] 

## Example

```python
from uapi.models.get_misc_district200_response_results_inner import GetMiscDistrict200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscDistrict200ResponseResultsInner from a JSON string
get_misc_district200_response_results_inner_instance = GetMiscDistrict200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscDistrict200ResponseResultsInner.to_json())

# convert the object into a dict
get_misc_district200_response_results_inner_dict = get_misc_district200_response_results_inner_instance.to_dict()
# create an instance of GetMiscDistrict200ResponseResultsInner from a dict
get_misc_district200_response_results_inner_from_dict = GetMiscDistrict200ResponseResultsInner.from_dict(get_misc_district200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


