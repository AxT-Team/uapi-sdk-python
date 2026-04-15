# GetGithubUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | GitHub 登录名。 | [optional] 
**name** | **str** | 用户公开显示的名称。 | [optional] 
**bio** | **str** | 用户个人简介。 | [optional] 
**company** | **str** | 用户填写的公司或组织信息。 | [optional] 
**location** | **str** | 用户公开展示的地理位置。 | [optional] 
**blog** | **str** | 用户填写的网站或博客地址。 | [optional] 
**twitter_username** | **str** | 用户绑定的 X（Twitter）用户名。 | [optional] 
**email** | **str** | 用户公开可见的邮箱地址。 | [optional] 
**html_url** | **str** | GitHub 个人主页链接。 | [optional] 
**avatar_url** | **str** | 用户头像图片链接。 | [optional] 
**type** | **str** | 账号类型，常见值为 User 或 Organization。 | [optional] 
**public_repos** | **int** | 公开仓库数量。 | [optional] 
**public_gists** | **int** | 公开 Gist 数量。 | [optional] 
**followers** | **int** | 关注该用户的人数。 | [optional] 
**following** | **int** | 该用户正在关注的人数。 | [optional] 
**created_at** | **datetime** | GitHub 账号创建时间（ISO 8601）。 | [optional] 
**updated_at** | **datetime** | 用户资料最近更新时间（ISO 8601）。 | [optional] 
**organizations** | [**List[GetGithubUser200ResponseOrganizationsInner]**](GetGithubUser200ResponseOrganizationsInner.md) | 用户公开加入的组织列表 | [optional] 
**activity** | [**GetGithubUser200ResponseActivity**](GetGithubUser200ResponseActivity.md) |  | [optional] 

## Example

```python
from uapi.models.get_github_user200_response import GetGithubUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200Response from a JSON string
get_github_user200_response_instance = GetGithubUser200Response.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200Response.to_json())

# convert the object into a dict
get_github_user200_response_dict = get_github_user200_response_instance.to_dict()
# create an instance of GetGithubUser200Response from a dict
get_github_user200_response_from_dict = GetGithubUser200Response.from_dict(get_github_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


