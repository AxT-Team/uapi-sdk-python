# GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | 当天日期。 | [optional] 
**contribution_count** | **int** | 当天的贡献次数。 | [optional] 
**color** | **str** | 当天贡献等级对应的颜色值。 | [optional] 
**weekday** | **int** | 星期索引，0 表示周日，6 表示周六。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner import GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner from a JSON string
get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner_instance = GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner.to_json())

# convert the object into a dict
get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner_dict = get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner_instance.to_dict()
# create an instance of GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner from a dict
get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner_from_dict = GetGithubUser200ResponseActivityContributionCalendarWeeksInnerContributionDaysInner.from_dict(get_github_user200_response_activity_contribution_calendar_weeks_inner_contribution_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


