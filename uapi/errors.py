from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, Mapping, Optional
import httpx

@dataclass
class RateLimitPolicyEntry:
    name: str
    quota: Optional[int] = None
    unit: Optional[str] = None
    window_seconds: Optional[int] = None

@dataclass
class RateLimitStateEntry:
    name: str
    remaining: Optional[int] = None
    unit: Optional[str] = None
    reset_after_seconds: Optional[int] = None

@dataclass
class ResponseMeta:
    request_id: Optional[str] = None
    retry_after_seconds: Optional[int] = None
    debit_status: Optional[str] = None
    credits_requested: Optional[int] = None
    credits_charged: Optional[int] = None
    credits_pricing: Optional[str] = None
    active_quota_buckets: Optional[int] = None
    stop_on_empty: Optional[bool] = None
    rate_limit_policy_raw: Optional[str] = None
    rate_limit_raw: Optional[str] = None
    rate_limit_policies: Dict[str, RateLimitPolicyEntry] = field(default_factory=dict)
    rate_limits: Dict[str, RateLimitStateEntry] = field(default_factory=dict)
    balance_limit_cents: Optional[int] = None
    balance_remaining_cents: Optional[int] = None
    quota_limit_credits: Optional[int] = None
    quota_remaining_credits: Optional[int] = None
    visitor_quota_limit_credits: Optional[int] = None
    visitor_quota_remaining_credits: Optional[int] = None
    raw_headers: Dict[str, str] = field(default_factory=dict)

class UapiError(Exception):
    code: str
    status: int
    message: str
    details: Any
    payload: Any
    meta: Optional[ResponseMeta]

    def __init__(
        self,
        code: str,
        status: int,
        message: str,
        details: Any = None,
        payload: Any = None,
        meta: Optional[ResponseMeta] = None,
    ):
        super().__init__(f"[{status}] {code}: {message}")
        self.code = code
        self.status = status
        self.message = message
        self.details = details
        self.payload = payload
        self.meta = meta


class ApiErrorError(UapiError):
    """上游/内部错误 (API_ERROR)"""
    DEFAULT_STATUS = 502

class AvatarNotFoundError(UapiError):
    """头像未找到 (AVATAR_NOT_FOUND)"""
    DEFAULT_STATUS = 404

class ConversionFailedError(UapiError):
    """转换失败 (CONVERSION_FAILED)"""
    DEFAULT_STATUS = 400

class FileOpenErrorError(UapiError):
    """文件打开错误 (FILE_OPEN_ERROR)"""
    DEFAULT_STATUS = 500

class FileRequiredError(UapiError):
    """文件必需 (FILE_REQUIRED)"""
    DEFAULT_STATUS = 400

class InsufficientCreditsError(UapiError):
    """账户积分不足 (INSUFFICIENT_CREDITS)"""
    DEFAULT_STATUS = 402

class InternalServerErrorError(UapiError):
    """服务器内部错误 (INTERNAL_SERVER_ERROR)"""
    DEFAULT_STATUS = 500

class InvalidParameterError(UapiError):
    """请求参数错误 (INVALID_PARAMETER)"""
    DEFAULT_STATUS = 400

class InvalidParamsError(UapiError):
    """无效参数 (INVALID_PARAMS)"""
    DEFAULT_STATUS = 400

class NotFoundError(UapiError):
    """资源不存在 (NOT_FOUND)"""
    DEFAULT_STATUS = 404

class NoMatchError(UapiError):
    """无匹配 (NO_MATCH)"""
    DEFAULT_STATUS = 404

class NoTrackingDataError(UapiError):
    """无物流数据 (NO_TRACKING_DATA)"""
    DEFAULT_STATUS = 404

class PhoneInfoFailedError(UapiError):
    """手机号信息查询失败 (PHONE_INFO_FAILED)"""
    DEFAULT_STATUS = 500

class RecognitionFailedError(UapiError):
    """识别失败 (RECOGNITION_FAILED)"""
    DEFAULT_STATUS = 404

class RequestEntityTooLargeError(UapiError):
    """错误 (REQUEST_ENTITY_TOO_LARGE)"""
    DEFAULT_STATUS = 413

class ServiceBusyError(UapiError):
    """请求过于频繁 (SERVICE_BUSY)"""
    DEFAULT_STATUS = 429

class TimezoneNotFoundError(UapiError):
    """时区未找到 (TIMEZONE_NOT_FOUND)"""
    DEFAULT_STATUS = 404

class UnauthorizedError(UapiError):
    """请求未授权 (UNAUTHORIZED)"""
    DEFAULT_STATUS = 401

class UnsupportedCarrierError(UapiError):
    """不支持的承运商 (UNSUPPORTED_CARRIER)"""
    DEFAULT_STATUS = 404

class UnsupportedFormatError(UapiError):
    """格式不支持 (UNSUPPORTED_FORMAT)"""
    DEFAULT_STATUS = 400

class VisitorMonthlyQuotaExhaustedError(UapiError):
    """访客月度免费额度已用尽 (VISITOR_MONTHLY_QUOTA_EXHAUSTED)"""
    DEFAULT_STATUS = 429


def _default_code(status: int) -> str:
    if status == 400:
        return "INVALID_PARAMETER"
    if status == 401:
        return "UNAUTHORIZED"
    if status == 402:
        return "INSUFFICIENT_CREDITS"
    if status == 404:
        return "NOT_FOUND"
    if status == 413:
        return "REQUEST_ENTITY_TOO_LARGE"
    if status == 429:
        return "SERVICE_BUSY"
    if status >= 500:
        return "INTERNAL_SERVER_ERROR"
    return "API_ERROR"

def _parse_int(value: Optional[str]) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

def _parse_bool(value: Optional[str]) -> Optional[bool]:
    if value is None:
        return None
    lowered = value.strip().lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return None

def _unquote(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text

def _parse_structured_items(raw: Optional[str]) -> list[tuple[str, Dict[str, str]]]:
    if not raw:
        return []
    items: list[tuple[str, Dict[str, str]]] = []
    for chunk in [part.strip() for part in raw.split(",") if part.strip()]:
        segments = [segment.strip() for segment in chunk.split(";") if segment.strip()]
        if not segments:
            continue
        name = _unquote(segments[0])
        params: Dict[str, str] = {}
        for segment in segments[1:]:
            if "=" not in segment:
                continue
            key, value = segment.split("=", 1)
            params[key.strip()] = _unquote(value)
        items.append((name, params))
    return items

def extract_meta(headers: Mapping[str, str]) -> ResponseMeta:
    raw_headers = {str(key).lower(): str(value) for key, value in headers.items()}
    rate_limit_policies: Dict[str, RateLimitPolicyEntry] = {}
    rate_limits: Dict[str, RateLimitStateEntry] = {}

    for name, params in _parse_structured_items(raw_headers.get("ratelimit-policy")):
        rate_limit_policies[name] = RateLimitPolicyEntry(
            name=name,
            quota=_parse_int(params.get("q")),
            unit=params.get("uapi-unit"),
            window_seconds=_parse_int(params.get("w")),
        )

    for name, params in _parse_structured_items(raw_headers.get("ratelimit")):
        rate_limits[name] = RateLimitStateEntry(
            name=name,
            remaining=_parse_int(params.get("r")),
            unit=params.get("uapi-unit"),
            reset_after_seconds=_parse_int(params.get("t")),
        )

    return ResponseMeta(
        request_id=raw_headers.get("x-request-id"),
        retry_after_seconds=_parse_int(raw_headers.get("retry-after")),
        debit_status=raw_headers.get("uapi-debit-status"),
        credits_requested=_parse_int(raw_headers.get("uapi-credits-requested")),
        credits_charged=_parse_int(raw_headers.get("uapi-credits-charged")),
        credits_pricing=raw_headers.get("uapi-credits-pricing"),
        active_quota_buckets=_parse_int(raw_headers.get("uapi-quota-active-buckets")),
        stop_on_empty=_parse_bool(raw_headers.get("uapi-stop-on-empty")),
        rate_limit_policy_raw=raw_headers.get("ratelimit-policy"),
        rate_limit_raw=raw_headers.get("ratelimit"),
        rate_limit_policies=rate_limit_policies,
        rate_limits=rate_limits,
        balance_limit_cents=rate_limit_policies.get("billing-balance").quota if "billing-balance" in rate_limit_policies else None,
        balance_remaining_cents=rate_limits.get("billing-balance").remaining if "billing-balance" in rate_limits else None,
        quota_limit_credits=rate_limit_policies.get("billing-quota").quota if "billing-quota" in rate_limit_policies else None,
        quota_remaining_credits=rate_limits.get("billing-quota").remaining if "billing-quota" in rate_limits else None,
        visitor_quota_limit_credits=rate_limit_policies.get("visitor-quota").quota if "visitor-quota" in rate_limit_policies else None,
        visitor_quota_remaining_credits=rate_limits.get("visitor-quota").remaining if "visitor-quota" in rate_limits else None,
        raw_headers=raw_headers,
    )

def _pick_details(data: Any) -> Any:
    if not isinstance(data, dict):
        return None
    if "details" in data:
        return data["details"]
    if "quota" in data:
        return data["quota"]
    if "docs" in data:
        return data["docs"]
    return None

def map_error(r: httpx.Response) -> UapiError:
    code = None
    msg = r.text
    data: Any = None
    try:
        data = r.json()
        code = data.get("code") or data.get("error") or data.get("errCode") or _default_code(r.status_code)
        msg = data.get("message") or data.get("errMsg") or msg
    except Exception:
        code = _default_code(r.status_code)
    status = r.status_code
    meta = extract_meta(r.headers)
    cls = _class_by_code(code, status)
    return cls(code, status, msg, _pick_details(data), data, meta)

def _class_by_code(code: str, status: int):
    c = (code or "").upper()
    mapping = {
        
        "API_ERROR": ApiErrorError,
        
        "AVATAR_NOT_FOUND": AvatarNotFoundError,
        
        "CONVERSION_FAILED": ConversionFailedError,
        
        "FILE_OPEN_ERROR": FileOpenErrorError,
        
        "FILE_REQUIRED": FileRequiredError,
        
        "INSUFFICIENT_CREDITS": InsufficientCreditsError,
        
        "INTERNAL_SERVER_ERROR": InternalServerErrorError,
        
        "INVALID_PARAMETER": InvalidParameterError,
        
        "INVALID_PARAMS": InvalidParamsError,
        
        "NOT_FOUND": NotFoundError,
        
        "NO_MATCH": NoMatchError,
        
        "NO_TRACKING_DATA": NoTrackingDataError,
        
        "PHONE_INFO_FAILED": PhoneInfoFailedError,
        
        "RECOGNITION_FAILED": RecognitionFailedError,
        
        "REQUEST_ENTITY_TOO_LARGE": RequestEntityTooLargeError,
        
        "SERVICE_BUSY": ServiceBusyError,
        
        "TIMEZONE_NOT_FOUND": TimezoneNotFoundError,
        
        "UNAUTHORIZED": UnauthorizedError,
        
        "UNSUPPORTED_CARRIER": UnsupportedCarrierError,
        
        "UNSUPPORTED_FORMAT": UnsupportedFormatError,
        
        "VISITOR_MONTHLY_QUOTA_EXHAUSTED": VisitorMonthlyQuotaExhaustedError,
        
    }
    return mapping.get(c) or ({
        400: InvalidParameterError,
        401: UnauthorizedError,
        402: InsufficientCreditsError,
        404: NotFoundError,
        429: ServiceBusyError,
        500: InternalServerErrorError,
    }.get(status) or UapiError)
