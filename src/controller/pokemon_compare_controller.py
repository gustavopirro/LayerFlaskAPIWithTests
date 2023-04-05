from src.controller.interface.pokemon_compare_controller_interface import PokemonCompareControllerInterface
from src.model.repository.interface.pokemon_repository_interface import PokemonRepositoryInterface
from src.validators.interface.validator_interface import ValidatorInterface
from src.model.entities.pokemon import Pokemon

from typing import Type

class PokemonCompareController(PokemonCompareControllerInterface):

    def __init__(self, repository: Type[PokemonRepositoryInterface], validator: Type[ValidatorInterface]) -> None:

        self.repository = repository
        self.validator = validator
    
    def run(self, pokemon_data):
        self._validate_input(pokemon_data)
        
        pokemon_id = pokemon_data['pokemonOne']['name']
        pokemon_id_two = pokemon_data['pokemonTwo']['name']


        pokemon_one = self._fetch_data(pokemon_id)
        pokemon_two = self._fetch_data(pokemon_id_two)

        stronger_pokemon = self._compare_pokemons(pokemon_one, pokemon_two)


        return self._format_response(stronger_pokemon)

    def _validate_input(self, data):
        self.validator.validate(data)

    def _fetch_data(self, id):
        return self.repository.get(id)

    def _compare_pokemons(self, pokemonOne: Pokemon, pokemonTwo: Pokemon):
        if pokemonOne.attack > pokemonTwo.attack:
            return pokemonOne
        return pokemonTwo

    def _format_response(self, pokemon: Pokemon):
        return {'data': f'{pokemon.name} is the stronger pokemon, his attack is {pokemon.attack}'}
