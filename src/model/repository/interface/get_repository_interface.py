from abc import ABC, abstractmethod
from typing import Any

class GetRepositoryInterface(ABC):

    @abstractmethod
    def get(self, **kwargs) -> Any:
        pass
