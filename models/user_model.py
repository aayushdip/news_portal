from edb import models
from pydantic import EmailStr


class User(models.entity):
    name: str
    email: EmailStr
    username: str
    admin: bool
    subscriber: bool
    hashed_password: str
