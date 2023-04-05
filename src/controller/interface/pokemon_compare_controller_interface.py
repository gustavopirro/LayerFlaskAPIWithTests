from abc import ABC, abstractmethod
from typing import Any, Type
from src.model.entities.pokemon import Pokemon

class PokemonCompareControllerInterface(ABC):

    @abstractmethod
    def run(self, pokemonOne: Type[Pokemon], pokemonTwo: Type[Pokemon]) -> Any:
        pass
