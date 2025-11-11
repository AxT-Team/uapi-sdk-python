# GetGithubRepo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**default_branch** | **str** |  | [optional] 
**primary_branch** | **str** |  | [optional] 
**default_branch_sha** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**fork** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**license** | **str** |  | [optional] 
**stargazers** | **int** |  | [optional] 
**forks** | **int** |  | [optional] 
**open_issues** | **int** |  | [optional] 
**watchers** | **int** |  | [optional] 
**pushed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**languages** | **Dict[str, int]** |  | [optional] 
**collaborators** | [**List[GetGithubRepo200ResponseCollaboratorsInner]**](GetGithubRepo200ResponseCollaboratorsInner.md) |  | [optional] 
**maintainers** | [**List[GetGithubRepo200ResponseCollaboratorsInner]**](GetGithubRepo200ResponseCollaboratorsInner.md) |  | [optional] 

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


