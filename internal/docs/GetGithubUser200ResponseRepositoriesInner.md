# GetGithubUser200ResponseRepositoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | 该仓库是否已归档。 | [optional] 
**description** | **str** | 仓库简介。 | [optional] 
**fork** | **bool** | 该仓库是否为 fork。 | [optional] 
**forks** | **int** | Fork 数量。 | [optional] 
**full_name** | **str** | 包含所有者的完整仓库名。 | [optional] 
**homepage** | **str** | 仓库填写的官网地址。 | [optional] 
**html_url** | **str** | 仓库主页链接。 | [optional] 
**language** | **str** | 仓库主语言。 | [optional] 
**name** | **str** | 仓库名。 | [optional] 
**pushed_at** | **datetime** | 最近一次 push 时间。 | [optional] 
**stargazers** | **int** | Star 数量。 | [optional] 
**updated_at** | **datetime** | 最近一次资料更新时间。 | [optional] 
**visibility** | **str** | 仓库可见性。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_repositories_inner import GetGithubUser200ResponseRepositoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseRepositoriesInner from a JSON string
get_github_user200_response_repositories_inner_instance = GetGithubUser200ResponseRepositoriesInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseRepositoriesInner.to_json())

# convert the object into a dict
get_github_user200_response_repositories_inner_dict = get_github_user200_response_repositories_inner_instance.to_dict()
# create an instance of GetGithubUser200ResponseRepositoriesInner from a dict
get_github_user200_response_repositories_inner_from_dict = GetGithubUser200ResponseRepositoriesInner.from_dict(get_github_user200_response_repositories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


