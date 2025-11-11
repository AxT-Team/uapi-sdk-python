# GetGithubRepo400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_github_repo400_response import GetGithubRepo400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubRepo400Response from a JSON string
get_github_repo400_response_instance = GetGithubRepo400Response.from_json(json)
# print the JSON string representation of the object
print(GetGithubRepo400Response.to_json())

# convert the object into a dict
get_github_repo400_response_dict = get_github_repo400_response_instance.to_dict()
# create an instance of GetGithubRepo400Response from a dict
get_github_repo400_response_from_dict = GetGithubRepo400Response.from_dict(get_github_repo400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


