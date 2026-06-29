# GetMiscMovieRatingRank200ResponseChannelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**items** | [**List[GetMiscMovieRatingRank200ResponseChannelsInnerItemsInner]**](GetMiscMovieRatingRank200ResponseChannelsInnerItemsInner.md) |  | [optional] 
**platform** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_movie_rating_rank200_response_channels_inner import GetMiscMovieRatingRank200ResponseChannelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscMovieRatingRank200ResponseChannelsInner from a JSON string
get_misc_movie_rating_rank200_response_channels_inner_instance = GetMiscMovieRatingRank200ResponseChannelsInner.from_json(json)
# print the JSON string representation of the object
print(GetMiscMovieRatingRank200ResponseChannelsInner.to_json())

# convert the object into a dict
get_misc_movie_rating_rank200_response_channels_inner_dict = get_misc_movie_rating_rank200_response_channels_inner_instance.to_dict()
# create an instance of GetMiscMovieRatingRank200ResponseChannelsInner from a dict
get_misc_movie_rating_rank200_response_channels_inner_from_dict = GetMiscMovieRatingRank200ResponseChannelsInner.from_dict(get_misc_movie_rating_rank200_response_channels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


