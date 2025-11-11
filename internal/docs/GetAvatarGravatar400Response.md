# GetAvatarGravatar400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from uapi.models.get_avatar_gravatar400_response import GetAvatarGravatar400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvatarGravatar400Response from a JSON string
get_avatar_gravatar400_response_instance = GetAvatarGravatar400Response.from_json(json)
# print the JSON string representation of the object
print(GetAvatarGravatar400Response.to_json())

# convert the object into a dict
get_avatar_gravatar400_response_dict = get_avatar_gravatar400_response_instance.to_dict()
# create an instance of GetAvatarGravatar400Response from a dict
get_avatar_gravatar400_response_from_dict = GetAvatarGravatar400Response.from_dict(get_avatar_gravatar400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


