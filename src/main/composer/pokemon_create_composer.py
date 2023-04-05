from src.controller.pokemon_create_controller import PokemonCreateController
from src.view.pokemon_create_view import PokemonCreateView
from src.model.repository.pokemon_repository import repository as pokemon_repository

def pokemon_create_composer():
    pokemon_create_controller = PokemonCreateController(pokemon_repository)
    pokemon_create_view = PokemonCreateView(pokemon_create_controller)
    return pokemon_create_view
