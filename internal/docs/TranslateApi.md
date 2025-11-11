# uapi.TranslateApi

All URIs are relative to *https://uapis.cn/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_translate_languages**](TranslateApi.md#get_ai_translate_languages) | **GET** /ai/translate/languages | 获取AI翻译支持的语言和配置
[**post_ai_translate**](TranslateApi.md#post_ai_translate) | **POST** /ai/translate | AI智能翻译
[**post_translate_text**](TranslateApi.md#post_translate_text) | **POST** /translate/text | 多语言文本翻译


# **get_ai_translate_languages**
> GetAiTranslateLanguages200Response get_ai_translate_languages()

获取AI翻译支持的语言和配置

获取AI智能翻译服务支持的完整语言列表、翻译风格选项、上下文场景选项以及性能指标信息。这个接口对于需要在前端动态展示翻译配置选项的应用非常有用，它会返回当前AI翻译服务所支持的所有语言代码、原生名称、翻译风格说明、上下文场景描述，以及服务的性能特征和限制信息。通过此接口，开发者可以构建用户友好的翻译界面，让用户选择合适的翻译参数。

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
        # 获取AI翻译支持的语言和配置
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
**200** | 成功获取AI翻译配置信息！ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_translate**
> PostAiTranslate200Response post_ai_translate(target_lang, post_ai_translate_request)

AI智能翻译

这是一个商业级的AI智能翻译服务，采用最新的神经网络翻译技术和大语言模型，提供远超传统机器翻译的质量。它不仅能够智能处理单个文本翻译，还支持高效的批量文本翻译，并且具备上下文感知、风格适配、格式保留等高级功能。

> [!VIP]
> 本API目前处于**限时免费**阶段，我们鼓励开发者深度集成和测试。未来，它将转为付费API，为用户提供更稳定、更智能的翻译服务。

## 功能概述

- **智能双模式**: 支持单个文本翻译和批量文本翻译的统一接口设计，自动识别请求类型并提供相应的翻译服务。系统会根据输入自动判断是处理单条文本还是批量文本，无需使用不同的接口。
- **多风格适配**: 提供随意口语化、专业商务、学术正式、文学艺术四种翻译风格，能够根据不同场景需求调整翻译的语言风格和表达方式。
- **上下文感知**: 支持通用、商务、技术、医疗、法律、市场营销、娱乐、教育、新闻等九种专业领域的上下文翻译，确保术语准确性和表达地道性。
- **高质量保证**: 内置质量评估系统，对每次翻译结果进行流畅度、准确度、完整性评分，并提供置信度分数和替代翻译建议。
- **智能解释**: 提供关键词组翻译注释、文化背景说明和语法结构分析，帮助用户理解翻译逻辑和文化差异。
- **高效批量**: 批量翻译支持最多50条文本，总计10万字符，配备智能并发控制（1-10并发）和失败重试机制。
- **快速模式**: 提供快速模式选项，在保证95%+准确率的前提下，响应时间缩短至800ms内，适合实时翻译和聊天应用。
- **格式保留**: 智能识别并保持原文的格式结构，包括换行、缩进、特殊符号等，确保翻译后的文本保持良好的可读性。

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
    target_lang = 'zh-CHS' # str | 目标语言代码。请从支持的语言列表中选择一个语言代码。
    post_ai_translate_request = uapi.PostAiTranslateRequest() # PostAiTranslateRequest | 包含翻译参数的JSON对象，支持单个文本或批量文本翻译

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
 **target_lang** | **str**| 目标语言代码。请从支持的语言列表中选择一个语言代码。 | 
 **post_ai_translate_request** | [**PostAiTranslateRequest**](PostAiTranslateRequest.md)| 包含翻译参数的JSON对象，支持单个文本或批量文本翻译 | 

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
**200** | 翻译成功！返回翻译结果、质量指标和性能统计。 |  -  |
**400** | 请求参数错误。请检查必填参数和参数格式是否正确。 |  -  |
**401** | 认证失败。请检查API密钥是否有效。 |  -  |
**429** | 请求频率过高。请稍后重试。 |  -  |
**500** | 翻译服务内部错误。请稍后重试或联系技术支持。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_translate_text**
> PostTranslateText200Response post_translate_text(to_lang, post_translate_text_request)

多语言文本翻译

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
    to_lang = 'zh-CHS' # str | 目标语言代码。请从支持的语言列表中选择一个语言代码。
    post_translate_text_request = uapi.PostTranslateTextRequest() # PostTranslateTextRequest | 包含待翻译文本的JSON对象

    try:
        # 多语言文本翻译
        api_response = api_instance.post_translate_text(to_lang, post_translate_text_request)
        print("The response of TranslateApi->post_translate_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->post_translate_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_lang** | **str**| 目标语言代码。请从支持的语言列表中选择一个语言代码。 | 
 **post_translate_text_request** | [**PostTranslateTextRequest**](PostTranslateTextRequest.md)| 包含待翻译文本的JSON对象 | 

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

