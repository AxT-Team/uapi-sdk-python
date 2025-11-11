from __future__ import annotations
from typing import Any, Dict, Optional
import httpx

class UapiError(Exception):
    code: str
    status: int
    message: str
    details: Optional[Dict[str, Any]]

    def __init__(self, code: str, status: int, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(f"[{status}] {code}: {message}")
        self.code = code
        self.status = status
        self.message = message
        self.details = details


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


def map_error(r: httpx.Response) -> UapiError:
    code = None
    msg = r.text
    try:
        data = r.json()
        code = data.get("code") or data.get("error") or data.get("errCode") or "API_ERROR"
        msg = data.get("message") or data.get("errMsg") or msg
        details = data.get("details")
    except Exception:
        details = None
    status = r.status_code
    cls = _class_by_code(code, status)
    return cls(code, status, msg, details)

def _class_by_code(code: str, status: int):
    c = (code or "").upper()
    mapping = {
        
        "API_ERROR": ApiErrorError,
        
        "AVATAR_NOT_FOUND": AvatarNotFoundError,
        
        "CONVERSION_FAILED": ConversionFailedError,
        
        "FILE_OPEN_ERROR": FileOpenErrorError,
        
        "FILE_REQUIRED": FileRequiredError,
        
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
        
    }
    return mapping.get(c) or ( {400: InvalidParameterError, 401: UnauthorizedError, 404: NotFoundError, 429: ServiceBusyError, 500: InternalServerError}.get(status) or UapiError )
