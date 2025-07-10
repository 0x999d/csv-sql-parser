from abc import ABC, abstractmethod
from typing import List, Any


class BaseFilter(ABC):
    
    @abstractmethod
    def _check(*args, **kwargs) -> Any:
        ...

    @abstractmethod
    def get(*args, **kwargs) -> List[List[str]]:
        ...