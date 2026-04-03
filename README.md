# uapi-sdk-python

![Banner](https://raw.githubusercontent.com/AxT-Team/uapi-sdk-python/main/banner.png)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Docs](https://img.shields.io/badge/Docs-uapis.cn-2EAE5D?style=flat-square)](https://uapis.cn/)
[![PyPI](https://img.shields.io/pypi/v/uapi-sdk-python?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/uapi-sdk-python/)

> [!NOTE]
> 所有接口的 Python 示例都可以在 [UApi](https://uapis.cn/docs/introduction) 的接口文档页面，向下滚动至 **快速启动** 区块后直接复制。

## 快速开始

```bash
pip install uapi-sdk-python
```

```python
from uapi import UapiClient

client = UapiClient("https://uapis.cn", "YOUR_API_KEY")
result = client.misc.get_misc_hotboard(type="weibo")
print(result)
```

这个接口默认只要传 `type` 就可以拿当前热榜。`time`、`keyword`、`time_start`、`time_end`、`limit`、`sources` 都是按场景再传的可选参数。

> [!TIP]
> 请使用与运行脚本相同的 Python 解释器安装依赖，例如执行 `python -m pip install uapi-sdk-python` 后再运行 `python main.py`。在 VS Code / Pyright 中若提示 “Import uapi could not be resolved”，将解释器切换到当前虚拟环境即可恢复补全。

## 特性

现在你不再需要反反复复的查阅文档了。

只需在 IDE 中键入 `client.`，所有核心模块——如 `social`、`game`、`image`——即刻同步展现。进一步输入即可直接定位到 `get_social_qq_userinfo` 这样的具体方法，其名称与文档的 `operationId` 严格保持一致，确保了开发过程的直观与高效。

所有方法签名只接受真实且必需的参数。当你在构建请求时，IDE 会即时提示 `qq`、`username` 等键名，这彻底杜绝了在 `dict`/关键字参数中因拼写错误而导致的运行时错误。

针对 401、404、429 等标准 HTTP 响应，SDK 已将其统一映射为具名的异常类型。这些异常均附带 `code`、`status`、`details` 等关键上下文信息，确保你在日志中能第一时间准确、快速地诊断问题。

`UapiClient(base_url, token, timeout)` 默认使用 `httpx` 并自动追加 `Authorization` 头；需要切换环境或调整超时时，只要改一次构造参数即可。

如果你需要查看字段细节或内部逻辑，仓库中的 `./internal` 目录同步保留了由 `openapi-generator` 生成的完整结构体，随时可供参考。

## 响应元信息

每次请求完成后，SDK 会自动把响应 Header 解析成结构化的 `ResponseMeta`，你不用自己拆原始字符串。

成功时可以通过 `client.last_response_meta` 读取，失败时可以通过 `err.meta` 读取，两条路径拿到的是同一套字段。

```python
from uapi import UapiClient, UapiError

client = UapiClient("https://uapis.cn", "YOUR_API_KEY")

# 成功路径
client.social.get_social_qq_userinfo(qq="10001")
meta = client.last_response_meta
if meta:
    print("这次请求原价:", meta.credits_requested or 0, "积分")
    print("这次实际扣费:", meta.credits_charged or 0, "积分")
    print("特殊计价:", meta.credits_pricing or "原价")
    print("余额剩余:", meta.balance_remaining_cents or 0, "分")
    print("资源包剩余:", meta.quota_remaining_credits or 0, "积分")
    print("当前有效额度桶:", meta.active_quota_buckets or 0)
    print("额度用空即停:", meta.stop_on_empty)
    print("Key QPS:", meta.billing_key_rate_remaining or 0, "/", meta.billing_key_rate_limit or 0, meta.billing_key_rate_unit or "req")
    print("Request ID:", meta.request_id)

# 失败路径
try:
    client.social.get_social_qq_userinfo(qq="10001")
except UapiError as err:
    if err.meta:
        print("Retry-After 秒数:", err.meta.retry_after_seconds)
        print("Retry-After 原始值:", err.meta.retry_after_raw)
        print("访客 QPS:", err.meta.visitor_rate_remaining or 0, "/", err.meta.visitor_rate_limit or 0)
        print("Request ID:", err.meta.request_id)
```

常用字段一览：

| 字段 | 说明 |
|------|------|
| `credits_requested` | 这次请求原本要扣多少积分，也就是请求价 |
| `credits_charged` | 这次请求实际扣了多少积分 |
| `credits_pricing` | 特殊计价原因，例如缓存半价 `cache-hit-half-price` |
| `balance_remaining_cents` | 账户余额剩余（分） |
| `quota_remaining_credits` | 资源包剩余积分 |
| `active_quota_buckets` | 当前还有多少个有效额度桶参与计费 |
| `stop_on_empty` | 额度耗尽后是否直接停止服务 |
| `retry_after_seconds` / `retry_after_raw` | 限流后的等待时长；当服务端返回 HTTP 时间字符串时看 `retry_after_raw` |
| `request_id` | 请求唯一 ID，排障时使用 |
| `billing_key_rate_limit` / `billing_key_rate_remaining` | Billing Key 当前 QPS 规则的上限与剩余 |
| `billing_ip_rate_limit` / `billing_ip_rate_remaining` | Billing Key 单 IP 当前 QPS 规则的上限与剩余 |
| `visitor_rate_limit` / `visitor_rate_remaining` | 访客当前 QPS 规则的上限与剩余 |
| `rate_limit_policies` / `rate_limits` | 完整结构化限流策略数据 |

## 进阶实践

### 缓存与幂等

```python
from functools import lru_cache
from uapi import UapiClient

client = UapiClient("https://uapis.cn", token="YOUR_API_KEY")

@lru_cache(maxsize=128)
def cached_lookup(qq: str):
    return client.social.get_social_qq_userinfo(qq=qq)

user = cached_lookup("10001")
```

也可以在 FastAPI / Django 项目里配合 Redis，将 SDK 的响应序列化后写入缓存，命中即直接返回。

### 调整超时与环境

```python
from uapi import UapiClient

client = UapiClient(
    "https://uapis.cn",
    token="YOUR_API_KEY",
    timeout=5.0,
)
```

如果你需要切换到别的环境，直接改 `base_url` 就可以；如果你只想缩短等待时间，传 `timeout` 就够了。

## 错误模型概览

| HTTP 状态码 | SDK 错误类型                                  | 附加信息                                                                          |
|-------------|----------------------------------------------|------------------------------------------------------------------------------------|
| 401/403     | `UnauthorizedError`                          | `code`、`status`                                                                   |
| 404         | `NotFoundError` / `NoMatchError`             | `code`、`status`                                                                   |
| 400         | `InvalidParameterError` / `InvalidParamsError` | `code`、`status`、`details`                                                        |
| 429         | `ServiceBusyError`                           | `code`、`status`、`retry_after_seconds`（用于决定何时重试）                        |
| 5xx         | `InternalServerErrorError` / `ApiErrorError` | `code`、`status`、`details`                                                        |
| 其他 4xx    | `UapiError`                                  | `code`、`status`、`details`                                                        |

## 其他 SDK

| 语言        | 仓库地址                                                     |
|-------------|--------------------------------------------------------------|
| Go          | https://github.com/AxT-Team/uapi-sdk-go                      |
| Python（当前）      | https://github.com/AxT-Team/uapi-sdk-python                  |
| TypeScript| https://github.com/AxT-Team/uapi-sdk-typescript           |
| Browser (TypeScript/JavaScript)| https://github.com/AxT-Team/uapi-browser-sdk        |
| Java        | https://github.com/AxT-Team/uapi-sdk-java                    |
| PHP         | https://github.com/AxT-Team/uapi-sdk-php                     |
| C#          | https://github.com/AxT-Team/uapi-sdk-csharp                  |
| C++         | https://github.com/AxT-Team/uapi-sdk-cpp                     |
| Rust        | https://github.com/AxT-Team/uapi-sdk-rust                    |

## 文档

访问 [UApi文档首页](https://uapis.cn/docs/introduction) 并选择任意接口，向下滚动到 **快速启动** 区块即可看到最新的 Python 示例代码。


