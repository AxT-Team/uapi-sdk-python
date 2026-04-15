# uapi.TranslateApi

All URIs are relative to *https://uapis.cn/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_translate_languages**](TranslateApi.md#get_ai_translate_languages) | **GET** /ai/translate/languages | AI翻译配置
[**post_ai_translate**](TranslateApi.md#post_ai_translate) | **POST** /ai/translate | AI智能翻译
[**post_translate_stream**](TranslateApi.md#post_translate_stream) | **POST** /translate/stream | 流式翻译（中英互译）
[**post_translate_text**](TranslateApi.md#post_translate_text) | **POST** /translate/text | 翻译


# **get_ai_translate_languages**
> GetAiTranslateLanguages200Response get_ai_translate_languages()

AI翻译配置

获取AI智能翻译服务支持的完整语言列表、翻译风格选项、上下文场景选项以及性能指标信息。

### Example


```python
import uapi
from uapi.models.get_ai_translate_languages200_response import GetAiTranslateLanguages200Response
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
    api_instance = uapi.TranslateApi(api_client)

    try:
        # AI翻译配置
        api_response = api_instance.get_ai_translate_languages()
        print("The response of TranslateApi->get_ai_translate_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->get_ai_translate_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAiTranslateLanguages200Response**](GetAiTranslateLanguages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功获取AI翻译配置信息 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_translate**
> PostAiTranslate200Response post_ai_translate(target_lang, post_ai_translate_request)

AI智能翻译

这是一个高质量的智能翻译服务，支持多种翻译风格和专业场景，适合对译文质量有更高要求的业务场景。

## 功能概述

- **单文本翻译**: 专注处理单条文本翻译，适合需要高质量译文的业务场景。
- **多风格适配**: 提供随意口语化、专业商务、学术正式、文学艺术四种翻译风格，能够根据不同场景需求调整翻译的语言风格和表达方式。
- **上下文感知**: 支持通用、商务、技术、医疗、法律、市场营销、娱乐、教育、新闻等九种专业领域的上下文翻译，确保术语准确性和表达地道性。
- **格式保留**: 智能识别并保持原文的格式结构，包括换行、缩进、特殊符号等，确保翻译后的文本保持良好的可读性。

## 支持的语言

我们支持超过100种语言的互译，详见下方参数列表。

### Example


```python
import uapi
from uapi.models.post_ai_translate200_response import PostAiTranslate200Response
from uapi.models.post_ai_translate_request import PostAiTranslateRequest
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
    api_instance = uapi.TranslateApi(api_client)
    target_lang = 'zh' # str | 目标语言代码。请从[支持的语言列表](#enum-list)中选择一个语言代码。
    post_ai_translate_request = uapi.PostAiTranslateRequest() # PostAiTranslateRequest | 

    try:
        # AI智能翻译
        api_response = api_instance.post_ai_translate(target_lang, post_ai_translate_request)
        print("The response of TranslateApi->post_ai_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->post_ai_translate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_lang** | **str**| 目标语言代码。请从[支持的语言列表](#enum-list)中选择一个语言代码。 | 
 **post_ai_translate_request** | [**PostAiTranslateRequest**](PostAiTranslateRequest.md)|  | 

### Return type

[**PostAiTranslate200Response**](PostAiTranslate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 翻译成功！返回翻译结果和性能统计。 |  -  |
**400** | 请求参数错误。请检查必填参数和参数格式是否正确。 |  -  |
**401** | 认证失败。请检查API密钥是否有效。 |  -  |
**429** | 请求频率过高。请稍后重试。 |  -  |
**500** | 翻译服务内部错误。请稍后重试或联系技术支持。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_translate_stream**
> str post_translate_stream(post_translate_stream_request)

流式翻译（中英互译）

想让翻译结果像打字机一样逐字显示出来？这个流式翻译接口能实现这种效果。

## 功能概述
不同于传统翻译API一次性返回完整结果，这个接口会实时地、一个字一个字地把翻译内容推给你（就像ChatGPT回复消息那样），非常适合用在聊天应用、直播字幕等需要即时反馈的场景。

## 它能做什么
- **中英互译**：支持中文和英文之间的双向翻译
- **自动识别**：不确定源语言？设置为 `auto` 让我们自动检测
- **逐字返回**：翻译结果会像打字机一样逐字流式返回，用户体验更流畅
- **音频朗读**：部分翻译结果会附带音频链接，方便朗读

## 支持的语言
目前专注于中英互译，支持以下选项：
- `中文`（简体/繁体）
- `英文`
- `auto`（自动检测）

### Example


```python
import uapi
from uapi.models.post_translate_stream_request import PostTranslateStreamRequest
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
    api_instance = uapi.TranslateApi(api_client)
    post_translate_stream_request = uapi.PostTranslateStreamRequest() # PostTranslateStreamRequest | 

    try:
        # 流式翻译（中英互译）
        api_response = api_instance.post_translate_stream(post_translate_stream_request)
        print("The response of TranslateApi->post_translate_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->post_translate_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_translate_stream_request** | [**PostTranslateStreamRequest**](PostTranslateStreamRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE流式响应。Content-Type为text/event-stream |  -  |
**400** | 请求参数错误 |  -  |
**500** | 翻译服务错误 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_translate_text**
> PostTranslateText200Response post_translate_text(to_lang, post_translate_text_request)

翻译

需要跨越语言的鸿沟进行交流？这个翻译接口是你可靠的'同声传译'。

## 功能概述
你可以将一段源语言文本（我们能自动检测源语言）翻译成你指定的任何目标语言。无论是中译英、日译法，都不在话下。

## 支持的语言
我们支持超过100种语言的互译，包括但不限于：中文（简体/繁体）、英语、日语、韩语、法语、德语、西班牙语、俄语、阿拉伯语等主流语言，以及各种小语种。详见下方参数列表。

### Example


```python
import uapi
from uapi.models.post_translate_text200_response import PostTranslateText200Response
from uapi.models.post_translate_text_request import PostTranslateTextRequest
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
    api_instance = uapi.TranslateApi(api_client)
    to_lang = 'zh' # str | 目标语言代码。请从[支持的语言列表](#enum-list)中选择一个语言代码。
    post_translate_text_request = uapi.PostTranslateTextRequest() # PostTranslateTextRequest | 

    try:
        # 翻译
        api_response = api_instance.post_translate_text(to_lang, post_translate_text_request)
        print("The response of TranslateApi->post_translate_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->post_translate_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_lang** | **str**| 目标语言代码。请从[支持的语言列表](#enum-list)中选择一个语言代码。 | 
 **post_translate_text_request** | [**PostTranslateTextRequest**](PostTranslateTextRequest.md)|  | 

### Return type

[**PostTranslateText200Response**](PostTranslateText200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功响应 |  -  |
**400** | 无效的请求体 |  -  |
**500** | 翻译失败 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

