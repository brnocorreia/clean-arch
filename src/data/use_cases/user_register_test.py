from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = 'bruno'
    last_name = 'bonito'
    age = 19

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert repo.insert_user_attributes['first_name'] == first_name
    assert repo.insert_user_attributes['last_name'] == last_name
    assert repo.insert_user_attributes['age'] == age

    assert response['type'] == "Users"
    assert response['count'] == 1
    assert response['attributes']

def test_register_first_name_error():
    first_name = 'bruno32'
    last_name = 'bonito'
    age = 19

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome inválido para o cadastro'

def test_register_longer_name_error():
    first_name = 'brunoaaaaaaaaaaaaaaaaaaaaaaa'
    last_name = 'bonito'
    age = 19

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome muito grande para o cadastro'
