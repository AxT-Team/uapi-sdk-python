# GetStatusRatelimit200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepts** | **int** | Total number of accepted requests | [optional] 
**in_flight** | **int** | Number of current in-flight requests | [optional] 
**last_update** | **str** | Last update time of the status | [optional] 
**limit** | **int** | Current concurrency limit | [optional] 
**load** | **float** | Calculated system load (in_flight / limit) | [optional] 
**min_rtt** | **float** | Minimum observed RTT in milliseconds | [optional] 
**rejects** | **int** | Total number of rejected requests | [optional] 
**rtt** | **float** | Smoothed RTT in milliseconds | [optional] 
**throttled** | **int** | Total number of throttled requests | [optional] 

## Example

```python
from uapi.models.get_status_ratelimit200_response import GetStatusRatelimit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusRatelimit200Response from a JSON string
get_status_ratelimit200_response_instance = GetStatusRatelimit200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatusRatelimit200Response.to_json())

# convert the object into a dict
get_status_ratelimit200_response_dict = get_status_ratelimit200_response_instance.to_dict()
# create an instance of GetStatusRatelimit200Response from a dict
get_status_ratelimit200_response_from_dict = GetStatusRatelimit200Response.from_dict(get_status_ratelimit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


