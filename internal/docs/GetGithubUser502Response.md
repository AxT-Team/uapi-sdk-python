# GetGithubUser502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 错误码。 | [optional] 
**error** | **str** | 错误原因说明。 | [optional] 

## Example

```python
from uapi.models.get_github_user502_response import GetGithubUser502Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser502Response from a JSON string
get_github_user502_response_instance = GetGithubUser502Response.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser502Response.to_json())

# convert the object into a dict
get_github_user502_response_dict = get_github_user502_response_instance.to_dict()
# create an instance of GetGithubUser502Response from a dict
get_github_user502_response_from_dict = GetGithubUser502Response.from_dict(get_github_user502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


