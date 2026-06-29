# GetMiscMovieBoxOffice200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_seat_view** | **str** | 上座率 | [optional] 
**avg_show_view** | **str** | 场均人次 | [optional] 
**box_office** | **str** | 实时综合票房，带单位 | [optional] 
**box_office_rate** | **str** | 实时综合票房占比 | [optional] 
**detail_url** | **str** | 电影详情页 URL | [optional] 
**movie_id** | **int** | 影片 ID | [optional] 
**movie_name** | **str** | 影片名称 | [optional] 
**rank** | **int** | 排名，从 1 开始 | [optional] 
**release_days** | **int** | 已上映天数。仅当 release_info 可解析为“上映N天”时返回 | [optional] 
**release_info** | **str** | 上游上映信息原文 | [optional] 
**release_status** | **str** | 结构化上映状态，可取 released、preview、re_release 或 other | [optional] 
**show_count** | **int** | 排片场次 | [optional] 
**show_count_rate** | **str** | 排片占比 | [optional] 
**split_box_office** | **str** | 实时分账票房，带单位 | [optional] 
**split_box_office_rate** | **str** | 实时分账票房占比 | [optional] 
**sum_box_office** | **str** | 累计综合票房 | [optional] 
**sum_split_box_office** | **str** | 累计分账票房 | [optional] 

## Example

```python
from uapi.models.get_misc_movie_box_office200_response_list_inner import GetMiscMovieBoxOffice200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscMovieBoxOffice200ResponseListInner from a JSON string
get_misc_movie_box_office200_response_list_inner_instance = GetMiscMovieBoxOffice200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscMovieBoxOffice200ResponseListInner.to_json())

# convert the object into a dict
get_misc_movie_box_office200_response_list_inner_dict = get_misc_movie_box_office200_response_list_inner_instance.to_dict()
# create an instance of GetMiscMovieBoxOffice200ResponseListInner from a dict
get_misc_movie_box_office200_response_list_inner_from_dict = GetMiscMovieBoxOffice200ResponseListInner.from_dict(get_misc_movie_box_office200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


