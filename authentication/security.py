from argon2 import PasswordHasher
from models.user import UserModel

ph = PasswordHasher()

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and ph.verify(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)