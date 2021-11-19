from uuid import uuid4

from peewee import TextField, Model, UUIDField, ForeignKeyField

from settings import Settings


class BaseModel(Model):
    class Meta:
        database = Settings.DATABASE


class User(BaseModel):
    id = UUIDField(default=uuid4)
    email = TextField(unique=True, null=True)
    cf = TextField(unique=True, null=True)

    class Meta:
        db_table = 'User'


class ServiceMapper(BaseModel):
    user_id = ForeignKeyField(User, field="id")
    service_one = TextField(null=False)

    class Meta:
        db_table = 'Service'
