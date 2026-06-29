# GetMiscMovieRatingRank200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[GetMiscMovieRatingRank200ResponseChannelsInner]**](GetMiscMovieRatingRank200ResponseChannelsInner.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**period** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_misc_movie_rating_rank200_response import GetMiscMovieRatingRank200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscMovieRatingRank200Response from a JSON string
get_misc_movie_rating_rank200_response_instance = GetMiscMovieRatingRank200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscMovieRatingRank200Response.to_json())

# convert the object into a dict
get_misc_movie_rating_rank200_response_dict = get_misc_movie_rating_rank200_response_instance.to_dict()
# create an instance of GetMiscMovieRatingRank200Response from a dict
get_misc_movie_rating_rank200_response_from_dict = GetMiscMovieRatingRank200Response.from_dict(get_misc_movie_rating_rank200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


