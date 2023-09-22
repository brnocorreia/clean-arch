from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = 'bruno'
    last_name = 'bonito'
    age = 19

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert response['type'] == "Users"
    assert response['count'] == 1
    assert response['attributes']    
