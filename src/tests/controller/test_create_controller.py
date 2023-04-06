from src.controller.pokemon_create_controller import PokemonCreateController
from unittest.mock import Mock
from unittest import TestCase
from src.errors.bad_request_exception import BadRequestException
import pytest


class CreateControllerTest(TestCase):

    def test_create_pokemon(self):
        repo_mock = Mock()
        validator_mock = Mock()
        controller = PokemonCreateController(repo_mock, validator_mock)
        pokemon_data = {'pokemon': {'name': 'Pikachu', 'attack': 55}}

        controller.run(pokemon_data)
        
        repo_mock.insert.assert_called_with('Pikachu', 55)

    def test_create_invalid_pokemon(self):
        repo_mock = Mock()
        validator_mock = Mock()
        message = Mock()
        errors = Mock()
        validator_mock.validate.side_effect = BadRequestException(message, errors)

        controller = PokemonCreateController(repo_mock, validator_mock)

        pokemon_data = {'pokemon': {'name': 123, 'attack': 55}}

        with pytest.raises(BadRequestException):
            controller.run(pokemon_data)
        
        repo_mock.insert.assert_not_called()
