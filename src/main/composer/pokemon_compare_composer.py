from src.view.pokemon_compare_view import PokemonCompareView
from src.controller.pokemon_compare_controller import PokemonCompareController
from src.model.repository.pokemon_repository import repository as pokemon_repository
from src.validators.input_validator import InputValidator
from src.validators.rules.pokemon_id_validator import pokemon_id_validator

def pokemon_compare_composer():
    pokemon_validator = InputValidator(pokemon_id_validator)
    pokemon_compare_controller = PokemonCompareController(repository=pokemon_repository, validator=pokemon_validator)
    pokemon_compare_view = PokemonCompareView(pokemon_compare_controller)
    return pokemon_compare_view
