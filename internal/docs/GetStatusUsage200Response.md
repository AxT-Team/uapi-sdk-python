# GetStatusUsage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[EndpointsAggregateEndpointsInner]**](EndpointsAggregateEndpointsInner.md) |  | [optional] 
**unaggregated** | [**EndpointsAggregateUnaggregated**](EndpointsAggregateUnaggregated.md) |  | [optional] 
**path** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from uapi.models.get_status_usage200_response import GetStatusUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusUsage200Response from a JSON string
get_status_usage200_response_instance = GetStatusUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatusUsage200Response.to_json())

# convert the object into a dict
get_status_usage200_response_dict = get_status_usage200_response_instance.to_dict()
# create an instance of GetStatusUsage200Response from a dict
get_status_usage200_response_from_dict = GetStatusUsage200Response.from_dict(get_status_usage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


