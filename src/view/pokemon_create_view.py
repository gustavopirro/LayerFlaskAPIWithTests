from typing import Type

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.pokemon_create_controller_interface import PokemonCreateControllerInterface

from src.validators.input_validator import InputValidator
from src.validators.rules.pokemon_validator import pokemon_validator

class PokemonCreateView(ViewInterface):
    def __init__(self, controller: Type[PokemonCreateControllerInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        body = http_request.body
        response = self.__controller.run(body)

        return HttpResponse(status_code=200, body={ "response": response })
