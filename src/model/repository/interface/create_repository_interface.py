from abc import ABC, abstractmethod
from typing import Any

class CreateRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, **kwargs) -> Any:
        pass
