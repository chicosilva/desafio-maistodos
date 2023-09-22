from dataclasses import dataclass
from typing import Any, Type

from pydantic import BaseModel

from app.domain.common.exception_base import NotFoundException


@dataclass
class ServiceBase:
    @classmethod
    def query_result(cls, result: list[Any] | dict[str, Any] | Type[BaseModel]) -> Any:
        if result:
            return result
        raise NotFoundException()
