# uapi.PoemApi

All URIs are relative to *https://uapis.cn/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saying**](PoemApi.md#get_saying) | **GET** /saying | 随机获取一句诗词或名言


# **get_saying**
> GetSaying200Response get_saying()

随机获取一句诗词或名言

想在你的应用里每天展示一句不一样的话，给用户一点小小的惊喜吗？这个“一言”接口就是为此而生。

## 功能概述
每次调用，它都会从我们精心收集的、包含数千条诗词、动漫台词、名人名言的语料库中，随机返回一条。你可以用它来做网站首页的Slogan、应用的启动语，或者任何需要灵感点缀的地方。

### Example


```python
import uapi
from uapi.models.get_saying200_response import GetSaying200Response
from uapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://uapis.cn/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = uapi.Configuration(
    host = "https://uapis.cn/api/v1"
)


# Enter a context with an instance of the API client
with uapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = uapi.PoemApi(api_client)

    try:
        # 随机获取一句诗词或名言
        api_response = api_instance.get_saying()
        print("The response of PoemApi->get_saying:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoemApi->get_saying: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSaying200Response**](GetSaying200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 请求成功！返回一条随机的语录。 |  -  |
**500** | 当语料库为空或无法读取时。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

