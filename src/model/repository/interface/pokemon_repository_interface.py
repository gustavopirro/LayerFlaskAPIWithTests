from abc import ABC, abstractmethod
from typing import Any
from src.model.repository.interface.create_repository_interface import CreateRepositoryInterface
from src.model.repository.interface.list_repository_interface import ListRepositoryInterface
from src.model.repository.interface.get_repository_interface import GetRepositoryInterface

class PokemonRepositoryInterface(CreateRepositoryInterface, ListRepositoryInterface, GetRepositoryInterface):
    pass