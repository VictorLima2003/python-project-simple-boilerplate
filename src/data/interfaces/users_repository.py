from typing import List
from abc import ABC, abstractmethod 
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):
    # Class method diz que esse metodo não usa nenhum outro metodo ou atributo
    @abstractmethod 
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass

    @abstractmethod 
    def select_user(self, first_name: str) -> List[Users]: pass
