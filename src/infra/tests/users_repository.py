from typing import List
from src.domain.models.users import Users

class UsersRepositorySpy():
    # Class method diz que esse metodo não usa nenhum outro metodo ou atributos
    def __init__(self) -> None:
        self.insert_user_attibutes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attibutes["first_name"] = first_name
        self.insert_user_attibutes["last_name"] = last_name
        self.insert_user_attibutes["age"] = age

        pass

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name

        return [
            Users(1, first_name=first_name, last_name="las", age=43 ),
            Users(1, first_name=first_name, last_name="las", age=42 )
        ]