from src.controller.interface.pokemon_create_controller_interface import PokemonCreateControllerInterface
from src.model.repository.interface.pokemon_repository_interface import PokemonRepositoryInterface
from src.validators.input_validator import InputValidator
from src.validators.rules.pokemon_id_validator import pokemon_id_validator
from typing import Type

class PokemonCreateController(PokemonCreateControllerInterface):

    def __init__(self, repository: Type[PokemonRepositoryInterface], validator: Type[InputValidator]) -> None:
        self.repository = repository
        self.validator = validator
    
    def run(self, pokemon_data):
        print(pokemon_data)
        self._validate_input(pokemon_data)
        self.repository.insert(pokemon_data['pokemon']['name'], 
                               pokemon_data['pokemon']['attack'])

    def _validate_input(self, data):
        self.validator.validate(data)