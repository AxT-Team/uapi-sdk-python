# GetDailyNewsImage500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 机器可读的错误代码。 | [optional] 
**message** | **str** | 人类可读的错误描述信息。 | [optional] 

## Example

```python
from uapi.models.get_daily_news_image500_response import GetDailyNewsImage500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyNewsImage500Response from a JSON string
get_daily_news_image500_response_instance = GetDailyNewsImage500Response.from_json(json)
# print the JSON string representation of the object
print(GetDailyNewsImage500Response.to_json())

# convert the object into a dict
get_daily_news_image500_response_dict = get_daily_news_image500_response_instance.to_dict()
# create an instance of GetDailyNewsImage500Response from a dict
get_daily_news_image500_response_from_dict = GetDailyNewsImage500Response.from_dict(get_daily_news_image500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


