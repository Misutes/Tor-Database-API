from typing import Any
from uuid import uuid4

from pydantic import BaseModel

from settings import Settings


def str_uuid():
    return str(uuid4())


def encrypt(data):
    return Settings.ENCRYPTOR.encrypt(data)


class User(BaseModel):
    data: dict[str, Any]

    def dict(self, *args, **kwargs):
        obj = super(User, self).dict(*args, **kwargs)
        data = obj.pop("data")

        for key, value in data.items():
            if key[0] == "s" and key[1:].isdigit():
                obj[key] = value
            else:
                obj[key] = encrypt(str(value))
        obj["_id"] = str_uuid()

        return obj


class UpdateUsersData(BaseModel):
    where_field: str
    where_value: str
    field_name: str
    field_value: Any
