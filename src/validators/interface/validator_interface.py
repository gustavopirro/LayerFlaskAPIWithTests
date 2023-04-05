from abc import ABC, abstractmethod
from typing import Type, Any


class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, data) -> Type[Any]:
        pass
