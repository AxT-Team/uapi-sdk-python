# GetGithubUser400ResponseOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 错误码。 | [optional] 
**error** | **str** | 错误原因说明。 | [optional] 

## Example

```python
from uapi.models.get_github_user400_response_one_of1 import GetGithubUser400ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubUser400ResponseOneOf1 from a JSON string
get_github_user400_response_one_of1_instance = GetGithubUser400ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(GetGithubUser400ResponseOneOf1.to_json())

# convert the object into a dict
get_github_user400_response_one_of1_dict = get_github_user400_response_one_of1_instance.to_dict()
# create an instance of GetGithubUser400ResponseOneOf1 from a dict
get_github_user400_response_one_of1_from_dict = GetGithubUser400ResponseOneOf1.from_dict(get_github_user400_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


