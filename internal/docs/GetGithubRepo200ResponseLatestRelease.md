# GetGithubRepo200ResponseLatestRelease

仓库最新发布版本信息，如果没有 Release 则为 null。可用于实现应用更新检查功能。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** | 版本标签 | [optional] 
**name** | **str** | 发布名称 | [optional] 
**published_at** | **datetime** | 发布时间 | [optional] 
**html_url** | **str** | Release 页面链接 | [optional] 
**prerelease** | **bool** | 是否为预发布版本 | [optional] 
**draft** | **bool** | 是否为草稿 | [optional] 

## Example

```python
from uapi.models.get_github_repo200_response_latest_release import GetGithubRepo200ResponseLatestRelease

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubRepo200ResponseLatestRelease from a JSON string
get_github_repo200_response_latest_release_instance = GetGithubRepo200ResponseLatestRelease.from_json(json)
# print the JSON string representation of the object
print(GetGithubRepo200ResponseLatestRelease.to_json())

# convert the object into a dict
get_github_repo200_response_latest_release_dict = get_github_repo200_response_latest_release_instance.to_dict()
# create an instance of GetGithubRepo200ResponseLatestRelease from a dict
get_github_repo200_response_latest_release_from_dict = GetGithubRepo200ResponseLatestRelease.from_dict(get_github_repo200_response_latest_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


