from src.infra.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_register import UserRagister

def test_register():
    first_name = "Hello"
    last_name = "World"
    age = 20

    repo = UsersRepositorySpy()
    user_register = UserRagister(user_repository=repo)

    response = user_register.register(first_name=first_name, last_name=last_name, age=age)

    assert repo.insert_user_attibutes["first_name"] == first_name
    assert repo.insert_user_attibutes["last_name"] == last_name
    assert repo.insert_user_attibutes["age"] == age
    
    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_first_name_error():
    first_name = "Hello11"
    last_name = "World"
    age = 20

    repo = UsersRepositorySpy()
    user_register = UserRagister(user_repository=repo)

    
    try :
        user_register.register(first_name=first_name, last_name=last_name, age=age)
        assert False
    except Exception as exeption:
        assert str(exeption) == 'Nome inválido para a busca'
    