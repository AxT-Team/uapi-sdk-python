# GetGithubUser200ResponseActivityContributionCalendarWeeksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_day** | **str** | 这一周的第一天日期。 | [optional] 
**contribution_days** | [**List[GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner]**](GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner.md) | 这一周中每天的贡献明细。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_activity_contribution_calendar_weeks_inner import GetGithubUser200ResponseActivityContributionCalendarWeeksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseActivityContributionCalendarWeeksInner from a JSON string
get_github_user200_response_activity_contribution_calendar_weeks_inner_instance = GetGithubUser200ResponseActivityContributionCalendarWeeksInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseActivityContributionCalendarWeeksInner.to_json())

# convert the object into a dict
get_github_user200_response_activity_contribution_calendar_weeks_inner_dict = get_github_user200_response_activity_contribution_calendar_weeks_inner_instance.to_dict()
# create an instance of GetGithubUser200ResponseActivityContributionCalendarWeeksInner from a dict
get_github_user200_response_activity_contribution_calendar_weeks_inner_from_dict = GetGithubUser200ResponseActivityContributionCalendarWeeksInner.from_dict(get_github_user200_response_activity_contribution_calendar_weeks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


