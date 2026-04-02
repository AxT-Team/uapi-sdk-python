# GetGithubRepo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** | 仓库完整名称。 | [optional] 
**description** | **str** | 仓库简介。 | [optional] 
**homepage** | **str** | 仓库主页链接。 | [optional] 
**default_branch** | **str** | 默认分支名称。 | [optional] 
**primary_branch** | **str** | 主要分支名称（通常与默认分支一致）。 | [optional] 
**default_branch_sha** | **str** | 默认分支最新提交的 SHA 哈希。 | [optional] 
**visibility** | **str** | 仓库可见性，常见值为 &#x60;public&#x60; 或 &#x60;private&#x60;。 | [optional] 
**archived** | **bool** | 仓库是否已归档。 | [optional] 
**disabled** | **bool** | 仓库是否被禁用。 | [optional] 
**fork** | **bool** | 是否为 Fork 仓库。 | [optional] 
**language** | **str** | 主要语言。 | [optional] 
**topics** | **List[str]** | 话题标签列表。 | [optional] 
**license** | **str** | 开源许可证名称。 | [optional] 
**stargazers** | **int** | Star 数。 | [optional] 
**forks** | **int** | Fork 数。 | [optional] 
**open_issues** | **int** | 开放 Issue 数。 | [optional] 
**watchers** | **int** | 关注者数量（watchers/subscribers）。 | [optional] 
**pushed_at** | **datetime** | 最后推送时间（ISO 8601）。 | [optional] 
**created_at** | **datetime** | 创建时间（ISO 8601）。 | [optional] 
**updated_at** | **datetime** | 更新时间（ISO 8601）。 | [optional] 
**languages** | **Dict[str, int]** | 语言统计（键为语言名，值为代码字节数）。 | [optional] 
**collaborators** | [**List[GetGithubRepo200ResponseCollaboratorsInner]**](GetGithubRepo200ResponseCollaboratorsInner.md) | 协作者列表。受权限限制时可能为 null 或空数组。 | [optional] 
**maintainers** | [**List[GetGithubRepo200ResponseCollaboratorsInner]**](GetGithubRepo200ResponseCollaboratorsInner.md) | 维护者列表（根据默认分支近期提交推断）。 | [optional] 
**latest_release** | [**GetGithubRepo200ResponseLatestRelease**](GetGithubRepo200ResponseLatestRelease.md) |  | [optional] 

## Example

```python
from uapi.models.get_github_repo200_response import GetGithubRepo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubRepo200Response from a JSON string
get_github_repo200_response_instance = GetGithubRepo200Response.from_json(json)
# print the JSON string representation of the object
print(GetGithubRepo200Response.to_json())

# convert the object into a dict
get_github_repo200_response_dict = get_github_repo200_response_instance.to_dict()
# create an instance of GetGithubRepo200Response from a dict
get_github_repo200_response_from_dict = GetGithubRepo200Response.from_dict(get_github_repo200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


