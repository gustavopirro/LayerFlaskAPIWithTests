from src.errors.error_handler import ErrorHandler
from src.model.config.connection import DBConnectionHandler
from src.model.entities.pokemon import Pokemon
from sqlalchemy.exc import IntegrityError
from src.errors.entity_already_exists_exception import EntityAlreadyExistsException
from src.model.repository.interface.pokemon_repository_interface import PokemonRepositoryInterface

class __PokemonRepository(PokemonRepositoryInterface):

    def list(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Pokemon).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def get(self, name):
        with DBConnectionHandler() as db:
            pokemon = db.session.query(Pokemon).filter_by(name=name).first()
            if not pokemon:
                raise Exception('Pokemon not found')
            return pokemon

    def insert(self, name, attack):
        with DBConnectionHandler() as db:
            try:
                data_insert = Pokemon(name=name, attack=attack)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError:
                raise EntityAlreadyExistsException("This entity id already exists at the database!")
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def delete(self, name):
        with DBConnectionHandler() as db:
            try:
                pokemon = db.session.query(Pokemon).filter_by(name=name)
                if not pokemon.count():
                    raise Exception('Pokemon not found')
                pokemon.delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
repository = __PokemonRepository()
print(type(repository))
