# GetDailyNewsImage502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 机器可读的错误代码。 | [optional] 
**message** | **str** | 人类可读的错误描述信息。 | [optional] 

## Example

```python
from uapi.models.get_daily_news_image502_response import GetDailyNewsImage502Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyNewsImage502Response from a JSON string
get_daily_news_image502_response_instance = GetDailyNewsImage502Response.from_json(json)
# print the JSON string representation of the object
print(GetDailyNewsImage502Response.to_json())

# convert the object into a dict
get_daily_news_image502_response_dict = get_daily_news_image502_response_instance.to_dict()
# create an instance of GetDailyNewsImage502Response from a dict
get_daily_news_image502_response_from_dict = GetDailyNewsImage502Response.from_dict(get_daily_news_image502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


