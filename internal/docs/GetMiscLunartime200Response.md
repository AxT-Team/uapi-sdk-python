# GetMiscLunartime200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_timestamp** | **str** | 原始 ts 入参。 | [optional] 
**query_timezone** | **str** | 原始 timezone 入参。 | [optional] 
**timezone** | **str** | 解析后的时区。 | [optional] 
**datetime** | **str** | 本地化时间，格式 YYYY-MM-DD HH:mm:ss。 | [optional] 
**datetime_rfc3339** | **str** | RFC3339 时间格式。 | [optional] 
**timestamp_unix** | **int** | 秒级 Unix 时间戳。 | [optional] 
**weekday** | **str** | 星期英文。 | [optional] 
**weekday_cn** | **str** | 星期中文。 | [optional] 
**lunar_year** | **int** | 农历年份（数字）。 | [optional] 
**lunar_month** | **int** | 农历月份（数字）。 | [optional] 
**lunar_day** | **int** | 农历日期（数字）。 | [optional] 
**is_leap_month** | **bool** | 是否闰月。 | [optional] 
**lunar_year_cn** | **str** | 农历年份中文表示。 | [optional] 
**lunar_month_cn** | **str** | 农历月份中文表示。 | [optional] 
**lunar_day_cn** | **str** | 农历日期中文表示。 | [optional] 
**ganzhi_year** | **str** | 干支年。 | [optional] 
**ganzhi_month** | **str** | 干支月。 | [optional] 
**ganzhi_day** | **str** | 干支日。 | [optional] 
**zodiac** | **str** | 生肖。 | [optional] 
**solar_term** | **str** | 节气名称。有值时返回，无值时可能为空字符串或不返回。 | [optional] 
**lunar_festivals** | **List[str]** | 农历节日数组。 | [optional] 
**solar_festivals** | **List[str]** | 公历节日数组。 | [optional] 

## Example

```python
from uapi.models.get_misc_lunartime200_response import GetMiscLunartime200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMiscLunartime200Response from a JSON string
get_misc_lunartime200_response_instance = GetMiscLunartime200Response.from_json(json)
# print the JSON string representation of the object
print(GetMiscLunartime200Response.to_json())

# convert the object into a dict
get_misc_lunartime200_response_dict = get_misc_lunartime200_response_instance.to_dict()
# create an instance of GetMiscLunartime200Response from a dict
get_misc_lunartime200_response_from_dict = GetMiscLunartime200Response.from_dict(get_misc_lunartime200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


