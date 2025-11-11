# GetGithubRepo200ResponseCollaboratorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_github_repo200_response_collaborators_inner import GetGithubRepo200ResponseCollaboratorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubRepo200ResponseCollaboratorsInner from a JSON string
get_github_repo200_response_collaborators_inner_instance = GetGithubRepo200ResponseCollaboratorsInner.from_json(json)
# print the JSON string representation of the object
print(GetGithubRepo200ResponseCollaboratorsInner.to_json())

# convert the object into a dict
get_github_repo200_response_collaborators_inner_dict = get_github_repo200_response_collaborators_inner_instance.to_dict()
# create an instance of GetGithubRepo200ResponseCollaboratorsInner from a dict
get_github_repo200_response_collaborators_inner_from_dict = GetGithubRepo200ResponseCollaboratorsInner.from_dict(get_github_repo200_response_collaborators_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


