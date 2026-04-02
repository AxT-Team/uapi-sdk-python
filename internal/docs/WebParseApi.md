# uapi.WebParseApi

All URIs are relative to *https://uapis.cn/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_tomarkdown_async_status**](WebParseApi.md#get_web_tomarkdown_async_status) | **GET** /web/tomarkdown/async/{task_id} | 转换任务状态
[**get_webparse_extractimages**](WebParseApi.md#get_webparse_extractimages) | **GET** /webparse/extractimages | 提取网页图片
[**get_webparse_metadata**](WebParseApi.md#get_webparse_metadata) | **GET** /webparse/metadata | 提取网页元数据
[**post_web_tomarkdown_async**](WebParseApi.md#post_web_tomarkdown_async) | **POST** /web/tomarkdown/async | 网页转 Markdown


# **get_web_tomarkdown_async_status**
> GetWebTomarkdownAsyncStatus200Response get_web_tomarkdown_async_status(task_id)

转换任务状态

提交了网页转 Markdown 任务后，想知道处理进度和结果？用这个接口来查询。

## 功能概述
通过任务 ID 查询转换任务的当前状态、处理进度和最终结果。任务结果缓存 30 分钟，期间可重复查询。

## 任务状态

| 状态 | 说明 |
|------|------|
| `pending` | 等待处理 |
| `processing` | 处理中 |
| `completed` | 已完成，可获取结果 |
| `failed` | 失败 |
| `timeout` | 超时（超过 60 秒） |

> [!NOTE]
> 建议每 2-5 秒轮询一次，当状态为 `completed`、`failed` 或 `timeout` 时停止轮询。

### Example


```python
import uapi
from uapi.models.get_web_tomarkdown_async_status200_response import GetWebTomarkdownAsyncStatus200Response
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
    api_instance = uapi.WebParseApi(api_client)
    task_id = 'a1b2c3d4-e5f6-47a8-b9c0-d1e2f3a4b5c6' # str | 任务ID（由提交接口返回）

    try:
        # 转换任务状态
        api_response = api_instance.get_web_tomarkdown_async_status(task_id)
        print("The response of WebParseApi->get_web_tomarkdown_async_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebParseApi->get_web_tomarkdown_async_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| 任务ID（由提交接口返回） | 

### Return type

[**GetWebTomarkdownAsyncStatus200Response**](GetWebTomarkdownAsyncStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功获取任务状态（包含各种状态的响应） |  -  |
**404** | 任务不存在或已过期 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webparse_extractimages**
> GetWebparseExtractimages200Response get_webparse_extractimages(url)

提取网页图片

想批量获取一个网页上的所有图片链接？这个接口帮你搞定。

## 功能概述
提供一个网页 URL，返回该页面中所有图片的链接列表。适合用于图片采集、素材下载等场景。

### Example


```python
import uapi
from uapi.models.get_webparse_extractimages200_response import GetWebparseExtractimages200Response
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
    api_instance = uapi.WebParseApi(api_client)
    url = 'https://cn.bing.com/' # str | 需要提取图片的网页URL

    try:
        # 提取网页图片
        api_response = api_instance.get_webparse_extractimages(url)
        print("The response of WebParseApi->get_webparse_extractimages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebParseApi->get_webparse_extractimages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 需要提取图片的网页URL | 

### Return type

[**GetWebparseExtractimages200Response**](GetWebparseExtractimages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功响应 |  -  |
**400** | URL参数缺失或无效 |  -  |
**500** | 服务器内部错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webparse_metadata**
> GetWebparseMetadata200Response get_webparse_metadata(url)

提取网页元数据

想在应用里做链接预览卡片？这个接口帮你一键获取网页的标题、描述、图标等信息。

## 功能概述
提供一个网页 URL，返回该页面的元数据，包括标题、描述、关键词、Favicon、Open Graph 信息等。非常适合用于生成链接预览卡片或做 SEO 分析。

### Example


```python
import uapi
from uapi.models.get_webparse_metadata200_response import GetWebparseMetadata200Response
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
    api_instance = uapi.WebParseApi(api_client)
    url = 'https://www.bilibili.com' # str | 需要提取元数据的网页URL

    try:
        # 提取网页元数据
        api_response = api_instance.get_webparse_metadata(url)
        print("The response of WebParseApi->get_webparse_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebParseApi->get_webparse_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 需要提取元数据的网页URL | 

### Return type

[**GetWebparseMetadata200Response**](GetWebparseMetadata200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功响应 |  -  |
**400** | URL参数缺失或无效 |  -  |
**500** | 服务器内部错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_web_tomarkdown_async**
> PostWebTomarkdownAsync202Response post_web_tomarkdown_async(url)

网页转 Markdown

想把一个网页的内容转成干净的 Markdown 文本？这个异步接口可以帮你搞定，特别适合处理大型或复杂的网页。

## 功能概述

提交一个网页 URL，我们会自动抓取主体内容，剔除广告、导航栏等干扰元素，并转换为 Markdown 格式。同时会提取标题、作者、发布日期等元数据，生成 YAML Front Matter。

任务提交后会立即返回任务 ID，你可以用它来查询处理进度和结果。单个任务最长处理 60 秒，结果缓存 30 分钟。

### Example


```python
import uapi
from uapi.models.post_web_tomarkdown_async202_response import PostWebTomarkdownAsync202Response
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
    api_instance = uapi.WebParseApi(api_client)
    url = 'https://example.com' # str | 需要转换的网页URL。URL必须经过编码。

    try:
        # 网页转 Markdown
        api_response = api_instance.post_web_tomarkdown_async(url)
        print("The response of WebParseApi->post_web_tomarkdown_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebParseApi->post_web_tomarkdown_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 需要转换的网页URL。URL必须经过编码。 | 

### Return type

[**PostWebTomarkdownAsync202Response**](PostWebTomarkdownAsync202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | 任务已提交成功，返回任务ID |  -  |
**400** | 请求参数错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

