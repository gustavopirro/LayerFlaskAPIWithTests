from abc import ABC, abstractmethod
from typing import Any

class ListRepositoryInterface(ABC):

    @abstractmethod
    def list(self, **kwargs) -> Any:
        pass
