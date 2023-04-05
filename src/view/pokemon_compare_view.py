from typing import Type

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controller.interface.pokemon_compare_controller_interface import PokemonCompareControllerInterface

class PokemonCompareView(ViewInterface):
    def __init__(self, controller: Type[PokemonCompareControllerInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        data = http_request.body
        response = self.__controller.run(data)
        

        return HttpResponse(status_code=200, body={ "response": response })
