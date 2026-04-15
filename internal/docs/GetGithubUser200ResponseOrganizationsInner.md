# GetGithubUser200ResponseOrganizationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | 组织登录名。 | [optional] 
**description** | **str** | 组织简介。 | [optional] 
**html_url** | **str** | 组织主页链接。 | [optional] 
**avatar_url** | **str** | 组织头像链接。 | [optional] 

## Example

```python
from uapi.models.get_github_user200_response_organizations_inner import GetGithubUser200ResponseOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser200ResponseOrganizationsInner from a JSON string
get_github_user200_response_organizations_inner_instance = GetGithubUser200ResponseOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser200ResponseOrganizationsInner.to_json())

# convert the object into a dict
get_github_user200_response_organizations_inner_dict = get_github_user200_response_organizations_inner_instance.to_dict()
# create an instance of GetGithubUser200ResponseOrganizationsInner from a dict
get_github_user200_response_organizations_inner_from_dict = GetGithubUser200ResponseOrganizationsInner.from_dict(get_github_user200_response_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


