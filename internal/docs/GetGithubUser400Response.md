# GetGithubUser400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 错误码。 | [optional] 
**error** | **str** | 错误原因说明。 | [optional] 

## Example

```python
from uapi.models.get_github_user400_response import GetGithubUser400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser400Response from a JSON string
get_github_user400_response_instance = GetGithubUser400Response.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser400Response.to_json())

# convert the object into a dict
get_github_user400_response_dict = get_github_user400_response_instance.to_dict()
# create an instance of GetGithubUser400Response from a dict
get_github_user400_response_from_dict = GetGithubUser400Response.from_dict(get_github_user400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


