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

client = UapiClient("https://uapis.cn/api/v1")
result = client.social.get_social_qq_userinfo(qq="10001")
print(result)
```

> [!TIP]
> 请使用与运行脚本相同的 Python 解释器安装依赖，例如执行 `python -m pip install uapi-sdk-python` 后再运行 `python main.py`。在 VS Code / Pyright 中若提示 “Import uapi could not be resolved”，将解释器切换到当前虚拟环境即可恢复补全。

## 特性

现在你不再需要反反复复的查阅文档了。

只需在 IDE 中键入 `client.`，所有核心模块——如 `social`、`game`、`image`——即刻同步展现。进一步输入即可直接定位到 `get_social_qq_userinfo` 这样的具体方法，其名称与文档的 `operationId` 严格保持一致，确保了开发过程的直观与高效。

所有方法签名只接受真实且必需的参数。当你在构建请求时，IDE 会即时提示 `qq`、`username` 等键名，这彻底杜绝了在 `dict`/关键字参数中因拼写错误而导致的运行时错误。

针对 401、404、429 等标准 HTTP 响应，SDK 已将其统一映射为具名的异常类型。这些异常均附带 `code`、`status`、`details` 等关键上下文信息，确保你在日志中能第一时间准确、快速地诊断问题。

`UapiClient(base_url, token, timeout)` 默认使用 `httpx` 并自动追加 `Authorization` 头；需要切换环境或调整超时时，只要改一次构造参数即可。

如果你需要查看字段细节或内部逻辑，仓库中的 `./internal` 目录同步保留了由 `openapi-generator` 生成的完整结构体，随时可供参考。

## 进阶实践

### 缓存与幂等

```python
from functools import lru_cache
from uapi import UapiClient

client = UapiClient("https://uapis.cn/api/v1", token="<TOKEN>")

@lru_cache(maxsize=128)
def cached_lookup(qq: str):
    return client.social.get_social_qq_userinfo(qq=qq)

user = cached_lookup("10001")
```

也可以在 FastAPI / Django 项目里配合 Redis，将 SDK 的响应序列化后写入缓存，命中即直接返回。

### 注入自定义 httpx.Client

```python
import httpx
from httpx import Auth
from uapi import UapiClient

class StaticToken(Auth):
    def __init__(self, token: str):
        self.token = token
    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        yield request

http_client = httpx.Client(
    timeout=5,
    transport=httpx.HTTPTransport(retries=3),
    event_hooks={"request": [lambda request: print("->", request.url)]},
)

client = UapiClient(
    "https://uapis.cn/api/v1",
    client=http_client,
    auth=StaticToken("<TOKEN>"),
)
```

通过自定义 `client` / `transport` / `auth`，可以无缝植入代理、重试策略或 APM 埋点。

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


