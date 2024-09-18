from typing import List
from src.data.use_cases.user_finder import UserFinder
from src.domain.models.users import Users
from src.infra.tests.users_repository import UsersRepositorySpy

def test_find():
    first_name = "MeuNome"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)
    response = user_finder.find(first_name=first_name)

    print(repo.select_user_attributes)

    assert repo.select_user_attributes["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != ['']


def test_find_error_in_valid_name():
    first_name = "MeuNome12"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)

    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as exeption:
        assert str(exeption) == "Nome inválido para a busca"


def test_find_error_in_too_long_name():
    first_name = "MeuNomeMeuNomeMeuNomeMeuNomeMeuNomeMeuNome"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)

    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as exeption:
        assert str(exeption) == "Nome muito grande para a busca"


def test_find_error_user_not_found():

    # Overrited
    class UserRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str) -> List[Users]:
            return []

    first_name = "MeuNome"

    repo = UserRepositoryError()
    user_finder = UserFinder(users_repository=repo)

    try:
        user_finder.find(first_name=first_name)
        assert False
    except Exception as exeption:
        assert str(exeption) == "Usuário não encontrado"