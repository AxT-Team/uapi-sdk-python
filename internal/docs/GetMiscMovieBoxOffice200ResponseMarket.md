# GetMiscMovieBoxOffice200ResponseMarket

实时大盘汇总数据

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_office** | **str** | 实时总票房，带单位 | [optional] 
**show_count** | **str** | 实时总场次 | [optional] 
**split_box_office** | **str** | 实时分账票房，带单位 | [optional] 
**view_count** | **str** | 实时总人次 | [optional] 

## Example

```python
from uapi.models.get_misc_movie_box_office200_response_market import GetMiscMovieBoxOffice200ResponseMarket

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscMovieBoxOffice200ResponseMarket from a JSON string
get_misc_movie_box_office200_response_market_instance = GetMiscMovieBoxOffice200ResponseMarket.from_json(json)
# print the JSON string representation of the object
print(GetMiscMovieBoxOffice200ResponseMarket.to_json())

# convert the object into a dict
get_misc_movie_box_office200_response_market_dict = get_misc_movie_box_office200_response_market_instance.to_dict()
# create an instance of GetMiscMovieBoxOffice200ResponseMarket from a dict
get_misc_movie_box_office200_response_market_from_dict = GetMiscMovieBoxOffice200ResponseMarket.from_dict(get_misc_movie_box_office200_response_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


