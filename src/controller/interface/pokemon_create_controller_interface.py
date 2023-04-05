from abc import ABC, abstractmethod
from typing import Any

class PokemonCreateControllerInterface(ABC):

    @abstractmethod
    def run(self, **kwargs) -> Any:
        pass
