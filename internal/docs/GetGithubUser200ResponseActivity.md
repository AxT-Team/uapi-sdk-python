# GetGithubUser200ResponseActivity

贡献活动数据（需开启 activity=true）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | 活动统计范围，常见值为 all 或 organization。 | [optional] 
**organization** | **str** | 按组织过滤时对应的组织登录名。 | [optional] 
**var_from** | **str** | 统计开始日期。 | [optional] 
**to** | **str** | 统计结束日期。 | [optional] 
**total_contributions** | **int** | 统计范围内的总贡献数。 | [optional] 
**total_commit_contributions** | **int** | Commit 贡献总数。 | [optional] 
**total_issue_contributions** | **int** | Issue 贡献总数。 | [optional] 
**total_pull_request_contributions** | **int** | Pull Request 贡献总数。 | [optional] 
**total_pull_request_review_contributions** | **int** | Pull Request Review 贡献总数。 | [optional] 
**contribution_calendar** | [**GetGithubUser200ResponseActivityContributionCalendar**](GetGithubUser200ResponseActivityContributionCalendar.md) |  | [optional] 
**timeline** | [**List[GetGithubUser200ResponseActivityTimelineInner]**](GetGithubUser200ResponseActivityTimelineInner.md) | 按月份聚合后的贡献时间线。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_activity import GetGithubUser200ResponseActivity

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseActivity from a JSON string
get_github_user200_response_activity_instance = GetGithubUser200ResponseActivity.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseActivity.to_json())

# convert the object into a dict
get_github_user200_response_activity_dict = get_github_user200_response_activity_instance.to_dict()
# create an instance of GetGithubUser200ResponseActivity from a dict
get_github_user200_response_activity_from_dict = GetGithubUser200ResponseActivity.from_dict(get_github_user200_response_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


