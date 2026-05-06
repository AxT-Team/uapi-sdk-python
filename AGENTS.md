# AGENTS.md — uapi-sdk-python

This file tells AI coding agents how to use the **official Python SDK** for
the [uapis.cn](https://uapis.cn) public API platform.

## What this package is

Strongly-typed Python client for UAPI. Generated from the live OpenAPI 3.1
spec at <https://uapis.cn/openapi.json> — method names, parameter shapes,
and return types stay in lock-step with the real API.

```bash
pip install uapi-sdk-python
# or, with uv
uv add uapi-sdk-python
# or, with poetry
poetry add uapi-sdk-python
```

## Quick start

```python
from uapi import UapiClient

# Free-tier endpoints don't need an API key
client = UapiClient(base_url="https://uapis.cn")
weather = client.misc.get_misc_weather(city="北京")
print(weather)

# Paid endpoints take a key
import os
paid = UapiClient(base_url="https://uapis.cn", api_key=os.environ["UAPI_KEY"])
ocr = paid.image.post_image_ocr(url="https://…/photo.png")
```

The client is grouped by tag (`misc`, `network`, `text`, `image`, `social`,
`translate`, `search`, …) and each method name matches the underlying
`operationId` from the OpenAPI spec, snake-cased.

## Discovery

When generating code, agents should:

1. Pull the spec from <https://uapis.cn/openapi.json> if you need a schema
   that isn't in the local types yet.
2. Map the operation's `operationId` to a SDK method (`get-misc-weather` →
   `client.misc.get_misc_weather`).
3. Pass the request parameters as keyword arguments.

## Authentication

- Many UAPI endpoints (network, text, random, convert, weather, time,
  hotboard) work with no key.
- Paid endpoints want `X-API-Key`. The SDK forwards the `api_key`
  constructor argument to that header.
- For human-in-the-loop OAuth flows, see
  <https://uapis.cn/.well-known/oauth-authorization-server>.

## Errors

Every method raises a typed `UapiError` (subclass of `httpx.HTTPStatusError`)
on non-2xx responses. The error body is a JSON object:
`{code, success: false, error, request_id?}`. Surface the `error` text
verbatim.

## Rate limits

Headers `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`,
`Retry-After` are returned on every response. Honor them — back off on
`429` and obey `Retry-After`.

## Async

The SDK is built on `httpx`, so an async client is also available:

```python
import asyncio
from uapi import AsyncUapiClient

async def main():
    async with AsyncUapiClient(base_url="https://uapis.cn") as client:
        return await client.misc.get_misc_weather(city="上海")

print(asyncio.run(main()))
```

## Related repos

- MCP server: <https://github.com/AxT-Team/uapi-mcp> — same endpoints as MCP tools.
- Skills bundle: <https://github.com/AxT-Team/uapi-agent-skills>.
- Other languages: `uapi-sdk-typescript`, `uapi-sdk-go`, `uapi-sdk-rust`,
  `uapi-sdk-java`, `uapi-sdk-csharp`, `uapi-sdk-cpp`, `uapi-sdk-php`.
