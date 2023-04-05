from src.model.config.base import Base
from sqlalchemy import Column, String, Integer

class Pokemon(Base):
    __tablename__ = "pokemons"

    name = Column(String, primary_key=True) 
    attack = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{ self.name, self.attack}"