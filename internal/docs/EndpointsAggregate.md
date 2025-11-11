# EndpointsAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[EndpointsAggregateEndpointsInner]**](EndpointsAggregateEndpointsInner.md) |  | [optional] 
**unaggregated** | [**EndpointsAggregateUnaggregated**](EndpointsAggregateUnaggregated.md) |  | [optional] 

## Example

```python
from uapi.models.endpoints_aggregate import EndpointsAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsAggregate from a JSON string
endpoints_aggregate_instance = EndpointsAggregate.from_json(json)
# print the JSON string representation of the object
print(EndpointsAggregate.to_json())

# convert the object into a dict
endpoints_aggregate_dict = endpoints_aggregate_instance.to_dict()
# create an instance of EndpointsAggregate from a dict
endpoints_aggregate_from_dict = EndpointsAggregate.from_dict(endpoints_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


