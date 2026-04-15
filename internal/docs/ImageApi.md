# uapi.ImageApi

All URIs are relative to *https://uapis.cn/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_avatar_gravatar**](ImageApi.md#get_avatar_gravatar) | **GET** /avatar/gravatar | 获取Gravatar头像
[**get_image_bing_daily**](ImageApi.md#get_image_bing_daily) | **GET** /image/bing-daily | 获取必应每日壁纸
[**get_image_bing_daily_history**](ImageApi.md#get_image_bing_daily_history) | **GET** /image/bing-daily/history | 查询必应壁纸历史
[**get_image_motou**](ImageApi.md#get_image_motou) | **GET** /image/motou | 生成摸摸头GIF (QQ号)
[**get_image_qrcode**](ImageApi.md#get_image_qrcode) | **GET** /image/qrcode | 生成二维码
[**get_image_tobase64**](ImageApi.md#get_image_tobase64) | **GET** /image/tobase64 | 图片转 Base64
[**post_image_compress**](ImageApi.md#post_image_compress) | **POST** /image/compress | 无损压缩图片
[**post_image_decode**](ImageApi.md#post_image_decode) | **POST** /image/decode | 解码并缩放图片
[**post_image_frombase64**](ImageApi.md#post_image_frombase64) | **POST** /image/frombase64 | 通过Base64编码上传图片
[**post_image_motou**](ImageApi.md#post_image_motou) | **POST** /image/motou | 生成摸摸头GIF
[**post_image_nsfw**](ImageApi.md#post_image_nsfw) | **POST** /image/nsfw | 图片敏感检测
[**post_image_ocr**](ImageApi.md#post_image_ocr) | **POST** /image/ocr | 通用 OCR 文字识别
[**post_image_speechless**](ImageApi.md#post_image_speechless) | **POST** /image/speechless | 生成你们怎么不说话了表情包
[**post_image_svg**](ImageApi.md#post_image_svg) | **POST** /image/svg | SVG转图片


# **get_avatar_gravatar**
> bytearray get_avatar_gravatar(email=email, hash=hash, s=s, d=d, r=r)

获取Gravatar头像

提供稳定、易用的头像获取能力，适合在网页或应用中直接展示头像。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    email = 'shuakami@sdjz.wiki' # str | 用户的 Email 地址。如果未提供 `hash` 参数，则此参数为必需。 (optional)
    hash = 'hash_example' # str | 用户 Email 地址的小写 MD5 哈希值。如果提供此参数，将忽略 `email` 参数。 (optional)
    s = 80 # int | 头像的尺寸，单位为像素。有效范围是 1 到 2048。 (optional) (default to 80)
    d = 'mp' # str | 当用户没有自己的 Gravatar 头像时，显示的默认头像类型。可选值包括 `mp`, `identicon`, `monsterid`, `wavatar`, `retro`, `robohash`, `blank`, `404`。 (optional) (default to 'mp')
    r = 'g' # str | 头像分级。可选值：`g`, `pg`, `r`, `x`。 (optional) (default to 'g')

    try:
        # 获取Gravatar头像
        api_response = api_instance.get_avatar_gravatar(email=email, hash=hash, s=s, d=d, r=r)
        print("The response of ImageApi->get_avatar_gravatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_avatar_gravatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| 用户的 Email 地址。如果未提供 &#x60;hash&#x60; 参数，则此参数为必需。 | [optional] 
 **hash** | **str**| 用户 Email 地址的小写 MD5 哈希值。如果提供此参数，将忽略 &#x60;email&#x60; 参数。 | [optional] 
 **s** | **int**| 头像的尺寸，单位为像素。有效范围是 1 到 2048。 | [optional] [default to 80]
 **d** | **str**| 当用户没有自己的 Gravatar 头像时，显示的默认头像类型。可选值包括 &#x60;mp&#x60;, &#x60;identicon&#x60;, &#x60;monsterid&#x60;, &#x60;wavatar&#x60;, &#x60;retro&#x60;, &#x60;robohash&#x60;, &#x60;blank&#x60;, &#x60;404&#x60;。 | [optional] [default to &#39;mp&#39;]
 **r** | **str**| 头像分级。可选值：&#x60;g&#x60;, &#x60;pg&#x60;, &#x60;r&#x60;, &#x60;x&#x60;。 | [optional] [default to &#39;g&#39;]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功响应，返回图片二进制数据。 |  * Content-Type -  <br>  * ETag -  <br>  * Cache-Control -  <br>  |
**400** | 当请求中既没有提供 &#x60;email&#x60; 也没有提供 &#x60;hash&#x60; 参数时。 |  -  |
**404** | 当 &#x60;d&#x3D;404&#x60; 且请求的 email 或 hash 没有对应的 Gravatar 头像时。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_bing_daily**
> bytearray get_image_bing_daily(var_date=var_date, resolution=resolution, format=format)

获取必应每日壁纸

这个接口可以获取最新或指定日期的必应壁纸。默认直接返回图片，也可以传 `format=json` 获取元数据，或者传 `format=redirect` 直接跳转到最终图片地址。

## 功能概述
- 不传参数时，默认返回当天壁纸图片二进制
- 可以传 `date` 查询指定日期的壁纸
- 可以传 `resolution` 选择 `4k` 或 `1080`
- 可以传 `format` 控制返回图片、JSON 或 302 跳转
- 当传 `format=json` 时，返回的是扁平 JSON 对象，里面会包含标题、副标题、说明文案、版权信息、问答信息和图片地址等字段

## 参数说明
`resolution` 默认是 `4k`。
`format` 默认是 `image`。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    var_date = 'var_date_example' # str | 壁纸日期，格式是 `YYYY-MM-DD`。不传时返回当天壁纸。 (optional)
    resolution = 4k # str | 返回图片的目标分辨率。可以传 `4k` 或 `1080`，不传时默认是 `4k`。 (optional) (default to 4k)
    format = image # str | 响应格式。可以传 `image`、`json` 或 `redirect`。不传时默认是 `image`。 (optional) (default to image)

    try:
        # 获取必应每日壁纸
        api_response = api_instance.get_image_bing_daily(var_date=var_date, resolution=resolution, format=format)
        print("The response of ImageApi->get_image_bing_daily:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image_bing_daily: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| 壁纸日期，格式是 &#x60;YYYY-MM-DD&#x60;。不传时返回当天壁纸。 | [optional] 
 **resolution** | **str**| 返回图片的目标分辨率。可以传 &#x60;4k&#x60; 或 &#x60;1080&#x60;，不传时默认是 &#x60;4k&#x60;。 | [optional] [default to 4k]
 **format** | **str**| 响应格式。可以传 &#x60;image&#x60;、&#x60;json&#x60; 或 &#x60;redirect&#x60;。不传时默认是 &#x60;image&#x60;。 | [optional] [default to image]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 请求成功。&#x60;format&#x3D;image&#x60; 返回图片二进制，&#x60;format&#x3D;json&#x60; 返回壁纸元数据。 |  -  |
**302** | 当 &#x60;format&#x3D;redirect&#x60; 时，这个接口会通过 &#x60;Location&#x60; 响应头跳转到最终图片地址。 |  * Location -  <br>  |
**400** | 请求参数不正确。 |  -  |
**404** | 指定日期没有找到对应的壁纸。 |  -  |
**500** | 服务器处理失败，请稍后重试。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_bing_daily_history**
> GetImageBingDailyHistory200Response get_image_bing_daily_history(var_date=var_date, resolution=resolution, page=page, page_size=page_size)

查询必应壁纸历史

这个接口用于查询必应壁纸历史列表，也可以按日期精确查询某一天。默认按时间倒序返回 JSON。

## 功能概述
- 可以传 `date` 精确查询某一天，命中后只返回 1 条数据
- 不传 `date` 时，按时间倒序分页返回历史列表
- 可以传 `resolution` 让 `image_url` 直接对应 `4k` 或 `1080`
- 可以传 `page` 和 `page_size` 控制分页
- 每条记录都是扁平 JSON 对象，里面会包含标题、副标题、说明文案、版权信息、问答信息和图片地址等字段

## 参数说明
`resolution` 默认是 `4k`。
`page` 默认是 `1`，`page_size` 默认是 `30`，最大是 `100`。
当传了 `date` 以后，`page` 和 `page_size` 不生效。

### Example


```python
import uapi
from uapi.models.get_image_bing_daily_history200_response import GetImageBingDailyHistory200Response
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
    api_instance = uapi.ImageApi(api_client)
    var_date = '2026-04-05' # str | 壁纸日期，格式是 `YYYY-MM-DD`。传了以后会按日期精确查询，并且忽略 `page` 和 `page_size`。 (optional)
    resolution = 4k # str | 返回图片的目标分辨率。可以传 `4k` 或 `1080`，不传时默认是 `4k`。 (optional) (default to 4k)
    page = 1 # int | 分页页码，必须是正整数。不传时默认是 `1`。只有在不传 `date` 时才生效。 (optional) (default to 1)
    page_size = 30 # int | 每页条数，必须是正整数。不传时默认是 `30`，最大是 `100`。只有在不传 `date` 时才生效。 (optional) (default to 30)

    try:
        # 查询必应壁纸历史
        api_response = api_instance.get_image_bing_daily_history(var_date=var_date, resolution=resolution, page=page, page_size=page_size)
        print("The response of ImageApi->get_image_bing_daily_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image_bing_daily_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| 壁纸日期，格式是 &#x60;YYYY-MM-DD&#x60;。传了以后会按日期精确查询，并且忽略 &#x60;page&#x60; 和 &#x60;page_size&#x60;。 | [optional] 
 **resolution** | **str**| 返回图片的目标分辨率。可以传 &#x60;4k&#x60; 或 &#x60;1080&#x60;，不传时默认是 &#x60;4k&#x60;。 | [optional] [default to 4k]
 **page** | **int**| 分页页码，必须是正整数。不传时默认是 &#x60;1&#x60;。只有在不传 &#x60;date&#x60; 时才生效。 | [optional] [default to 1]
 **page_size** | **int**| 每页条数，必须是正整数。不传时默认是 &#x60;30&#x60;，最大是 &#x60;100&#x60;。只有在不传 &#x60;date&#x60; 时才生效。 | [optional] [default to 30]

### Return type

[**GetImageBingDailyHistory200Response**](GetImageBingDailyHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 查询成功，返回历史壁纸列表和分页信息。 |  -  |
**400** | 请求参数不正确。 |  -  |
**404** | 按日期精确查询时，没有找到对应的壁纸。 |  -  |
**500** | 服务器处理失败，请稍后重试。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_motou**
> bytearray get_image_motou(qq, bg_color=bg_color)

生成摸摸头GIF (QQ号)

想在线rua一下好友的头像吗？这个趣味接口可以满足你。

## 功能概述
此接口通过GET方法，专门用于通过QQ号生成摸摸头GIF。你只需要提供一个QQ号码，我们就会自动获取其公开头像，并制作成一个可爱的动图。

## 使用须知
- **响应格式**：接口成功时直接返回 `image/gif` 格式的二进制数据。
- **背景颜色**：你可以通过 `bg_color` 参数来控制GIF的背景。使用 `transparent` 选项可以让它更好地融入各种聊天背景中。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    qq = '10001' # str | 你想要摸头的对象的QQ号码。
    bg_color = 'transparent' # str | GIF的背景颜色。留空则由后端服务决定默认值。 (optional)

    try:
        # 生成摸摸头GIF (QQ号)
        api_response = api_instance.get_image_motou(qq, bg_color=bg_color)
        print("The response of ImageApi->get_image_motou:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image_motou: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qq** | **str**| 你想要摸头的对象的QQ号码。 | 
 **bg_color** | **str**| GIF的背景颜色。留空则由后端服务决定默认值。 | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 生成成功！响应体是GIF格式的图片二进制数据。 |  -  |
**400** | 请求参数错误。必须提供有效的 &#39;qq&#39; 参数。 |  -  |
**500** | 服务器内部错误。可能的原因包括：获取QQ头像失败，或在生成GIF过程中发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_qrcode**
> bytearray get_image_qrcode(text, size=size, format=format, transparent=transparent, fgcolor=fgcolor, bgcolor=bgcolor)

生成二维码

无论是网址、文本还是联系方式，通通可以变成一个二维码！这是一个非常灵活的二维码生成工具。

## 功能概述
你提供一段文本内容，我们为你生成对应的二维码图片。你可以自定义尺寸、前景色、背景色，还支持透明背景，并选择不同的返回格式以适应不同场景。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    text = 'https://www.bilibili.com/video/BV1uT4y1P7CX/' # str | 你希望编码到二维码中的任何文本内容，比如一个URL、一段话或者一个JSON字符串。
    size = 256 # int | 二维码图片的边长（正方形），单位是像素。有效范围是 256 到 2048 之间。 (optional) (default to 256)
    format = image # str | 指定响应内容的格式。可选值为 `image`, `json`, `json_url`。 (optional) (default to image)
    transparent = False # bool | 是否使用透明背景。启用后生成的 PNG 图片将具有 alpha 通道，背景透明。 (optional) (default to False)
    fgcolor = '#000000' # str | 二维码前景色（即二维码本身的颜色），使用十六进制格式。URL 中需要将 `#` 编码为 `%23`。 (optional) (default to '#000000')
    bgcolor = '#FFFFFF' # str | 二维码背景色，使用十六进制格式。当 `transparent=true` 时此参数会被忽略。URL 中需要将 `#` 编码为 `%23`。 (optional) (default to '#FFFFFF')

    try:
        # 生成二维码
        api_response = api_instance.get_image_qrcode(text, size=size, format=format, transparent=transparent, fgcolor=fgcolor, bgcolor=bgcolor)
        print("The response of ImageApi->get_image_qrcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image_qrcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| 你希望编码到二维码中的任何文本内容，比如一个URL、一段话或者一个JSON字符串。 | 
 **size** | **int**| 二维码图片的边长（正方形），单位是像素。有效范围是 256 到 2048 之间。 | [optional] [default to 256]
 **format** | **str**| 指定响应内容的格式。可选值为 &#x60;image&#x60;, &#x60;json&#x60;, &#x60;json_url&#x60;。 | [optional] [default to image]
 **transparent** | **bool**| 是否使用透明背景。启用后生成的 PNG 图片将具有 alpha 通道，背景透明。 | [optional] [default to False]
 **fgcolor** | **str**| 二维码前景色（即二维码本身的颜色），使用十六进制格式。URL 中需要将 &#x60;#&#x60; 编码为 &#x60;%23&#x60;。 | [optional] [default to &#39;#000000&#39;]
 **bgcolor** | **str**| 二维码背景色，使用十六进制格式。当 &#x60;transparent&#x3D;true&#x60; 时此参数会被忽略。URL 中需要将 &#x60;#&#x60; 编码为 &#x60;%23&#x60;。 | [optional] [default to &#39;#FFFFFF&#39;]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 请求成功。响应的格式和内容取决于你传入的 &#x60;format&#x60; 参数。请参考下面不同格式的定义。 |  -  |
**400** | 请求参数错误。请检查 &#x60;text&#x60; 是否提供，&#x60;size&#x60; 是否在有效范围内，&#x60;format&#x60; 是否为支持的值。 |  -  |
**500** | 服务器内部错误。在生成二维码的过程中发生了未知错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_tobase64**
> GetImageTobase64200Response get_image_tobase64(url)

图片转 Base64

看到一张网上的图片，想把它转换成 Base64 编码以便嵌入到你的 HTML 或 CSS 中？用这个接口就对了。

## 功能概述
你提供一个公开可访问的图片 URL，我们帮你把它下载下来，并转换成包含 MIME 类型的 Base64 Data URI 字符串返回给你。

### Example


```python
import uapi
from uapi.models.get_image_tobase64200_response import GetImageTobase64200Response
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
    api_instance = uapi.ImageApi(api_client)
    url = 'https://ts3.tc.mm.bing.net/th?id=ORMS.44196851bb1757ec3f66572811fe8e07&pid=Wdp&w=612&h=304&qlt=90&c=1&rs=1&dpr=1.25&p=0' # str | 需要转换为Base64的、可公开访问的图片URL地址。

    try:
        # 图片转 Base64
        api_response = api_instance.get_image_tobase64(url)
        print("The response of ImageApi->get_image_tobase64:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_image_tobase64: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 需要转换为Base64的、可公开访问的图片URL地址。 | 

### Return type

[**GetImageTobase64200Response**](GetImageTobase64200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 转换成功！返回包含Base64编码的JSON对象。 |  -  |
**400** | 请求参数错误。请检查你是否提供了 &#x60;url&#x60; 参数，以及它是否是一个合法的URL格式。 |  -  |
**502** | 获取图片失败。我们无法从你提供的URL下载图片。请检查该URL是否可以公开访问，以及它是否指向一个有效的图片资源。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_compress**
> bytearray post_image_compress(file, level=level, format=format)

无损压缩图片

还在为图片体积和加载速度发愁吗？体验一下我们强大的**无损压缩服务**，它能在几乎不牺牲任何肉眼可感知的画质的前提下，将图片体积压缩到极致。

## 功能概述
你只需要上传一张常见的图片（如 PNG, JPG），选择一个压缩等级，就能获得一个体积小到惊人的压缩文件。这对于需要大量展示高清图片的网站、App 或小程序来说，是优化用户体验、节省带宽和存储成本的利器。

## 使用须知
> [!TIP]
> 图片越大或压缩等级越高，处理时间可能越长，请您耐心等待。

> [!WARNING]
> **处理时间提醒**
> 在访问量较高时，处理时间可能进一步延长。如果您的业务对返回时间比较敏感，建议预留充足的处理时间。

### 请求与响应格式
- 请求必须使用 `multipart/form-data` 格式上传文件。
- 成功响应将直接返回压缩后的文件二进制流 (`image/*`)，并附带 `Content-Disposition` 头，建议客户端根据此头信息保存文件。

## 参数详解
### `level` (压缩等级)
这是一个从 `1` 到 `5` 的整数，它决定了压缩的强度和策略，数字越小，压缩率越高。所有等级都经过精心调校，以在最大化压缩率的同时保证出色的视觉质量。
- `1`: **极限压缩** (推荐，体积最小，画质优异)
- `2`: **高效压缩**
- `3`: **智能均衡** (默认选项)
- `4`: **画质优先**
- `5`: **专业保真** (压缩率稍低，保留最多图像信息)

## 错误处理指南
- **400 Bad Request**: 通常因为没有上传文件，或者 `level` 参数不在 1-5 的范围内。
- **500 Internal Server Error**: 如果在压缩过程中服务器发生内部错误，会返回此状态码。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    file = None # bytearray | 支持PNG, JPG, JPEG等常见图片格式。文件大小不超过15MB。
    level = 3 # int | 压缩强度 (1-5)，默认为 3。数字越小，压缩率越高。 (optional) (default to 3)
    format = png # str | 输出图片格式，可以是 'png' 或 'jpeg'。 (optional) (default to png)

    try:
        # 无损压缩图片
        api_response = api_instance.post_image_compress(file, level=level, format=format)
        print("The response of ImageApi->post_image_compress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_compress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| 支持PNG, JPG, JPEG等常见图片格式。文件大小不超过15MB。 | 
 **level** | **int**| 压缩强度 (1-5)，默认为 3。数字越小，压缩率越高。 | [optional] [default to 3]
 **format** | **str**| 输出图片格式，可以是 &#39;png&#39; 或 &#39;jpeg&#39;。 | [optional] [default to png]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 压缩成功响应。响应是压缩后的图片二进制数据。返回格式会依据你选择的目标格式变化，默认是 PNG 图片数据。 |  * Content-Disposition - 提示客户端文件下载为压缩后的文件。建议扩展名与输出格式一致。 <br>  |
**400** | 请求无效。可能是未上传文件、文件格式不受支持或参数错误。 |  -  |
**500** | 服务器内部错误。压缩过程中发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_decode**
> bytearray post_image_decode(width=width, height=height, max_width=max_width, max_height=max_height, format=format, color_mode=color_mode, fit=fit, background=background, file=file, url=url)

解码并缩放图片

在 RAM 和 Flash 极其有限的设备上解码图片是一项繁重的任务。这个接口专为 IoT 和嵌入式开发设计，将复杂的图像解码和缩放操作转移到云端，直接输出适用于单片机屏幕的二进制像素流。

## 功能概述
此接口提供了灵活的云端图像预处理能力，帮助硬件开发者跳过繁琐的图像处理逻辑：
- **直接推流渲染**：如果选择输出纯像素流（如 RGB565），单片机收到网络数据后无需解析文件头，可直接将其写入显存，实现极低内存占用的边下边播。
- **完美适配屏幕**：无需在设备端编写裁剪或补边代码。只需传入目标屏幕的物理分辨率，接口会自动完成等比缩放、居中补色或铺满裁剪，确保最终显示画面不变形。
- **精准内存分配**：在动态缩放图片的场景下，服务端会在 HTTP 响应头中提前注入 `X-Image-Width` 和 `X-Image-Height`，方便设备在读取真实的二进制数据前进行准确的内存分配。

## 使用须知
- **请求格式**：无论是上传本地文件还是传递图片链接，请求体都必须使用 `multipart/form-data` 编码格式。
- **网络资源获取**：当您选择传递图片链接时，服务端会自动尝试获取该资源。请确保您提供的图片链接是公网直接可访问的，且不需要任何形式的登录鉴权。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    width = 56 # int | 目标宽度，单位是像素。可以单独传，也可以和 `height` 一起传。与 `max_width`、`max_height` 互斥。 (optional)
    height = 56 # int | 目标高度，单位是像素。可以单独传，也可以和 `width` 一起传。与 `max_width`、`max_height` 互斥。 (optional)
    max_width = 56 # int | 最大宽度，单位是像素。只有在不传 `width`、`height` 时才生效，会按原比例缩放。 (optional)
    max_height = 56 # int | 最大高度，单位是像素。只有在不传 `width`、`height` 时才生效，会按原比例缩放。 (optional)
    format = bmp # str | 输出格式。可以传 `bmp`、`rgb565` 或 `rgb888`，不传时默认是 `bmp`。 (optional) (default to bmp)
    color_mode = RGB888 # str | BMP 输出的颜色模式。只有在 `format=bmp` 时才生效，可以传 `RGB565` 或 `RGB888`，不传时默认是 `RGB888`。 (optional) (default to RGB888)
    fit = contain # str | 缩放模式。可以传 `contain`、`cover` 或 `fill`，不传时默认是 `contain`。当传 `cover` 或 `fill` 时，`width` 和 `height` 都要传。 (optional) (default to contain)
    background = 'black' # str | 背景色。可以传 `black`、`white` 或 `#RRGGBB`，不传时默认是 `black`。 (optional) (default to 'black')
    file = None # bytearray | 要处理的图片文件。这个接口适合直接上传 JPG、JPEG、PNG、WebP、BMP 等常见格式。 (optional)
    url = 'url_example' # str | 要处理的图片链接。适合不方便直接上传文件时使用。 (optional)

    try:
        # 解码并缩放图片
        api_response = api_instance.post_image_decode(width=width, height=height, max_width=max_width, max_height=max_height, format=format, color_mode=color_mode, fit=fit, background=background, file=file, url=url)
        print("The response of ImageApi->post_image_decode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_decode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**| 目标宽度，单位是像素。可以单独传，也可以和 &#x60;height&#x60; 一起传。与 &#x60;max_width&#x60;、&#x60;max_height&#x60; 互斥。 | [optional] 
 **height** | **int**| 目标高度，单位是像素。可以单独传，也可以和 &#x60;width&#x60; 一起传。与 &#x60;max_width&#x60;、&#x60;max_height&#x60; 互斥。 | [optional] 
 **max_width** | **int**| 最大宽度，单位是像素。只有在不传 &#x60;width&#x60;、&#x60;height&#x60; 时才生效，会按原比例缩放。 | [optional] 
 **max_height** | **int**| 最大高度，单位是像素。只有在不传 &#x60;width&#x60;、&#x60;height&#x60; 时才生效，会按原比例缩放。 | [optional] 
 **format** | **str**| 输出格式。可以传 &#x60;bmp&#x60;、&#x60;rgb565&#x60; 或 &#x60;rgb888&#x60;，不传时默认是 &#x60;bmp&#x60;。 | [optional] [default to bmp]
 **color_mode** | **str**| BMP 输出的颜色模式。只有在 &#x60;format&#x3D;bmp&#x60; 时才生效，可以传 &#x60;RGB565&#x60; 或 &#x60;RGB888&#x60;，不传时默认是 &#x60;RGB888&#x60;。 | [optional] [default to RGB888]
 **fit** | **str**| 缩放模式。可以传 &#x60;contain&#x60;、&#x60;cover&#x60; 或 &#x60;fill&#x60;，不传时默认是 &#x60;contain&#x60;。当传 &#x60;cover&#x60; 或 &#x60;fill&#x60; 时，&#x60;width&#x60; 和 &#x60;height&#x60; 都要传。 | [optional] [default to contain]
 **background** | **str**| 背景色。可以传 &#x60;black&#x60;、&#x60;white&#x60; 或 &#x60;#RRGGBB&#x60;，不传时默认是 &#x60;black&#x60;。 | [optional] [default to &#39;black&#39;]
 **file** | **bytearray**| 要处理的图片文件。这个接口适合直接上传 JPG、JPEG、PNG、WebP、BMP 等常见格式。 | [optional] 
 **url** | **str**| 要处理的图片链接。适合不方便直接上传文件时使用。 | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/bmp, application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 处理成功，直接返回图片二进制数据。&#x60;format&#x3D;bmp&#x60; 时返回 BMP 图片数据，&#x60;format&#x3D;rgb565&#x60; 或 &#x60;rgb888&#x60; 时返回原始二进制像素数据。 |  * X-Image-Width - 输出图片的实际宽度（像素）。 <br>  * X-Image-Height - 输出图片的实际高度（像素）。 <br>  * X-Output-Format - 本次响应使用的输出格式。 <br>  * X-Color-Mode - 本次响应使用的颜色模式。 <br>  * X-Source-Format - 源图片识别出的格式。 <br>  * X-Byte-Order - 当输出使用 16 位像素数据时返回字节序信息。 <br>  |
**400** | 请求参数不正确，或者传入的文件和链接都不是可处理的图片内容。 |  -  |
**413** | 上传图片体积、拉取到的图片体积、源图片像素，或者输出图片像素超过限制。 |  -  |
**500** | 服务器处理失败，例如图片编码阶段发生错误。 |  -  |
**502** | 图片下载失败，或者图片链接返回的不是可识别的图片内容。 |  -  |
**503** | 当前图片处理任务过多，或者暂时无法获取图片。 |  -  |
**504** | 获取图片超时。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_frombase64**
> PostImageFrombase64200Response post_image_frombase64(post_image_frombase64_request)

通过Base64编码上传图片

当你需要在前端处理完图片（比如裁剪、加滤镜后），不通过传统表单，而是直接上传图片的场景，这个接口就派上用场了。

## 功能概述
你只需要将图片的 Base64 编码字符串发送过来，我们就会把它解码、保存为图片文件，并返回一个可供访问的公开 URL。

## 使用须知

> [!IMPORTANT]
> **关于 `imageData` 格式**
> 你发送的 `imageData` 字符串必须是完整的 Base64 Data URI 格式，它需要包含 MIME 类型信息，例如 `data:image/png;base64,iVBORw0KGgo...`。缺少 `data:image/...;base64,` 前缀将导致解码失败。

### Example


```python
import uapi
from uapi.models.post_image_frombase64200_response import PostImageFrombase64200Response
from uapi.models.post_image_frombase64_request import PostImageFrombase64Request
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
    api_instance = uapi.ImageApi(api_client)
    post_image_frombase64_request = uapi.PostImageFrombase64Request() # PostImageFrombase64Request | 

    try:
        # 通过Base64编码上传图片
        api_response = api_instance.post_image_frombase64(post_image_frombase64_request)
        print("The response of ImageApi->post_image_frombase64:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_frombase64: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_image_frombase64_request** | [**PostImageFrombase64Request**](PostImageFrombase64Request.md)|  | 

### Return type

[**PostImageFrombase64200Response**](PostImageFrombase64200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 上传成功！返回图片的访问地址。 |  -  |
**400** | 请求失败。可能的原因有：请求体不是有效的JSON，缺少 &#x60;imageData&#x60; 字段，或者 &#x60;imageData&#x60; 的内容不是有效的Base64 Data URI。 |  -  |
**500** | 服务器内部错误。在解码或保存图片文件时发生了未知错误。请稍后重试。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_motou**
> bytearray post_image_motou(image_url=image_url, file=file, bg_color=bg_color)

生成摸摸头GIF

除了使用QQ头像，你还可以通过上传自己的图片或提供图片URL来制作独一无二的摸摸头GIF。

## 功能概述
此接口通过POST方法，支持两种方式生成GIF：
1.  **图片URL**：在表单中提供 `image_url` 字段。
2.  **上传图片**：在表单中上传 `file` 文件。

## 使用须知
- **响应格式**：接口成功时直接返回 `image/gif` 格式的二进制数据。
- **参数优先级**：如果同时提供了 `image_url` 和上传的 `file` 文件，系统将 **优先使用 `image_url`**。
- **背景颜色**：同样支持 `bg_color` 表单字段来控制GIF背景。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    image_url = 'image_url_example' # str | 图片的URL地址。如果提供此项，将优先使用该URL的图片。 (optional)
    file = None # bytearray | 上传的图片文件。支持JPG、PNG、GIF等常见格式。 (optional)
    bg_color = 'bg_color_example' # str | GIF的背景颜色。可选值为 'white', 'black', 'transparent'。 (optional)

    try:
        # 生成摸摸头GIF
        api_response = api_instance.post_image_motou(image_url=image_url, file=file, bg_color=bg_color)
        print("The response of ImageApi->post_image_motou:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_motou: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| 图片的URL地址。如果提供此项，将优先使用该URL的图片。 | [optional] 
 **file** | **bytearray**| 上传的图片文件。支持JPG、PNG、GIF等常见格式。 | [optional] 
 **bg_color** | **str**| GIF的背景颜色。可选值为 &#39;white&#39;, &#39;black&#39;, &#39;transparent&#39;。 | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/gif, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 生成成功！响应体是GIF格式的图片二进制数据。 |  -  |
**400** | 请求参数错误。必须提供 &#39;image_url&#39; 或上传 &#39;file&#39; 文件两者中的一个。 |  -  |
**500** | 服务器内部错误。可能的原因包括：从URL获取图片失败、处理上传文件失败，或在生成GIF过程中发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_nsfw**
> PostImageNsfw200Response post_image_nsfw(file=file, url=url)

图片敏感检测

这是一个图片内容审核接口，自动识别图片中的违规内容并返回处理建议。

## 功能概述
上传图片文件或提供图片URL，接口会自动分析图片内容，返回是否违规、风险等级和处理建议。适合对接到用户上传流程中，实现自动化内容审核。

## 返回字段说明
- **is_nsfw**: 是否判定为违规内容，`true` 表示违规，`false` 表示正常
- **nsfw_score**: 违规内容置信度，0-1 之间，越高表示越可能违规
- **normal_score**: 正常内容置信度，0-1 之间，与 nsfw_score 互补
- **suggestion**: 处理建议
  - `pass`: 内容正常，可以直接放行
  - `review`: 存在风险，建议转人工复核
  - `block`: 高风险内容，建议直接拦截
- **risk_level**: 风险等级
  - `low`: 低风险
  - `medium`: 中风险
  - `high`: 高风险
- **label**: 内容标签，`nsfw` 或 `normal`
- **confidence**: 模型对当前判断的整体置信度
- **inference_time_ms**: 模型推理耗时，单位毫秒

### Example


```python
import uapi
from uapi.models.post_image_nsfw200_response import PostImageNsfw200Response
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
    api_instance = uapi.ImageApi(api_client)
    file = None # bytearray | 要检测的图片文件。支持 JPG、JPEG、PNG、GIF、WebP 格式，最大 20MB。 (optional)
    url = 'url_example' # str | 图片的 URL 地址。如果同时提供 file 和 url，将优先使用 file。 (optional)

    try:
        # 图片敏感检测
        api_response = api_instance.post_image_nsfw(file=file, url=url)
        print("The response of ImageApi->post_image_nsfw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_nsfw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| 要检测的图片文件。支持 JPG、JPEG、PNG、GIF、WebP 格式，最大 20MB。 | [optional] 
 **url** | **str**| 图片的 URL 地址。如果同时提供 file 和 url，将优先使用 file。 | [optional] 

### Return type

[**PostImageNsfw200Response**](PostImageNsfw200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 检测成功！返回图片的 NSFW 分析结果。 |  -  |
**400** | 请求参数错误。可能是未提供图片、文件格式不支持或文件过大。 |  -  |
**413** | 文件过大。上传的图片超过了 20MB 的限制。 |  -  |
**500** | 服务器内部错误。在处理图片或进行 NSFW 检测时发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_ocr**
> PostImageOcr200Response post_image_ocr(file=file, url=url, image_base64=image_base64, image_name=image_name, need_location=need_location, return_markdown=return_markdown, enable_cls=enable_cls)

通用 OCR 文字识别

无论您是需要实现票据的自动化录入，还是在网页前端对图片上的文字进行坐标框选，这个高精度的 OCR 接口都能为您提供强大的基础能力。

## 功能概述
> [!IMPORTANT]
> 如果您只关心图片上写了什么（例如截图取字或内容安全审核），强烈建议将 `need_location` 设置为 `false`。这会大幅精简返回的 JSON 数据体积，提升网络传输与系统解析效率。

除了常规的图片转文字，这个接口还针对实际开发场景做了一些实用设计：
- **前端文字高亮与结构化分析**：默认返回每一段文字的矩形坐标和四个顶点坐标。这非常适合使用 Canvas 在原图上画框高亮，或者在后端根据相对位置提取票据中的键值对信息。
- **复杂拍摄环境下的抗畸变**：针对手机拍摄导致的旋转或倾斜，可以开启 `enable_cls=true`。服务端在识别前会自动进行方向预校正，显著提升识别准确率。
- **灵活的输入与请求要求**：接口支持 `file`、`url` 或 `image_base64` 三种方式输入。请确保请求格式为 `multipart/form-data`，且图片链接在公网可直接访问。

### Example


```python
import uapi
from uapi.models.post_image_ocr200_response import PostImageOcr200Response
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
    api_instance = uapi.ImageApi(api_client)
    file = None # bytearray | 待识别的图片文件。支持 JPG、JPEG、PNG、BMP、GIF、WebP 等常见格式，最大不超过 10MB。请勿与 url 或 image_base64 同时提交。 (optional)
    url = 'url_example' # str | 公网可直接访问的图片地址。请勿与 file 或 image_base64 同时提交。 (optional)
    image_base64 = 'image_base64_example' # str | 图片的 Base64 字符串。可以传完整 Data URI，也可以只传纯 Base64 内容。请勿与 file 或 url 同时提交。 (optional)
    image_name = 'image_name_example' # str | 自定义图片文件名。传链接或纯 Base64 时建议一起传，便于保留或推断扩展名。 (optional)
    need_location = true # str | 是否返回文字坐标信息。请传 `true` 或 `false`，不传时默认是 `true`。 (optional) (default to true)
    return_markdown = false # str | 是否额外返回整理后的 Markdown 文本。请传 `true` 或 `false`，不传时默认是 `false`。 (optional) (default to false)
    enable_cls = false # str | 是否开启额外的文字方向校正。请传 `true` 或 `false`，不传时默认是 `false`。 (optional) (default to false)

    try:
        # 通用 OCR 文字识别
        api_response = api_instance.post_image_ocr(file=file, url=url, image_base64=image_base64, image_name=image_name, need_location=need_location, return_markdown=return_markdown, enable_cls=enable_cls)
        print("The response of ImageApi->post_image_ocr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_ocr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| 待识别的图片文件。支持 JPG、JPEG、PNG、BMP、GIF、WebP 等常见格式，最大不超过 10MB。请勿与 url 或 image_base64 同时提交。 | [optional] 
 **url** | **str**| 公网可直接访问的图片地址。请勿与 file 或 image_base64 同时提交。 | [optional] 
 **image_base64** | **str**| 图片的 Base64 字符串。可以传完整 Data URI，也可以只传纯 Base64 内容。请勿与 file 或 url 同时提交。 | [optional] 
 **image_name** | **str**| 自定义图片文件名。传链接或纯 Base64 时建议一起传，便于保留或推断扩展名。 | [optional] 
 **need_location** | **str**| 是否返回文字坐标信息。请传 &#x60;true&#x60; 或 &#x60;false&#x60;，不传时默认是 &#x60;true&#x60;。 | [optional] [default to true]
 **return_markdown** | **str**| 是否额外返回整理后的 Markdown 文本。请传 &#x60;true&#x60; 或 &#x60;false&#x60;，不传时默认是 &#x60;false&#x60;。 | [optional] [default to false]
 **enable_cls** | **str**| 是否开启额外的文字方向校正。请传 &#x60;true&#x60; 或 &#x60;false&#x60;，不传时默认是 &#x60;false&#x60;。 | [optional] [default to false]

### Return type

[**PostImageOcr200Response**](PostImageOcr200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 识别成功，返回统一的 OCR 结果对象。默认会带坐标信息；当 &#x60;need_location&#x3D;false&#x60; 时，坐标相关字段会省略。 |  -  |
**400** | 请求参数不正确，比如没有传图片来源、提交了多重图片来源，或者布尔参数和 Base64 格式不合法。 |  -  |
**413** | 图片大小超过当前限制。 |  -  |
**415** | 上传内容不是可识别的常见图片格式。 |  -  |
**502** | 识别处理失败，请稍后重试。 |  -  |
**503** | 文字识别服务暂时不可用，请稍后再试。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_speechless**
> bytearray post_image_speechless(post_image_speechless_request)

生成你们怎么不说话了表情包

你们怎么不说话了？是不是都在偷偷玩Uapi，求求你们不要玩Uapi了

## 使用须知
- **响应格式**：接口成功时直接返回 `image/png` 格式的二进制数据。
- **文字内容**：至少需要提供 `top_text`（上方文字）或 `bottom_text`（下方文字）之一。
- **梗图逻辑**：上方描述某个行为，下方通常以「们」开头表示劝阻，形成戏谑的对比效果。

### Example


```python
import uapi
from uapi.models.post_image_speechless_request import PostImageSpeechlessRequest
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
    api_instance = uapi.ImageApi(api_client)
    post_image_speechless_request = uapi.PostImageSpeechlessRequest() # PostImageSpeechlessRequest | 包含表情包文字内容的JSON对象。至少需要提供上方或下方文字之一。

    try:
        # 生成你们怎么不说话了表情包
        api_response = api_instance.post_image_speechless(post_image_speechless_request)
        print("The response of ImageApi->post_image_speechless:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_speechless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_image_speechless_request** | [**PostImageSpeechlessRequest**](PostImageSpeechlessRequest.md)| 包含表情包文字内容的JSON对象。至少需要提供上方或下方文字之一。 | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 生成成功！响应体是PNG格式的表情包图片二进制数据。 |  -  |
**400** | 请求参数错误。必须提供 &#39;top_text&#39; 或 &#39;bottom_text&#39; 至少其中之一。 |  -  |
**500** | 服务器内部错误。在生成表情包图片过程中发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_svg**
> bytearray post_image_svg(format=format, width=width, height=height, quality=quality, file=file)

SVG转图片

需要将灵活的 SVG 矢量图形转换为常见的光栅图像格式吗？这个接口可以帮你轻松实现。

## 功能概述
上传一个 SVG 文件，并指定目标格式（如 PNG、JPEG 等），接口将返回转换后的图像。你还可以调整输出图像的尺寸和（对于JPEG）压缩质量，以满足不同场景的需求。

### Example


```python
import uapi
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
    api_instance = uapi.ImageApi(api_client)
    format = png # str | 输出图像的目标格式。支持的值：`png`, `jpeg`, `jpg`, `gif`, `tiff`, `bmp`。 (optional) (default to png)
    width = 56 # int | 输出图像的宽度（像素）。如果省略，将根据 `height` 保持宽高比，或者使用 SVG 的原始宽度。 (optional)
    height = 56 # int | 输出图像的高度（像素）。如果省略，将根据 `width` 保持宽高比，或者使用 SVG 的原始高度。 (optional)
    quality = 90 # int | JPEG 图像的压缩质量（1-100）。仅当 `format` 为 `jpeg` 或 `jpg` 时有效。 (optional) (default to 90)
    file = None # bytearray | 支持SVG文件 (optional)

    try:
        # SVG转图片
        api_response = api_instance.post_image_svg(format=format, width=width, height=height, quality=quality, file=file)
        print("The response of ImageApi->post_image_svg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->post_image_svg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| 输出图像的目标格式。支持的值：&#x60;png&#x60;, &#x60;jpeg&#x60;, &#x60;jpg&#x60;, &#x60;gif&#x60;, &#x60;tiff&#x60;, &#x60;bmp&#x60;。 | [optional] [default to png]
 **width** | **int**| 输出图像的宽度（像素）。如果省略，将根据 &#x60;height&#x60; 保持宽高比，或者使用 SVG 的原始宽度。 | [optional] 
 **height** | **int**| 输出图像的高度（像素）。如果省略，将根据 &#x60;width&#x60; 保持宽高比，或者使用 SVG 的原始高度。 | [optional] 
 **quality** | **int**| JPEG 图像的压缩质量（1-100）。仅当 &#x60;format&#x60; 为 &#x60;jpeg&#x60; 或 &#x60;jpg&#x60; 时有效。 | [optional] [default to 90]
 **file** | **bytearray**| 支持SVG文件 | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 转换成功！响应体是转换后图像的二进制数据。 |  -  |
**400** | 请求无效。可能是未上传文件或指定了不支持的输出格式。 |  -  |
**500** | 服务器内部错误。SVG 渲染或文件处理过程中发生错误。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

