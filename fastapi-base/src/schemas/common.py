from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel, Field


T = TypeVar("T")


class IResponseBase(BaseModel, Generic[T]):  # type: ignore
    message: str = ""
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    data: Optional[T] = None


class IGetResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Data fetched correctly"
    data: Optional[T] = None


class IPostResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Data created correctly"


class IPutResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Data updated correctly"


class IDeleteResponseBase(IResponseBase[None]):
    message: str = "Data deleted correctly"


class IErrorResponseBase(IResponseBase[None]):
    message: str = "An error occurred"
    error_code: Optional[str | int] = None
    details: Optional[Any] = None
