# GetGithubUser200ResponseActivityContributionCalendar

按周整理好的贡献日历数据。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colors** | **List[str]** | 贡献等级对应的颜色列表。 | [optional] 
**is_halloween** | **bool** | 是否启用了 GitHub 万圣节配色主题。 | [optional] 
**total_contributions** | **int** | 贡献日历中的总贡献数。 | [optional] 
**weeks** | [**List[GetGithubUser200ResponseActivityContributionCalendarWeeksInner]**](GetGithubUser200ResponseActivityContributionCalendarWeeksInner.md) | 按周排列的贡献日历列数据。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_activity_contribution_calendar import GetGithubUser200ResponseActivityContributionCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseActivityContributionCalendar from a JSON string
get_github_user200_response_activity_contribution_calendar_instance = GetGithubUser200ResponseActivityContributionCalendar.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseActivityContributionCalendar.to_json())

# convert the object into a dict
get_github_user200_response_activity_contribution_calendar_dict = get_github_user200_response_activity_contribution_calendar_instance.to_dict()
# create an instance of GetGithubUser200ResponseActivityContributionCalendar from a dict
get_github_user200_response_activity_contribution_calendar_from_dict = GetGithubUser200ResponseActivityContributionCalendar.from_dict(get_github_user200_response_activity_contribution_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


