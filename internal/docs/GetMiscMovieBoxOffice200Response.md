# GetMiscMovieBoxOffice200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[GetMiscMovieBoxOffice200ResponseListInner]**](GetMiscMovieBoxOffice200ResponseListInner.md) | 影片排名列表 | [optional] 
**market** | [**GetMiscMovieBoxOffice200ResponseMarket**](GetMiscMovieBoxOffice200ResponseMarket.md) |  | [optional] 
**total_items** | **int** | 返回的影片数量 | [optional] 
**update_gap_seconds** | **int** | 上游数据刷新间隔（秒） | [optional] 
**update_time** | **str** | 数据更新时间的格式化字符串 | [optional] 
**updated_at** | **int** | 数据更新时间戳（毫秒） | [optional] 

## Example

```python
from uapi.models.get_misc_movie_box_office200_response import GetMiscMovieBoxOffice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscMovieBoxOffice200Response from a JSON string
get_misc_movie_box_office200_response_instance = GetMiscMovieBoxOffice200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscMovieBoxOffice200Response.to_json())

# convert the object into a dict
get_misc_movie_box_office200_response_dict = get_misc_movie_box_office200_response_instance.to_dict()
# create an instance of GetMiscMovieBoxOffice200Response from a dict
get_misc_movie_box_office200_response_from_dict = GetMiscMovieBoxOffice200Response.from_dict(get_misc_movie_box_office200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


