# GetGithubUser200ResponseActivityTimelineInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **str** | 月份，格式为 YYYY-MM。 | [optional] 
**contribution_count** | **int** | 该月的贡献总数。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_activity_timeline_inner import GetGithubUser200ResponseActivityTimelineInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseActivityTimelineInner from a JSON string
get_github_user200_response_activity_timeline_inner_instance = GetGithubUser200ResponseActivityTimelineInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseActivityTimelineInner.to_json())

# convert the object into a dict
get_github_user200_response_activity_timeline_inner_dict = get_github_user200_response_activity_timeline_inner_instance.to_dict()
# create an instance of GetGithubUser200ResponseActivityTimelineInner from a dict
get_github_user200_response_activity_timeline_inner_from_dict = GetGithubUser200ResponseActivityTimelineInner.from_dict(get_github_user200_response_activity_timeline_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


