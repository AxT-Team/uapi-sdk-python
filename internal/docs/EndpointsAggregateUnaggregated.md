# EndpointsAggregateUnaggregated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**oldest_log** | **str** |  | [optional] 

## Example

```python
from uapi.models.endpoints_aggregate_unaggregated import EndpointsAggregateUnaggregated

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsAggregateUnaggregated from a JSON string
endpoints_aggregate_unaggregated_instance = EndpointsAggregateUnaggregated.from_json(json)
# print the JSON string representation of the object
print(EndpointsAggregateUnaggregated.to_json())

# convert the object into a dict
endpoints_aggregate_unaggregated_dict = endpoints_aggregate_unaggregated_instance.to_dict()
# create an instance of EndpointsAggregateUnaggregated from a dict
endpoints_aggregate_unaggregated_from_dict = EndpointsAggregateUnaggregated.from_dict(endpoints_aggregate_unaggregated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


